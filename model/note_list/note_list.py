import datetime

from model.note.note import Note


class NoteList(Note):
    note_list = list()

    def add_note(head, body, creation_date):
        note = Note(len(NoteList.note_list) + 1, head, body, creation_date, creation_date)
        NoteList.note_list.append(note)

    def edit_note(id_note, body_note, last_edit_date=datetime.datetime.now()):
        editable_note = NoteList.note_list[id_note]
        editable_note.set_body(body_note)
        editable_note.set_last_edit_date(last_edit_date)
        NoteList.note_list[id_note] = editable_note

    def print_note_list():
        txt = ''
        for i in range(len(NoteList.note_list)):
            txt += str(NoteList.note_list[i].get_id()) + '. ' + NoteList.note_list[i].get_head() + '\n'
        print(txt)

