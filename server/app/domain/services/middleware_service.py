from app.infrastructure.rate_limiting_middleware import RateLimitingMiddleware
from app.infrastructure.auth_middleware import AuthMiddleware


class MiddlewareService:
    def __init__(self):
        self.rate_limiting = RateLimitingMiddleware
        self.auth = AuthMiddleware
    
    