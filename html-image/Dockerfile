FROM bitnami/node:16.17.0-debian-11-r6
WORKDIR /src
COPY package.json .
RUN npm install -g live-server
RUN npm i
COPY . .
CMD ["npm", "run", "dev"]