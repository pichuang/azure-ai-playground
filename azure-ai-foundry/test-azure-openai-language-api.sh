#!/bin/bash

source .env

ENDPOINT=${ENDPOINT}
AZURE_REGION=${AZURE_REGION}
AZURE_SUBSCRIPTION_KEY=${AZURE_SUBSCRIPTION_KEY}

curl -X POST "${ENDPOINT}/language/:analyze-text?api-version=2022-05-01" \
-H "Ocp-Apim-Subscription-Key: ${AZURE_SUBSCRIPTION_KEY}" \
-H "Content-Type: application/json" \
-d '{
    "kind": "LanguageDetection",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput":{
        "documents":[
            {
                "id":"1",
                "text": "小飛機 is an CNCF ambassador, he is a senior cloud solution architect at Microsoft Taiwan."
            },
            {
                "id":"2",
                "text": "Phil Huang 是一位台灣微軟架構師，專注於如何通靈"
            }
        ]
    }
}'