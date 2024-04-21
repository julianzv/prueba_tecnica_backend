# Usar una imagen base de Node.js
FROM node:16

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de definición de paquetes y instalar dependencias
COPY package.json ./
RUN yarn install

# Copiar el resto de los archivos del frontend
COPY . /app/

# Construir la aplicación de React para producción
RUN yarn build

# Exponer el puerto para el servidor de desarrollo (opcional)
EXPOSE 3000

# Servir la aplicación usando un servidor estático
CMD ["yarn", "start"]
