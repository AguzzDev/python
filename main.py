import os
import time
import argparse
from utils.file_extension import get_file_extension
from utils.dict import file_type_dict
from utils.check_folder_exist import check_folder_exist
from utils.generate_files import generate_files

parser = argparse.ArgumentParser(
    description="Organize your files or run a test to generate files")
parser.add_argument("--test", action="store_true", help="Generate test files")
args = parser.parse_args()


def main():
    if args.test:
        generate_files("files")

    start_time = time.time()

    check_folder_exist("files")
    os.chdir("files")

    files = [file for file in os.listdir() if os.path.isfile(file)]

    os.chdir("../")
    check_folder_exist("organized")
    os.chdir("organized")

    rest = 0
    for file in files:
        extension = get_file_extension(file)
        folder = file_type_dict.get(extension)

        if folder:
            if not os.path.exists(folder):
                os.mkdir(folder)

            source = os.path.join("../files", file)
            destination = os.path.join(folder, file)
            os.rename(source, destination)
        else:
            rest += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print(f"Se organizaron {len(files) -
          rest} archivos en {total_time} segundos")


if __name__ == "__main__":
    main()
