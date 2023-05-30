from keras.models import load_model
import numpy as np

autoencoder = load_model("d-ae-5-linear.h5")
training_file = open('training-eonly.csv', 'r')

training_data = []

for line in training_file.readlines():
    for data in line.split(","):
        if data != "\n" or data != "":
            try:
                training_data.append(float(data))
            except ValueError:
                pass

training_data = np.reshape(training_data, (-1, 12, 1))

print(len(training_data))
array = autoencoder.predict(training_data)
array = array.astype('float32')

prediction_file = open('prediction-2.csv', 'w')

# for i in array:
#     print(i[4], " | ", i[5])

array = np.reshape(array, (-1, 6, 1))
for frame in array:
    for data in frame:
        for float in data:
            prediction_file.write(str(float) + ",")
    prediction_file.write("\n")

