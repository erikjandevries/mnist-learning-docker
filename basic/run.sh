#!/bin/bash

DOCKER_COMMAND=$1

source config.sh

echo "Granting root user access to X display"
xhost +si:localuser:root

echo "Running Docker image: ${docker_image_id}"
nvidia-docker run -it --rm \
    --name ${docker_image_name} \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    --env="DISPLAY" \
    --device=/dev/dri:/dev/dri \
    --volume /mnt/data/Data/mnist:/mnt/data/Data/mnist \
    --workdir /repositories/mnist-learning \
    ${docker_image_id} ${DOCKER_COMMAND}

echo "Revoking root user access to X display"
xhost -si:localuser:root
