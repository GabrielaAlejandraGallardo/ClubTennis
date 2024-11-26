# Usa una imagen base  
FROM node:14  

# Establece el directorio de trabajo  
WORKDIR /usr/src/app  

# Copia package.json y package-lock.json  
COPY package*.json ./  

# Instala las dependencias  
RUN npm install  

# Copia el resto del código de la aplicación  
COPY . .  

# Expone el puerto en que la aplicación escucha  
EXPOSE 3000  

# Comando para ejecutar la aplicación  
CMD ["node", "app.js"]
