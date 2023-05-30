from keras.models import load_model
import numpy as np
import pickle
import socket

testing_file = open('training.csv', 'r')
# result_file = open('result.csv', 'w')
testing_data = []
target_data = []

for line in testing_file.readlines():
    for data in line.split(","):
        if data != "\n" or data != "":
            try:
                testing_data.append(float(data))
            except ValueError:
                pass

testing_data = np.reshape(testing_data, (-1, 15))
print(testing_file)

filename = 'finalized_model_1.sav'
loaded_model = load_model('d-ae-1.h5')


def predict_stream(data):
    '''
    :param data:
    :type data: bytearray
    :return:
    :rtype: str
    '''

    np_data = []
    prediction_string = ""
    prediction = None
    if data is not None:
        data_list = data.decode().split(',')
        try:

            for data in data_list:
                np_data.append(float(data))
            np_data = np.reshape(np_data, (9, -1))
            # prediction = loaded_model.predict(np_data)
            #
            # if prediction is not None:
            #     for data in prediction:
            #         print(data)
            #         prediction_string += str(data) + ","
        except ValueError:
            pass
    return prediction_string[:-1] if prediction_string is not "" else ""


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(("localhost", 3000))
connection.listen(5)
while True:
    print("Waiting for conn ")
    conn, addr = connection.accept()
    print("got conn on ", conn, addr)
    while True:
        data = conn.recv(1024)
        # print(data)
        if data:
            predicted_data = predict_stream(data)
            if predicted_data is not "":
                conn.send(predicted_data.encode())
                print(predicted_data)
            else:
                conn.send(data)

            print("am sending", data.decode())