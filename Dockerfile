FROM gcr.io/tensorflow/tensorflow:latest-gpu-py3

MAINTAINER Erik Jan de Vries (github.com/erikjandevries)

RUN pip install --upgrade \
        pip \
        keras

RUN apt-get update && \
    apt-get install -y \
        python3-tk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY mnist-learning /repositories/mnist-learning
COPY prepare /repositories/prepare

WORKDIR /repositories/mnist-learning
ENTRYPOINT ["python3"]
CMD [ "train.py" ]
