FROM node:16-alpine3.14 AS build
WORKDIR /usr/src/app
COPY ./fe/package.json ./fe/package-lock.json ./
RUN npm install
COPY ./fe/ .
RUN mkdir -p dist/fe
RUN npm run build

FROM nginx:latest
COPY ./fe/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /usr/src/app/dist/ /src/
