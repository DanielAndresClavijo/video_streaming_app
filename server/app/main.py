from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.video_routes import router as video_router
from app.api.auth_routes import router as auth_router
from app.domain.services.middleware_service import MiddlewareService

app = FastAPI(
    title="Video Streaming App"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:*"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE", "PUT"],
    allow_headers=[
        "*",
        # "accept",
        # "Content-Type",
        # "Authorization",
        # "X-CSRF-Token",
    ],
)

middlewares = MiddlewareService()
app.add_middleware(middlewares.rate_limiting)
app.add_middleware(middlewares.auth)


app.include_router(video_router, prefix="/videos")
app.include_router(auth_router, prefix="/auth")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
