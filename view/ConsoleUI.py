from presenter.Presenter import Presenter


class ConsoleUI:
    def __init__(self):
        self.presenter = Presenter


    def check_number(n):
        while n < 1 or n > 9:
            n = int(input("Ошибка. Такой комманды нет!\n"
                          "Выберите функцию:\n"
                          "1. Добавить заметку. \n"
                          "2. Удалить заметку. \n"
                          "3. Изменить заметку. \n"
                          "4. Вывести заметку на экран.\n"
                          "5. Вывести список заметок. \n"
                          "6. Сохранить список заметок. \n"
                          "7. Загрузить список заметок. \n"
                          "8. Выход \n"
                          "Введите номер команды: "))
        return n


    def start_menu():
        command = None
        print("Доброго времени суток!\n")
        while command != 9:
            command = int(input("Выберите функцию:\n"
                                "1. Добавить заметку. \n"
                                "2. Удалить заметку. \n"
                                "3. Изменить заметку. \n"
                                "4. Вывести заметку на экран.\n"
                                "5. Вывести список заметок. \n"
                                "6. Вывести все заметки на экран. \n"
                                "7. Сохранить список заметок. \n"
                                "8. Загрузить список заметок. \n"
                                "9. Выход \n"
                                "Введите номер команды: "))
            command = ConsoleUI.check_number(command)
            if command == 1:
                note_head = input("Введите заголовок заметки:")
                note_body = input("Введите текст заметки:")
                Presenter.add_note(note_head, note_body)
            if command == 2:
                note_id = int(input("Введите номер заметки:"))
                Presenter.del_note(note_id)
            if command == 3:
                note_id = int(input("Введите номер заметки:"))
                note_head = input("Введите заголовок заметки:")
                note_body = input("Введите текст заметки:")
                Presenter.edit_note(note_id, note_head, note_body)
            if command == 4:
                note_id = int(input("Введите номер заметки:"))
                print(Presenter.print_note(note_id))
            if command == 5:
                print(Presenter.print_note_body())
            if command == 6:
                print(Presenter.print_note_list())
            if command == 7:
                Presenter.save_note_list()
            if command == 8:
                Presenter.load_note_list()

