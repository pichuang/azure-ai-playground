#!/bin/bash

source .env

AZURE_REGION=${AZURE_REGION}
AZURE_SUBSCRIPTION_KEY=${AZURE_SUBSCRIPTION_KEY}
OUTPUT_FILENAME=${OUTPUT_FILENAME}
TOKEN_FILENAME=${TOKEN_FILENAME}

curl -X POST \
  "https://${AZURE_REGION}.api.cognitive.microsoft.com/sts/v1.0/issueToken" \
  -H "Ocp-Apim-Subscription-Key: $AZURE_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Content-Length: 0" > ${TOKEN_FILENAME}

# echo "Access token: $(cat $TOKEN_FILENAME)"

curl -X POST \
  "https://${AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1" \
  -H "Authorization: Bearer $(cat ${TOKEN_FILENAME})" \
  -H "Content-Type: application/ssml+xml" \
  -H "X-Microsoft-OutputFormat: riff-24khz-16bit-mono-pcm" \
  -d '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="zh-TW">
        <voice name="zh-TW-HsiaoChenNeural">
          Hello, this is a test message. Phil Huang is happy to be here.
          This is a health check for Azure Text-to-Speech service.
        </voice>
      </speak>' \
  --output ${OUTPUT_FILENAME}

file ${OUTPUT_FILENAME}

rm ${TOKEN_FILENAME}