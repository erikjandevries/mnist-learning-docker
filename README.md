# mnist-learning-docker
Learning MNIST using TensorFlow in a Docker container


### Prepare

_Based on: https://github.com/datapythonista/mnist_

You can use the provided scripts to download the MNIST dataset from:
http://yann.lecun.com/exdb/mnist/


Running the script `download-mnist-data.py --out-dir=<out_dir>` downloads the training and test sets into
the following folder/file structure:

 - \<out_dir> / \<train|test> / \<label> / \<image_index>.png
