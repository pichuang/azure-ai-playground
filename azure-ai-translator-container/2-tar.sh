#!/bin/bash

cd ..

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

tar -czvf "azure-ai-translator-container-archive-${TIMESTAMP}.tar.gz" azure-ai-translator-container