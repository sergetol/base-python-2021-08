#!/bin/sh
set -e

docker build -f Dockerfile -t homework_03-app:latest ./
docker run -ti --rm -p 8000:8000/tcp homework_03-app:latest
