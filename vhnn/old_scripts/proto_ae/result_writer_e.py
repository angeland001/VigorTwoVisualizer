import numpy as np

training_file = open('training-eonly.csv', 'r')
prediction_file = open('prediction-2.csv', 'r')

training_data = []
prediction_data = []

for line in training_file.readlines():
    for data in line.split(","):
        if data != "\n" or data != "":
            try:
                training_data.append(float(data))
            except ValueError:
                pass

for line in prediction_file.readlines():
    for data in line.split(","):
        if data != "\n" or data != "":
            try:
                prediction_data.append(float(data))
            except ValueError:
                pass

training_data = np.reshape(training_data, (4996, -1))
prediction_data = np.reshape(prediction_data, (4996, -1))

result_file = open('result.csv', 'w')

for frame in range(4996):
    tdata = training_data[frame]
    pdata = prediction_data[frame]
    for data in tdata:
        result_file.write(str(data) + ",")
    for data in pdata:
        result_file.write(str(data) + ",")
    result_file.write("\n")
