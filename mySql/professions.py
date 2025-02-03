from my_test_db_professions import Professions


class Profession:

    def __init__(self):
        self.obj_prof = Professions()

    def add_prof(self):
        print("Введите профессию")
        profession = input()
        self.obj_prof.write(profession)
        print("Профессия успешно добавлена")
        input()
        return

    def del_prof(self) -> None:
        print("Введите профессию которую хотите удалить")
        profession = input()
        print(self.obj_prof.del_prof(profession))
        input()
        return

    def change_prof_name(self):
        print("Введите id профессии которую хотите изменить")
        id = int(input())
        print("Введите новое название")
        profession = input()
        print(self.obj_prof.change_name(id, profession))
        input()
        return

    # function for worcking with professions
    def prof(self):
        while True:
            doit = {
                "1": self.add_prof,
                "3": self.del_prof,
                "4": self.change_prof_name,
                "добавить новую профессию": self.add_prof,
                "удалить профессиию": self.del_prof,
                "изменить название профессии": self.change_prof_name,
            }
            print(
                f"""Вы выбрали работу с профессиями, выберите команду:
                      1 - Добавить новую профессию
                      2 - Посмотреть все профессии
                      3 - Удалить профессиию
                      4 - Изменить название профессии
                      5 - Посмотреть все данные таблицы
                      6 - Назат
                      7 - Выход"""
            )
            answer = input()
            if int(answer) == 6 or answer.lower() == "назат":
                return
            elif int(answer) == 7 or answer.lower() == "выход":
                return 7
            elif int(answer) == 5 or answer.lower() == "посмотреть все данные таблицы":
                for row in self.obj_prof.show_all():
                    print(
                        f"id: {row[0]},\nпрофессия: {row[1]},\nколичество сотрудников: {row[2]}"
                    )
                    print("--------------------------")
                    print()
                input()
                return
            elif int(answer) == 2 or answer.lower() == "посмотреть все профессии":
                for row in self.obj_prof.show_profession():
                    print(row)
                input()
                return
            else:
                doit[answer.lower()]()
