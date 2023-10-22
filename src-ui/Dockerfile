FROM node:20

RUN mkdir /code
WORKDIR /code

COPY package.json yarn.lock /code/
RUN yarn install --frozen-lockfile

EXPOSE 8888
