#!/bin/bash

source config.sh

echo "Granting root user access to X display"
xhost +si:localuser:root

echo "Entering shell for Docker image: ${docker_image_id}"
nvidia-docker run -it --rm \
    --name ${docker_image_name} \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    --env="DISPLAY" \
    --device=/dev/dri:/dev/dri \
    --entrypoint="/bin/bash" \
    --volume /mnt/data:/mnt/data \
    ${docker_image_id}

echo "Revoking root user access to X display"
xhost -si:localuser:root
