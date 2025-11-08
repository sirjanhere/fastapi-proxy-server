from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import Response
import httpx

app = FastAPI()

@app.get("/api")
async def proxy(url: str):
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        headers = dict(resp.headers)
        # Ensure CORS header is added
        headers["Access-Control-Allow-Origin"] = "*"
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            headers=headers,
            media_type=resp.headers.get("content-type")
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
