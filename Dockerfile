FROM gcr.io/tensorflow/tensorflow:latest-gpu-py3

MAINTAINER Erik Jan de Vries (github.com/erikjandevries)

RUN apt-get update && \
    apt-get install -y \
        python3-tk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade \
        pip \
        keras

COPY prepare /repositories/prepare
COPY mnist-learning /repositories/mnist-learning

WORKDIR /repositories/mnist-learning
ENTRYPOINT ["python3"]
CMD [ "train.py" ]
