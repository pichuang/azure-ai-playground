#!/bin/bash

mkdir -p ./root/logs
mkdir -p ./root/share

sudo chown -R 65532:65532 ./root/logs
sudo chown -R 65532:65532 ./root/share
sudo chmod -R o+w ./root