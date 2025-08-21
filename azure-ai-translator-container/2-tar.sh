#!/bin/bash

cd ..

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
TARBALL_NAME="package-azure-ai-translator-container-${TIMESTAMP}.tar.gz"

sudo tar -czvpf "$TARBALL_NAME" azure-ai-translator-container
mv "$TARBALL_NAME" ./azure-ai-translator-container/archive/