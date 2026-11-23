from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "knowledge-flow-explorer",
        "revision": "1.0.0",
        "time": datetime.now(timezone.utc).isoformat(),
    }

