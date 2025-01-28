from my_test_db_professions import Professions
from my_test_db_worckers import Worckers

obj_prof = Professions()
obj_worck = Worckers()


def add_prof():
    print("Введите профессию")
    profession = input()
    obj_prof.write(profession)
    print("Профессия успешно добавлена")
    input()
    return


def del_prof() -> None:
    print("Введите профессию которую хотите удалить")
    profession = input()
    print(obj_prof.del_prof(profession))
    input()
    return


def change_prof_name():
    print("Введите id профессии которую хотите изменить")
    id = int(input())
    print("Введите новое название")
    profession = input()
    print(obj_prof.change_name(id, profession))
    input()
    return


def prof():
    while True:
        doit = {
            "1": add_prof,
            "3": del_prof,
            "4": change_prof_name,
            "добавить новую профессию": add_prof,
            "удалить профессиию": del_prof,
            "изменить название профессии": change_prof_name,
        }
        print(f"""Вы выбрали работу с профессиями, выберите команду:
                  1 - Добавить новую профессию
                  2 - Посмотреть все профессии
                  3 - Удалить профессиию
                  4 - Изменить название профессии
                  5 - Посмотреть все данные таблицы
                  6 - Назат
                  7 - Выход""")
        answer = input()
        if int(answer) == 6 or answer.lower() == "назат":
            return
        elif int(answer) == 7 or answer.lower() == "выход":
            return 7
        elif int(answer) == 5 or answer.lower() == "посмотреть все данные таблицы":
            for row in obj_prof.show_all():
                print(row)
            input()
            return
        elif int(answer) == 2 or answer.lower() == "посмотреть все профессии":
            for row in obj_prof.show_profession():
                print(row)
            input()
            return
        else:
            doit[answer.lower()]()

def worcker():
    pass

def main():
    while True:
        print(f"""Здравствуйте, добро пожаловать в бот помошник с базой данных
              Выберите команду:
              1 - Работа с профессиями
              2 - Работа с работниками""")
        print("Введите номер команды или её название")
        
        answer = input()
        if int(answer) == 1 or answer.lower() == "работа с профессиями":
            step = prof()
            if step == 7:
                break

        elif int(answer) == 2 or answer.lower() == "работа с работниками":
            worcker()


if __name__ == "__main__":
    main()
