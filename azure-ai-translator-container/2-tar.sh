#!/bin/bash

cd ..

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

tar -czvpf "azure-ai-translator-container-archive-${TIMESTAMP}.tar.gz" azure-ai-translator-container