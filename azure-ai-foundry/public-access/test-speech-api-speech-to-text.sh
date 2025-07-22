#!/bin/bash

source .env

AZURE_REGION=${AZURE_REGION}
AZURE_SUBSCRIPTION_KEY=${AZURE_SUBSCRIPTION_KEY}
OUTPUT_FILENAME=${OUTPUT_FILENAME}

curl --location --request POST "https://${AZURE_REGION}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US&format=detailed" \
--header "Ocp-Apim-Subscription-Key: ${AZURE_SUBSCRIPTION_KEY}" \
--header "Content-Type: audio/wav; codecs=audio/pcm; samplerate=16000" \
--data-binary "@${OUTPUT_FILENAME}"