FROM gcr.io/tensorflow/tensorflow:latest-gpu-py3

MAINTAINER Erik Jan de Vries (github.com/erikjandevries)

# Upgrade pip
RUN pip install --upgrade \
        pip \
        keras

COPY mnist-learning /repositories/mnist-learning
COPY prepare /repositories/prepare

WORKDIR /repositories/mnist-learning
ENTRYPOINT ["python3"]
CMD [ "train.py" ]
