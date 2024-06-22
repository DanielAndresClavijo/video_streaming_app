# Usar una imagen base oficial de Python
FROM python:3.12.3-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos y la aplicación al contenedor
COPY server/requirements.txt requirements.txt
COPY server/app app
COPY server/.env .env

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que la aplicación estará corriendo
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
