FROM node:12.16.3

RUN mkdir /code
WORKDIR /code

COPY package.json yarn.lock /code/
RUN yarn install --frozen-lockfile

EXPOSE 8888
