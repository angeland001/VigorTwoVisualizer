import numpy as np

prediction_file = open('prediction-2.csv', 'r')
target_file = open('target-eonly.csv')
prediction_data = []
target_data = []

for line in prediction_file.readlines():
    for data in line.split(","):
        if data != "\n" or data != "":
            try:
                prediction_data.append(float(data))
            except ValueError:
                pass


for line in target_file.readlines():
    for data in line.split(","):
        if data != "\n" or data != "":
            try:
                target_data.append(float(data))
            except ValueError:
                pass


prediction_data = np.reshape(prediction_data, (-1, 6, 1))
target_data = np.reshape(target_data, (-1, 6, 1))

result = np.subtract(prediction_data, target_data)
result = result.astype('int')
print(result)