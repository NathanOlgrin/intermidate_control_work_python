import datetime

from model.note.note import Note
from model.file_working.save_note_list import save_note_list
from model.file_working.load_note_list import load


class NoteList(Note):
    note_list = list()
    NL = []
    def add_note(head, body, creation_date):
        note = Note(len(NoteList.note_list) + 1, head, body, creation_date, creation_date)
        NoteList.note_list.append(note)

    def edit_note(id_note, body_note, last_edit_date=datetime.datetime.now()):
        editable_note = NoteList.note_list[id_note]
        editable_note.set_body(body_note)
        editable_note.set_last_edit_date(last_edit_date)
        NoteList.note_list[id_note] = editable_note

    def print_note_body():
        txt = ''
        for i in range(len(NoteList.note_list)):
            txt += str(NoteList.note_list[i].get_id()) + '. ' + NoteList.note_list[i].get_head() + '\n'
        print(txt)

    def print_note_list():
        txt = ''
        for i in range(len(NoteList.note_list)):
            txt += str(NoteList.note_list[i].get_id()) + '. ' + NoteList.note_list[i].get_head() + '. '+ NoteList.note_list[i].get_body()+'\n'
        print(txt)

    def print_note(number):
        txt = str(NoteList.note_list[number].get_id()) + '. ' + NoteList.note_list[number].get_head() + '. '+ NoteList.note_list[number].get_body()+'\n'
        print(txt)

    def save_note_list():
        for i in range(len(NoteList.note_list)):
            print(NoteList.note_list[i].get_body())
            NoteList.NL.append({'note number': NoteList.note_list[i].get_id(), 'note head': NoteList.note_list[i].get_head(),
                                'note body': NoteList.note_list[i].get_body(), 'creation date': NoteList.note_list[i].get_creation_date().isoformat(), 'last edit date': NoteList.note_list[i].get_last_edit_date().isoformat()})
        save_note_list(NoteList.NL)

    def load_note_list():
        NL = load()
        for i in NL:
            note = Note(i['note number'], i['note head'], i['note body'], i['creation date'], i['last edit date'])
            NoteList.note_list.append(note)