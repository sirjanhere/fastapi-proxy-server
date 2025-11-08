# Run the app and submit to TDS portal

Follow these steps to install Uvicorn, run the ASGI app, and submit the required URL to the TDS portal.
> Important: The portal expects the endpoint `http://127.0.0.1:8000/api`. Keep the server running while you submit in the TDS portal.

## 1. (Optional) Create and activate a virtual environment
```bash
# create a venv (recommended)
python3 -m venv .venv

# activate (Linux / macOS)
source .venv/bin/activate

# activate (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

## 2. Install dependencies (including uvicorn)
```bash
pip install -r requirements.txt
```

## 3. Run the server with Uvicorn
Run Uvicorn serving the `app` object from `main.py` on all interfaces and port 8000:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
This will run in the foreground. Leave this terminal open while you submit the URL in the TDS portal.

## 4. Verify the endpoint locally
Before submitting to the TDS portal, confirm the endpoint responds:
```bash
curl -i http://127.0.0.1:8000/api
```
You should see an HTTP response (200 or other expected code and body depending on your app).

## 6. Submit to TDS portal
- In the TDS portal, submit the URL:
  - `http://127.0.0.1:8000/api`
- Make sure the server process from step 3 or 4 is running while you complete the submission.
