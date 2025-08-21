#!/bin/bash

mkdir -p ./azure-ai-translator/models
mkdir -p ./azure-ai-translator/logs
mkdir -p ./azure-ai-translator/license
sudo chown -R 65532:65532 ./azure-ai-translator
sudo chmod -R o+w ./azure-ai-translator


# Download Container Image
docker pull mcr.microsoft.com/azure-cognitive-services/translator/text-translation:latest

# Verified Container Image
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.ID}}"

# Save Container image
docker save -o azure-translator-text-translation.tar mcr.microsoft.com/azure-cognitive-services/translator/text-translation:latest

# Check tarball
ls -lh azure-translator-text-translation.tar