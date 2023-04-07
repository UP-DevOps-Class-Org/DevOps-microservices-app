#Each instruction in this file creates a new layer
#Here we are getting our node as Base image
FROM node:14

#Creating a new directory for app files and setting path in the container
WORKDIR /app

#setting working directory in the container
WORKDIR /usr/src/app

#copying the package.json file(contains dependencies) from project source dir to container dir
COPY package.json .

RUN npm install

COPY . .

CMD npm start