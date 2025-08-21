#!/bin/bash

# Check .env is existing
if [ ! -f .env ]; then
  echo ".env file is missing"
  echo "Please create a .env file based on the .env.example file"
  exit 1
fi

docker compose -f download-models-docker-compose.yaml up
