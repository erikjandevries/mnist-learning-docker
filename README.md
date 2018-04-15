# mnist-learning-docker
Learning MNIST using TensorFlow in a Docker container


### Prepare

_Based on: https://github.com/datapythonista/mnist_

You can use the provided scripts to download the MNIST dataset from:
http://yann.lecun.com/exdb/mnist/


Running the script `download-mnist-data.py --out-dir=<out_dir>` downloads the training and test sets into
the following folder/file structure:

 - \<out_dir> / \<train|test> / \<label> / \<image_index>.png


### Build Docker image

To build the Docker image, run the `build.sh` script.


### Train the model

To train the model, run the Docker image with the `train.sh` script.

### Test predictions

To test the predictions of the model, run the Docker image with the
`test_predictions.sh` script.

This will load the pretrained model from disk and test the predictions on
10 batches of image. **For each failed prediction**, the image will be displayed
and the true and predicted labels will be printed to the console.
