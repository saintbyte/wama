FROM node:20
WORKDIR /code
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
COPY src/wama/package.json package.json
COPY src/wama/package-lock.json package-lock.json
RUN npm install
COPY ./src/wama  .
CMD [ "npm", "run", "dev"]
