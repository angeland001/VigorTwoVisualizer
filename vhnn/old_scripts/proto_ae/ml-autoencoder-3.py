# based on de-noising auto-encoder found in Keras

from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Dropout
from keras.layers import Conv1D, MaxPooling1D, UpSampling1D, Lambda
from keras.models import Model
from random import randint
from keras.optimizers import Adam
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard

training_file = open('training-eonly.csv', 'r')
target_file = open('target-eonly.csv')
training_data = []
target_data = []

for line in training_file.readlines():
    for data in line.split(","):
        if data != "\n" or data != "":
            try:
                training_data.append(float(data))
            except ValueError:
                pass


for line in target_file.readlines():
    for data in line.split(","):
        if data != "\n" or data != "":
            try:
                target_data.append(float(data))
            except ValueError:
                pass



# Setting both as target data just for testing purposes to get past errors
x_train = np.reshape(training_data, (-1, 12, 1))  # adapt this if using `channels_first` image data format
x_test = np.reshape(target_data, (-1, 6, 1))  # adapt this if using `channels_first` image data format

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')



input_img = Input(shape=(12, 1))  # adapt this if using `channels_first` image data format

x = Conv1D(32, 3, activation='relu', padding='same')(input_img)
x = Dropout(0.3)(x)
x = MaxPooling1D(2, padding='same')(x)
x = Conv1D(32, 3, activation='relu', padding='same')(x)
encoded = MaxPooling1D(2, padding='same')(x)

x = Conv1D(32, 3, activation='relu', padding='same')(encoded)
x = Dropout(0.3)(x)
x = UpSampling1D(2)(x)
# x = Conv1D(32, 3, activation='relu', padding='same')(x)
# x = UpSampling1D(1)(x)
decoded = Conv1D(1, 3, activation='relu', padding='same')(x)

autoencoder = Model(input_img, decoded)
autoencoder.compile("adam", loss='mse')

autoencoder.fit(x_train, x_test,
                epochs=5000,
                batch_size=32,
                shuffle=True,
                validation_data=(x_train, x_test),
                callbacks=[TensorBoard(log_dir='/tmp/tb', histogram_freq=0, write_graph=False)])

autoencoder.save("d-ae-5-linear.h5")