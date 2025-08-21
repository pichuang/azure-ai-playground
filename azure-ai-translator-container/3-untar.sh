#!/bin/bash

sudo tar -xzvpf package-azure-ai-translator-container-*.tar.gz
cd ./azure-ai-translator-container/

# Fix permissions
sudo chown -R 65532:65532 ./azure-ai-translator
sudo chmod -R o+rw ./azure-ai-translator

# Load Container Image
docker load -i ./archive/oci-azure-translator-text-translation.tar