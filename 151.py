
import os

import tensorflow as tf
from tensorflow import keras

# maxHeight = 94
# maxWidth = 80

newWidth = 64
newHeight = 64

def loadImages():
    path = "./testing"
    imgHeight = 64
    imgWidth = 64
    batchSize = 32
    return tf.keras.preprocessing.image_dataset_from_directory(
        path,
        labels="inferred",
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(imgHeight, imgWidth),
        batch_size=batchSize
    )

def buildModel():
    imgHeight = 64
    imgWidth = 64
    layers = 32
    numClasses = 151
    activation = "relu"

    return tf.keras.Sequential([
        keras.layers.experimental.preprocessing.Rescaling(1. / 255),
        keras.layers.Conv2D(imgHeight, 3, activation=activation),
        keras.layers.MaxPool2D(),
        keras.layers.Conv2D(imgHeight, 3, activation=activation),
        keras.layers.MaxPool2D(),
        keras.layers.Conv2D(imgHeight, 3, activation=activation),
        keras.layers.MaxPool2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(layers, activation=activation),
        keras.layers.Dense(numClasses)
    ])

def cacheImages(images):
    AUTOTUNE = tf.data.experimental.AUTOTUNE

    return images.cache().prefetch(buffer_size=AUTOTUNE)

def classify151():
    train_images = loadImages()
    validation_images = loadImages()

    class_names = train_images.class_names

    print(class_names)

    # train_images = cacheImages(train_images)
    # validation_images = cacheImages(validation_images)

    poke_model = buildModel()

    poke_model.compile(
        optimizer='adam',
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )

    try:
        poke_model.fit(
            train_images,
            validation_data=validation_images,
            epochs=5
        )
    except:
        print("\nwtf went wrong")

    poke_model.evaluate(validation_images, verbose=2)





def main():
    print("hello world")

    classify151()



main()