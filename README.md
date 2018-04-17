# mnist-learning-docker

Learning MNIST using TensorFlow in a Docker container


## Prepare
You will need the MNIST data set in order to run these Docker images

You can use the provided scripts, based on: https://github.com/datapythonista/mnist,
to download the MNIST dataset from: http://yann.lecun.com/exdb/mnist/


Running the script `download-mnist-data.py --out-dir=<out_dir>` downloads the training and test sets into
the required folder/file structure:

 - \<out_dir> / \<train|test> / \<label> / \<image_index>.png

By default `<out_dir>="/mnt/data/Data/mnist"` 

## Basic Docker image

In this image, you will define and train a TensorFlow model using Keras.
After preparing the data, you will need to run the following three scripts.

#### Build the Docker image

To build the Docker image, run the `build.sh` script.

#### Train the model

To train the model, run the Docker image with the `train.sh` script.

Depending on your hardware, this will take a while.
With an Nvidia Geforce 1070 it takes about 25s per epoch.
By default the script is set up to run for 3 epochs.

#### Test predictions

To test the predictions of the model, run the Docker image with the
`test_predictions.sh` script.

This will load the pretrained model from disk and test the predictions on
10 batches of image. For each failed prediction, the image will be displayed,
and the true and predicted labels will be printed to the console.
