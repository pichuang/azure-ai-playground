#!/bin/bash

source .env

ENDPOINT_TRANSLATOR=${ENDPOINT_TRANSLATOR}
AZURE_SUBSCRIPTION_KEY=${AZURE_SUBSCRIPTION_KEY}
TO_LANG=${TO_LANG}
TO_LANG_2=${TO_LANG_2}
AZURE_REGION=${AZURE_REGION}
TEXT=${TEXT}

curl -X POST "${ENDPOINT_TRANSLATOR}&to=${TO_LANG}&to=${TO_LANG_2}" -H "Ocp-Apim-Subscription-Key: ${AZURE_SUBSCRIPTION_KEY}" -H "Ocp-Apim-Subscription-Region: ${AZURE_REGION}" -H "Content-Type: application/json; charset=UTF-8" -d "[{'Text':'${TEXT}'}]"; echo