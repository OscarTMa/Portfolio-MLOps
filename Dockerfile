# 1. Imagen base: Usamos un Python ligero (slim) para que descargue rápido
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar primero las dependencias (truco para que Docker sea más rápido al reconstruir)
COPY requirements.txt .

# 4. Instalar las librerías
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código (src y models)
COPY src/ src/
COPY models/ models/

# 6. Exponer el puerto 8000 al mundo exterior
EXPOSE 8000

# 7. El comando que se ejecuta al encender el contenedor
# Usamos "0.0.0.0" para que sea accesible desde fuera del contenedor
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
