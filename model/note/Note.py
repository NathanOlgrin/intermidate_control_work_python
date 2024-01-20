import datetime


class Note:
    def __init__(self, id=0, head="", body="", creation_date=datetime.datetime.now(),
                 last_edit_date=datetime.datetime.now()):
        self._id = id
        self._head = head
        self._body = body
        self._creation_date = creation_date
        self._last_edit_date = last_edit_date

    # Ceттеры

    def set_id(self, number):
        self._id = number

    def set_head(self, heading):
        self._head = heading

    def set_body(self, body_note):
        self._body = body_note

    def set_creation_date(self, creation_date_note):
        self._creation_date = creation_date_note

    def set_last_edit_date(self, last_edit_date_note):
        self._last_edit_date = last_edit_date_note

    # Геттеры

    def get_id(self):
        return self._id

    def get_head(self):
        return self._head

    def get_body(self):
        return self._body

    def get_creation_date(self):
        return self._creation_date

    def get_last_edit_date(self):
        return self._last_edit_date

    def get_note(self):
        txt = str(self._id) + '. ' + self._head + '. ' + self._body
        return txt

    def get_note_body(self):
        txt = str(self._id) + '. ' + self._head
        return txt

    def get_note_to_file(self):
        txt = (str(self._id) + '. ' + self._head + '. ' + self._body + '. creature: ' + str(self._creation_date) +
               '. last_edit: ' + str(self._last_edit_date) + '\n')
        return txt