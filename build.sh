#!/bin/bash

source config.sh

echo "Building Docker image: ${docker_image_id}"

docker build -t ${docker_image_id} .
docker image prune -f

# docker push ${image_name}
