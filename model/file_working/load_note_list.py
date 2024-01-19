import json


def load():
    # загрузить из JSON
    fname = 'model\\NoteList files\\Note_One.json'  # открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        NL = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успешно загружена')
    return NL
