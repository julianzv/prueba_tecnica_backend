# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos y instalar dependencias
COPY requirements-python.txt .
RUN pip install --no-cache-dir -r requirements-python.txt

# Copiar el resto del código del backend al contenedor
COPY . /app/

# Exponer el puerto en el que Flask se ejecutará
EXPOSE 8080

# Definir el comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
