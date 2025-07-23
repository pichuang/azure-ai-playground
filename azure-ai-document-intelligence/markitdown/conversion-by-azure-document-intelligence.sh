#!/bin/bash

source .env
ENDPOINT_DOCUMENT_INTELLIGENCE="https://aif-pichuang-jpe.services.ai.azure.com/"

markitdown 衛生福利部醫療領域資通系統資安防護基準核定本.pdf \
    --output test-azure-di.md \
    --use-docintel \
    --endpoint "${ENDPOINT_DOCUMENT_INTELLIGENCE}"