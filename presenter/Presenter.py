from model.note_list.Note_list import NoteList


class Presenter:

    def __init__(self, view):
        self.view = view
        self.model = NoteList

    def add_note(note_head, note_body):
        NoteList.add_note(note_head, note_body)

    def del_note(note_id):
        NoteList.del_note(note_id)

    def edit_note(note_id, note_head, note_body):
        NoteList.edit_note(note_id, note_head, note_body)

    def print_note(note_id):
        return NoteList.print_note(note_id)

    def print_note_list():
        return NoteList.print_note_list()

    def print_note_body():
        return NoteList.print_note_body()

    def save_note_list():
        NoteList.save_note_list()

    def load_note_list():
        NoteList.load_note_list()