import datetime

from model.note.Note import Note
from model.file_working import file_working


class NoteList(Note):
    note_list = list()
    NL = []

    def __init__(self):
        self.note_list = self
        self.NL = self

    def add_note(head, body, creation_date=datetime.datetime.now().isoformat()):
        note = Note(len(NoteList.note_list) + 1, head, body, creation_date, creation_date)
        NoteList.note_list.append(note)

    def edit_note(id_note, head_note, body_note, last_edit_date=datetime.datetime.now().isoformat()):
        editable_note = NoteList.note_list[id_note]
        editable_note.set_head(head_note)
        editable_note.set_body(body_note)
        editable_note.set_last_edit_date(last_edit_date)
        NoteList.note_list[id_note] = editable_note

    def print_note_body():
        txt = ''
        for i in range(len(NoteList.note_list)):
            txt += str(NoteList.note_list[i].get_id()) + '. ' + NoteList.note_list[i].get_head() + '\n'
        return txt

    def print_note_list():
        txt = ''
        for i in range(len(NoteList.note_list)):
            txt += str(NoteList.note_list[i].get_id()) + '. ' + NoteList.note_list[i].get_head() + '. ' + \
                   NoteList.note_list[i].get_body() + '\n'
        return txt

    def print_note(number):
        txt = str(NoteList.note_list[number].get_id()) + '. ' + NoteList.note_list[number].get_head() + '. ' + \
              NoteList.note_list[number].get_body() + '\n'
        return txt

    def del_note(id):
        NoteList.note_list.pop(id-1)

    def save_note_list():
        for i in range(len(NoteList.note_list)):
            NoteList.NL.append(
                {'note number': NoteList.note_list[i].get_id(), 'note head': NoteList.note_list[i].get_head(),
                 'note body': NoteList.note_list[i].get_body(),
                 'creation date': NoteList.note_list[i].get_creation_date(),
                 'last edit date': NoteList.note_list[i].get_last_edit_date()})
        file_working.save_notelist(NoteList.NL)

    def load_note_list():
        NL = file_working.load()
        for i in NL:
            note = Note(i['note number'], i['note head'], i['note body'], i['creation date'], i['last edit date'])
            NoteList.note_list.append(note)