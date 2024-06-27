import re

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime, timedelta

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):
        if re.match('^(/videos)', request.url.path):          
            # Obtiene el token de autorización para los endpoint protegidos
            auth_token = request.headers.get("auth")
            if not auth_token or len(auth_token) <= 0:
              return JSONResponse(
                  status_code=401,
                  content={"message": "Unauthorized."}
              )
          
        # Proceder con la solicitud
        response = await call_next(request)
        return response
