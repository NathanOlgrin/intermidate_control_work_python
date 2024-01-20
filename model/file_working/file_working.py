import json


def save_notelist(NL):
    fname= "model\\NoteList files\\Note_One.json"
    with open(fname, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(NL, indent=2, ensure_ascii=False))  # преобразовываем словарь data  в unicode-строку

def load():
    # загрузить из JSON
    fname = 'model\\NoteList files\\Note_One.json'  # открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        NL = json.load(fh)  # загружаем из файла данные в словарь data
    open(fname, 'w').close()
    return NL