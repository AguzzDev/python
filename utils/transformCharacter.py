import unicodedata
from utils.dictionaries import charDictionary


def transform_characters(text):

    text = unicodedata.normalize("NFD", text)

    text = ''.join(
        char for char in text
        if unicodedata.category(char) != 'Mn'
    )

    # Reemplaza caracteres especiales según el mapeo definido
    text = ''.join(charDictionary.get(char, char) for char in text)

    return text
