from keras.preprocessing.image import ImageDataGenerator

from model import get_model


def main(batch_size=32):
    train_data_generator = ImageDataGenerator(
        rescale=1. / 255
    )
    test_data_generator = ImageDataGenerator(
        rescale=1. / 255
    )

    train_generator = train_data_generator.flow_from_directory(
        directory='/mnt/data/Data/mnist/train/',
        target_size=(28, 28),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical'
    )

    validation_generator = test_data_generator.flow_from_directory(
        directory='/mnt/data/Data/mnist/test/',
        target_size=(28, 28),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical'
    )

    model = get_model(simple=False)
    model.summary()
    model.fit_generator(
        generator=train_generator,
        steps_per_epoch=60000 // batch_size,
        epochs=3,
        validation_data=validation_generator,
        validation_steps=10000 // batch_size)
    model.save_weights('/mnt/data/Data/mnist/model.h5')


if __name__ == '__main__':
    main(batch_size=16)
