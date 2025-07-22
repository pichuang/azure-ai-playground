#!/bin/bash

source .env

AZURE_REGION=${AZURE_REGION}
AZURE_SUBSCRIPTION_KEY=${AZURE_SUBSCRIPTION_KEY}

curl --location --request GET "https://${AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/voices/list" \
--header "Ocp-Apim-Subscription-Key: ${AZURE_SUBSCRIPTION_KEY}"
