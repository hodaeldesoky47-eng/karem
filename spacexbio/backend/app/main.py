"""
SpaceXBio FastAPI Application Entrypoint
English: Minimal FastAPI app with health check and root endpoint.
العربية: تطبيق FastAPI مصغر مع نقطة فحص الصحة ونقطة الجذر.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SpaceXBio API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """English: Root welcome route. العربية: مسار ترحيبي رئيسي."""
    return {"message": "SpaceXBio API is running"}


@app.get("/health")
def health_check():
    """English: Simple health check. العربية: فحص صحة بسيط."""
    return {"status": "ok"}



