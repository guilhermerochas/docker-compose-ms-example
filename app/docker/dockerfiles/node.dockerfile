FROM node:10.16-alpine
WORKDIR /home
COPY ./services/api/package.json .
COPY ./services/api/node_modules .
RUN npm install --quiet
EXPOSE 3000
CMD ["node", "index.js"]