#!/bin/bash

mkdir -p ./azure-ai-translator/models
mkdir -p ./azure-ai-translator/logs
mkdir -p ./azure-ai-translator/license
sudo chown -R 65532:65532 ./azure-ai-translator
sudo chmod -R o+w ./azure-ai-translator
sudo setfacl -R -m d:o::rw,o::rw ./azure-ai-translator

