import json

def convert(read, write):
    array = open(read + '.json')
    save_file = open(write + '.csv', 'w')
    userdata = json.load(array)

    for frame in range(0, 5000):
        for joint in "45":
            save_file.write(
                str(userdata["ModelQuaternionList"][frame]['ChildQuaternionList'][int(joint)]['euler']['x'])
                )
            save_file.write(",")
            save_file.write(
                str(userdata["ModelQuaternionList"][frame]['ChildQuaternionList'][int(joint)]['euler']['y'])
                )
            save_file.write(",")
            save_file.write(
                str(userdata["ModelQuaternionList"][frame]['ChildQuaternionList'][int(joint)]['euler']['z'])
                )
            save_file.write(",")
        save_file.write("\n")
    save_file.close()

convert('JSONs/ae-naturalwalk-1', 'target-eonly')