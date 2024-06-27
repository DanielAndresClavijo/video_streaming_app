import time
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime, timedelta

class RateLimitingMiddleware(BaseHTTPMiddleware):
    # Configuraciones de limitación de velocidad
    RATE_LIMIT_DURATION = timedelta(seconds=30)
    RATE_LIMIT_REQUESTS = 60

    def __init__(self, app):
        super().__init__(app)
        # Diccionario para almacenar recuentos de solicitudes para cada IP
        self.request_counts = {}

    async def dispatch(self, request, call_next):
        # Obtener la dirección IP del cliente
        client_ip = request.client.host

        # Compruebe si la IP ya está presente en request_counts
        request_count, last_request = self.request_counts.get(client_ip, (0, datetime.min))

        # Calcular el tiempo transcurrido desde la última solicitud.
        elapsed_time = datetime.now() - last_request

        if elapsed_time > self.RATE_LIMIT_DURATION:
            # Si el tiempo transcurrido es mayor que la duración del límite de velocidad, restablezca el recuento
            request_count = 1
        else:
            if request_count >= self.RATE_LIMIT_REQUESTS:
                # Si el recuento de solicitudes excede el límite de tasa, devolverá una respuesta JSON con un mensaje de error
                return JSONResponse(
                    status_code=429,
                    content={"message": "Rate limit exceeded. Please try again later."}
                )
            request_count += 1

        # Actualice el recuento de solicitudes y la marca de tiempo de la última solicitud para la IP
        self.request_counts[client_ip] = (request_count, datetime.now())

        # Proceder con la solicitud
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        
        response.headers["X-Process-Time"] = str(process_time)
        
        return response
