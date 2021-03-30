import socket
import pickle
import os
import yaml

file_path = "Logs.yaml"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("34.77.60.185", 8080))
        
    info = input("What do you want information about(weather, time or airquality): ")
    s.send(pickle.dumps(info))

    return_info = s.recv(1024)
    return_info = pickle.loads(pickle.loads(return_info))

    s.close()

    print("Here is the information:", "\n", return_info)

    comand_dict = {info : return_info}

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            yaml.dump(comand_dict, file)
    else:
        with open(file_path, "w") as file:
            yaml.dump(comand_dict, file)

    check = input("Do you wish to run the program angain?(y/n): ")
    if check == 'n':
        break