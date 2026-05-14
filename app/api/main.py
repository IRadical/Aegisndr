from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="NDR Plataform with Zeek and Suricata integration",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "AegisNDR API is running", "satatus": "active"}
