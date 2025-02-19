# Video Streaming App

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Estado: En Progreso](https://img.shields.io/badge/estado-En%20progreso-yellow.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Último Commit](https://img.shields.io/github/last-commit/DanielAndresClavijo/video_streaming_app.svg)


Una aplicación de transmisión de video en vivo, compuesta por una aplicación cliente multiplataforma desarrollada con Flutter y un servidor backend construido con Python FastApi.

## Descripción

Video Streaming App integra una aplicación cliente y un servidor backend para ofrecer transmisión de video en tiempo real con baja latencia. La aplicación cliente, desarrollada en Flutter (versión 3.22.0), se ejecuta en múltiples plataformas (iOS, Android, Web y Windows). El servidor, implementado con Python FastApi (Python 3.12.3), gestiona la lógica de transmisión y la comunicación entre el cliente y el backend. Además, se utiliza Supabase para la autenticación y gestión de videos.

## Características

- **Transmisión en tiempo real:** Visualiza y transmite video en vivo con baja latencia.
- **Arquitectura cliente-servidor:** Separa la interfaz de usuario (cliente) de la lógica de negocio (servidor).
- **Aplicación Multiplataforma:** Desarrollada en Flutter, soporta iOS, Android, Web y Windows.
- **Backend escalable:** Utiliza Python FastApi para ofrecer un servicio rápido y eficiente.
- **Autenticación con Supabase:** Gestión de usuarios y autenticación a través de Supabase.

## Tecnologías Utilizadas

- **Flutter (Dart):** Desarrollo de la aplicación cliente (versión 3.22.0).
- **Python FastApi:** Construcción del servidor backend con Python 3.12.3.
- **Supabase:** Utilizado para la autenticación y gestión de videos.

## Requisitos

- **Sistema Operativo:** Compatible con iOS, Android, Web y Windows.
- **Dependencias:**
  - [Flutter SDK](https://flutter.dev/docs/get-started/install) (versión 3.22.0) para el desarrollo y ejecución de la aplicación cliente.
  - Python 3.12.3 y FastApi para ejecutar el servidor.
  - Base de datos (MySQL, PostgreSQL u otra) para el almacenamiento seguro de la información.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/DanielAndresClavijo/video_streaming_app.git
cd video_streaming_app
```

### 2. Configuración del entorno para el servidor

1. **Crear un entorno virtual** (recomendado):

   ```bash
   cd server
   python -m venv venv
   ```

2. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar las dependencias de Python:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno**  
   Para el correcto funcionamiento del servidor, asegúrate de configurar las siguientes variables de entorno:

   - `VIDEO_DIRECTORY`: Directorio donde se almacenarán los videos.
   - `SUPABASE_VIDEOS_BUCKET_ID`: Identificador del bucket en Supabase destinado a los videos.
   - `SUPABASE_URL`: URL de la instancia de Supabase.
   - `SUPABASE_KEY`: API Key de Supabase para acceder a sus servicios.
   - `JWT_SECRET`: Clave secreta utilizada para la generación y validación de tokens JWT.

   Puedes crear un archivo `.env` en la carpeta del servidor con estas variables para facilitar la configuración.

### 3. Configuración del entorno para el cliente

Asegúrate de tener instalado el Flutter SDK (versión 3.22.0) y configura tu entorno siguiendo la [documentación oficial de Flutter](https://flutter.dev/docs/get-started/install).

### 4. Ejecución de la aplicación

- **Servidor:**  
  Inicia el servidor FastApi:
  
  ```bash
  cd server
  uvicorn main:app --reload
  ```

- **Cliente:**  
  Ejecuta la aplicación Flutter:
  
  ```bash
  cd app
  flutter run
  ```

## Uso

- **Servidor:** Una vez iniciado, el servidor FastApi gestionará las peticiones y coordinará la transmisión en vivo, además de manejar la autenticación y almacenamiento de videos a través de Supabase.
- **Cliente:** La aplicación Flutter se conectará al servidor para iniciar y gestionar la transmisión de video. Asegúrate de configurar correctamente la URL del servidor en la aplicación.

## Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. Realiza un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección:

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. Realiza tus cambios y haz commit:

   ```bash
   git commit -m "Añadida nueva funcionalidad X"
   ```

4. Envía tu pull request.

Por favor, sigue las buenas prácticas de desarrollo y documenta tus cambios adecuadamente.

## Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.

```
MIT License

Copyright (c) 2025 Daniel Andrés Clavijo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactar al autor:

- **Daniel Andrés Clavijo**
- [Perfil de GitHub](https://github.com/DanielAndresClavijo)
