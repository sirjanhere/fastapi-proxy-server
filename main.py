from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Add global CORS support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def proxy(url: str):
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            media_type=resp.headers.get("content-type")
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
