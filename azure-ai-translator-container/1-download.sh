#!/bin/bash

# Check .env is existing
if [ ! -f .env ]; then
  echo ".env file is missing"
  echo "Please create a .env file based on the .env.example file"
  echo "Command:"
  echo "cp .env.example .env"
  exit 1
fi

source .env

# Check TRANSLATOR_KEY is not empty
if [ -z "$TRANSLATOR_KEY" ]; then
  echo "TRANSLATOR_KEY is missing"
  exit 1
fi

logfile="download-models_$(date +%Y%m%d_%H%M%S).log"

docker compose \
    -f download-models-docker-compose.yaml up \
    > "$logfile" 2>&1

echo "====================="
echo "MODELS (Please copy the following string)"
echo "====================="
grep "docker run.*-e MODELS=" "$logfile" | head -n1 \
  | sed -E 's/.*-e MODELS=([^[:space:]]*).*/\1/'


echo "====================="
echo "TRANSLATORSYSTEMCONFIG (Please copy the following string)"
echo "====================="
grep "docker run.*-e TRANSLATORSYSTEMCONFIG=" "$logfile" | head -n1 \
  | sed -E 's/.*-e TRANSLATORSYSTEMCONFIG=([^[:space:]]*).*/\1/'