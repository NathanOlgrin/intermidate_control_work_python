import datetime

from model.note_list.note_list import NoteList

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        c = NoteList
        #c.add_note("Заметка-1", "олалала", datetime.datetime.now())
        #c.add_note("Заметка-2", "олалалалла", datetime.datetime.now())


        #c.save_note_list()
        c.load_note_list()
        c.print_note_list()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
