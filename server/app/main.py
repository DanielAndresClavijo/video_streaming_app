from fastapi import FastAPI
from app.api.video_routes import router as video_router
from app.api.auth_routes import router as auth_router

app = FastAPI()

app.include_router(video_router, prefix="/videos")
app.include_router(auth_router, prefix="/auth")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
