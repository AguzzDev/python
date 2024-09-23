import os


def check_folder_exist(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
