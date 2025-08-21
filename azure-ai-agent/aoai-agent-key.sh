#!/bin/bash


# https://learn.microsoft.com/en-us/rest/api/aifoundry/aiagents/
# The API follows the same protocol as the Azure OpenAI Assistants API. This allows you to use existing OpenAI-compatible tools and SDKs with minimal configuration changes.


source .env
curl --request POST \
  --url $AZURE_AI_FOUNDRY_PROJECT_ENDPOINT/assistants?api-version=2025-05-01 \
  -H "Ocp-Apim-Subscription-Key: $AZURE_AI_FOUNDRY_PROJECT_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "instructions": "You are not a helpful agent.",
    "name": $AGENT_NAME,
    "tools": [{"type": "code_interpreter"}],
    "model": $DEPLOYMENT_NAME
  }'