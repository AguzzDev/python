import os
import random
from utils.dict import file_type_dict


def generate_files(dir, num=100):
    if not os.path.exists(dir):
        os.mkdir(dir)

    os.chdir(dir)

    for i in range(0, num):
        extension = random.choice(list(file_type_dict.keys()))

        file_name = f"file_{i}.{extension}"

        with open(file_name, "w", encoding="utf-8"):
            continue
    
    os.chdir("../")
