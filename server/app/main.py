from fastapi import FastAPI
from app.api.video_routes import router as video_router

app = FastAPI()

app.include_router(video_router, prefix="/videos")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
