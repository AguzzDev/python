def get_file_extension(file):
    if "." in file:
        return file.split(".")[-1].lower()
    return None
