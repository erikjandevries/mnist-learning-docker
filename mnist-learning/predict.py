from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np


from model import get_model


def main(batch_size=32):
    train_data_generator = ImageDataGenerator(
        rescale=1. / 255
    )
    test_data_generator = ImageDataGenerator(
        rescale=1. / 255
    )

    # train_generator = train_data_generator.flow_from_directory(
    #     directory='/mnt/data/Data/mnist/train/',
    #     target_size=(28, 28),
    #     color_mode='grayscale',
    #     batch_size=batch_size,
    #     class_mode='categorical'
    # )

    validation_generator = test_data_generator.flow_from_directory(
        directory='/mnt/data/Data/mnist/test/',
        target_size=(28, 28),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical'
    )

    model = get_model(simple=False)
    model.summary()
    model.load_weights('/mnt/data/Data/mnist/model.h5')

    for b in range(10):
        batch = validation_generator.next()
        predictions = model.predict(x=batch[0])

        for i in range(batch[0].shape[0]):
            image = batch[0][i, :, :, 0]
            label = np.argmax(batch[1][i])
            prediction = np.argmax(predictions[i])

            if not label == prediction:
                print("Batch: {} - Label {} - Prediction {}".format(b, label, prediction))
                plt.imshow(image, cmap='gray')
                plt.show()


if __name__ == '__main__':
    main(batch_size=16)
