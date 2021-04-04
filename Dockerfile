FROM node:14.16.0-alpine3.12
RUN mkdir -p /home/node/app

WORKDIR /home/node/app

COPY package*.json ./
RUN npm install

COPY . .

