#!/bin/bash

source .env

ENDPOINT=${ENDPOINT}
AZURE_REGION=${AZURE_REGION}
AZURE_SUBSCRIPTION_KEY=${AZURE_SUBSCRIPTION_KEY}

response_headers=$(mktemp)
http_status=$(curl -s -D "${response_headers}" -o /dev/null -w "%{http_code}" -X POST \
  "${ENDPOINT}/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-07-31-preview" \
  -H "Content-Type: application/json" \
  -H "Ocp-Apim-Subscription-Key: ${AZURE_SUBSCRIPTION_KEY}" \
  --data-ascii '{"urlSource": "https://transflow.tw/wp-content/uploads/2025/04/IMG_1748-scaled.jpg"}')

echo "HTTP Status Code: ${http_status}"
echo "HTTP Response Header: $(cat ${response_headers})"

location=$(grep -i "^operation-location:" "${response_headers}" | awk '{print $2}' | tr -d '\r\n')
analyze_id=$(echo "${location}" | grep -oE '[0-9a-fA-F-]{8}-[0-9a-fA-F-]{4}-[0-9a-fA-F-]{4}-[0-9a-fA-F-]{4}-[0-9a-fA-F-]{12}')

echo "Analyze ID: ${analyze_id}"
echo "Waiting for analysis to complete after 10 seconds..."
sleep 10

rm -f "${response_headers}"

# Put analyze result
curl -i -X GET \
-H "Ocp-Apim-Subscription-Key: ${AZURE_SUBSCRIPTION_KEY}" \
"${ENDPOINT}/documentintelligence/documentModels/prebuilt-layout/analyzeResults/${analyze_id}?api-version=2024-07-31-preview"

