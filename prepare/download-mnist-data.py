import argparse
import os
import scipy.misc

import mnist


def save(subset, images, labels, out_dir):
    for i in range(images.shape[0]):
        image = scipy.misc.toimage(images[i, :, :] * -1 + 256)
        label = labels[i]

        dir_name = "{}/{}/{}".format(out_dir, subset, label)
        os.makedirs(dir_name, exist_ok=True)

        scipy.misc.imsave("{}/{}.png".format(dir_name, i),
                          image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir",
                        dest="out_dir",
                        default="/mnt/data/Data/mnist",
                        help="Output directory in which to save the image files")
    args = parser.parse_args()

    print("Downloading training set...")
    train_images = mnist.train_images()
    train_labels = mnist.train_labels()

    print("Downloading test set...")
    test_images = mnist.test_images()
    test_labels = mnist.test_labels()

    print("Saving training images...")
    save('train', train_images, train_labels, args.out_dir)
    print("Saving test images...")
    save('test', test_images, test_labels, args.out_dir)
    print("Done")
