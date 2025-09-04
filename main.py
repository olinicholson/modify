from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(
    title="FastAPI Simple Service",
    description="A simple FastAPI service",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "FastAPI Simple Service is running!",
        "status": "healthy",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    """Health check for Cloud Run"""
    return {
        "status": "healthy",
        "service": "fastapi-simple"
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
