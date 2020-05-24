#!/usr/bin/env bash

echo "Running Django only in debug mode (with pdb support)"
docker-compose run -p 8000:8000 --rm api
