import tensorflow as tf

import pathlib
import IPython.display as display
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = pathlib.Path('./scaled')
test_dir = pathlib.Path('./test')

image_count = len(list(data_dir.glob('*/*.png')))

CLASS_NAMES = np.array([item.name for item in data_dir.glob('*') if item.name != ".DS_Store"])

print(image_count, CLASS_NAMES)

image_generator = tf.keras.preprocessing.image.ImageDataGenerator()

image_res = (300, 140)

BATCH_SIZE = 5
IMG_HEIGHT = 140
IMG_WIDTH = 300
STEPS_PER_EPOCH = np.ceil(image_count/BATCH_SIZE)

train_data_gen = image_generator.flow_from_directory(directory=str(data_dir),
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                     classes = list(CLASS_NAMES), class_mode="sparse")

test_it_gen = image_generator.flow_from_directory(directory=str(test_dir),
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                     classes = list(CLASS_NAMES), class_mode="sparse")

model = tf.keras.models.Sequential([
	tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
	tf.keras.layers.MaxPooling2D(2, 2),
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(256, activation=tf.nn.relu),
	tf.keras.layers.Dense(3, activation=tf.nn.softmax)
])

print(model.summary())
model.compile(optimizer='adam',
							loss='sparse_categorical_crossentropy',
							metrics=['accuracy'])
model.fit(train_data_gen, epochs=5)

#
#def show_batch(image_batch, label_batch):
#	plt.figure(figsize=(10,10))
#	for n in range(3):
#			ax = plt.subplot(5,5,n+1)
#			plt.imshow(image_batch[n])
#			plt.title(CLASS_NAMES[label_batch[n]==1][0].title())
#			plt.axis('off')
#
#image_batch, label_batch = next(train_data_gen)
#
#epochs = 50
#

#x_train, x_test = x_train.reshape(60000, 28, 28, 1), x_test.reshape(10000, 28, 28, 1)
#x_train, x_test = x_train / 255.0, x_test / 255.0
#

#
#print(model.summary())
#
#model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
#model.fit(x_train, y_train, epochs=2)

