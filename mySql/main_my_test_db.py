
from my_test_db_worckers import Worckers
from professions import Profession

obj_worck = Worckers()


obj_prof = Profession()


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
            step = obj_prof.prof()
            if step == 7:
                break

        elif int(answer) == 2 or answer.lower() == "работа с работниками":
            worcker()


if __name__ == "__main__":
    main()
