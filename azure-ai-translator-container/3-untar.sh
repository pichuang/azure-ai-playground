#!/bin/bash

tar -xzvpf azure-ai-translator-container-archive-*.tar.gz
cd ./azure-ai-translator-container/

# Fix permissions
sudo chown -R 65532:65532 ./azure-ai-translator
sudo chmod -R o+w ./azure-ai-translator