import json


def save_note_list(BD):
    fname= "model\\NoteList files\\Note_One.json"
    with open(fname, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(BD, indent=2, ensure_ascii=False))  # преобразовываем словарь data  в unicode-строку
    print('БД успешно сохранена')
