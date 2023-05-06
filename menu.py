from noteEx import NotesApp


class Menu:
    def __init__(self):
        self.notes_app = NotesApp("notes.csv")

    def show(self):
        while True:
            print("Выберите опцию:")
            print("1. Добавить заметку")
            print("2. Показать все заметки")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Поиск заметки")
            print("6. Выход")
            choice = input("Введите свой выбор (1-5): ")
            if choice == "1":
                title = input("Введите название заметки: ")
                body = input("Введите текст заметки: ")
                self.notes_app.add_note(title, body)
            elif choice == "2":
                self.notes_app.read_notes()
            elif choice == "3":
                id_note = input("Введите id заметки: ")
                title = input("Введите название заметки: ")
                body = input("Введите текст заметки: ")
                self.notes_app.edit_note_by_id(int(id_note), title, body)
            elif choice == "4":
                id_note = input("Введите id заметки: ")
                self.notes_app.delete_note_by_id(int(id_note))
            elif choice == "5":
                id_note = input("Введите id заметки: ")
                print(self.notes_app.find_note_by_id(int(id_note)))
            elif choice == "6":
                break
            else:
                print("Неверный выбор. Введите число от 1 до 6.")