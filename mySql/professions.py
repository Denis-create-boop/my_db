# импортируем класс для работы с таблицой в бд
from my_test_db_professions import Professions

# создаём класс для работы с профессиями
class Profession:

    def __init__(self):
        self.obj_prof = Professions()

    # функция для добавления новой профессии в бд
    def add_prof(self):
        profession = input("Введите профессию: ")
        # вызываем метод класса для записи профессии в бд
        self.obj_prof.write(profession)
        input("Профессия успешно добавлена")
        return

    # функция для удаления профессии из бд
    def del_prof(self) -> None:
        profession = input("Введите профессию которую хотите удалить: ")
        # вызываем метод класса для удаления профессии
        print(self.obj_prof.del_prof(profession))
        input("Профессия удалена")
        return

    # функция для переименования названия профессии
    def change_prof_name(self):
        # считываем все id из бд
        all_id = self.obj_prof.all_id()
        ls_id = []
        # записываем все id в список
        for row in all_id:
            ls_id.append(int(row[0]))

        print("Введите id профессии которую хотите изменить")
        # принимаем id от пользователя
        id = int(input())
        # проверяем если id такой есть в бд то меняем название
        if id in ls_id:
            profession = input("Введите новое название: ")
            print(self.obj_prof.change_name(id, profession))
        # если id  в бд нет то говорим об ошибке и вызываем функцию повторно
        else:
            print("Введен неверный id")
            self.change_prof_name()
        input()
        return

    # главная функция для работы с профессиями
    def prof(self):
        # бесконечный цикл для взаимодействия с пользователем
        while True:
            # словарь комманд
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
            # проверяем что ввел пользователь и вызываем определенную функцию
            # если команда назат то выходим из главной функции в то место где её вызвали
            if int(answer) == 6 or answer.lower() == "назат":
                return
            # если команда выход то возвращаемся и завершаем работу
            elif int(answer) == 7 or answer.lower() == "выход":
                return 7
            # выводим все поля из таблицы профессий
            elif int(answer) == 5 or answer.lower() == "посмотреть все данные таблицы":
                flag = True
                for row in self.obj_prof.show_all():
                    print(
                        f"id: {row[0]},\nпрофессия: {row[1]},\nколичество сотрудников: {row[2]}"
                    )
                    print("--------------------------")
                    print()
                    flag = False
                if flag:
                    print("База данных пуста")
                input()
                return
            
            # выводим все имеющиеся профессии в бд
            elif int(answer) == 2 or answer.lower() == "посмотреть все профессии":
                flag = True
                for row in self.obj_prof.show_profession():
                    print(row)
                    flag = False
                if flag:
                    print("В базе пока нет профессий")
                input()
                return
            # для остальных комманд вызываем функцию закрепленную за определенным ключем
            else:
                doit[answer.lower()]()
