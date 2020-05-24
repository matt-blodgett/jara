#!/usr/bin/env bash

set -ex

echo "Build DB container..."
docker-compose build db

echo "Build API container..."
docker-compose build api

echo "Build UI container..."
docker-compose build ui

echo "Build dist..."
docker-compose run --rm --no-deps ui yarn run build
