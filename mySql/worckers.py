# импортируем класс таблицы работников
from my_test_db_worckers import Worckers

# класс для работы с таблицой работников
class Worcker:

    def __init__(
        self,
        name=None,
        first_name=None,
        address=None,
        phone=None,
        profession=None,
        status=None,
    ):
        self.id = 0
        self.name = name
        self.first_name = first_name
        self.address = address
        self.phone = phone
        self.profession = profession
        self.status = status

    # функция для добавления работников
    def add_worcker(self):
        # вспомогательная функция для сбора данных о работнике
        def asc(self):
            print("Введите имя работника")
            name = input()
            self.name = name
            print()
            print("Введите фамилию работника")
            first_name = input()
            self.first_name = first_name
            print()
            print("Введите адресс работника (необязательно)")
            address = input()
            if address:
                self.address = address
            print()
            print("Введите телефон работника (необязательно)")
            phone = input()
            if phone:
                self.phone = phone
            print()
            print("Введите профессию работника (необязательно)")
            profession = input()
            if profession:
                self.profession = profession
                from my_test_db_professions import Professions

                obj = Professions()
                prof = obj.show_profession()
                if profession in prof:
                    amount = obj.get_amount(profession)
                    amount = int(amount[0])
                    amount += 1
                    obj.change_amount(amount, profession)
                else:
                    obj.write(profession, 1)

            print()
            print("Введите статус работника (необязательно)")
            status = input()
            if status:
                self.status = status

        asc(self)
        # поключаемся к бд и записуем нового работника
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        obj_worcker.add_worcker(
            address=self.address,
            phone=self.phone,
            profession=self.profession,
            status=self.status,
        )
        print(
            f"Работник:\nИмя: {self.name}\nФамилия: {self.first_name}\nУспешно добавлен"
        )
        print()

    #
    def show_all(self):
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        result = obj_worcker.show_all()
        for row in result:
            print(row)
        print()

    # функция для просмотра работников которые есть в бд
    def show_worckers(self):
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        result = obj_worcker.show_worckers()
        ls = ["имя: ", "фамилия: "]
        for row in result:
            print(ls[0], str(row[0]) + "\n" + str(ls[1]), row[1])
        print()

    # функция для изменения статуса работника
    def change_status(self):
        ans = self.check()
        if ans == 0:
            return

        else:
            status = input("Введите новый статус: ")
            obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
            obj_worcker.change_worcker_status(status)
            print("Статус успешно изменен")
            print()

    # функция для изменения профессии
    def change_prof(self):
        ans = self.check()
        if ans == 0:
            return
        else:
            print("Введите новую профессию")
            profession = input()
            obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
            obj_worcker.change_worcker_profession(profession)
            print("Профессия успешно изменена")
            print()

    # функция для получения профессии работника
    def get_prof(self):
        obj_worcker = Worckers(id=self.id, name=self.name, first_name=self.first_name)
        return obj_worcker.get_prof()

    # функция для удаления работника из бд
    def del_worcker(self):
        # подключаемся к базе профессий
        from my_test_db_professions import Professions

        ans = self.check()
        if ans == 0:
            return
        else:
            # удаляем работника из бд работников и уменьшаем количество сотрудников в бд профессии
            obj_worcker = Worckers(id=self.id, name=self.name, first_name=self.first_name)
            obj_prof = Professions()
            prof = self.get_prof()
            amounts = obj_prof.get_amount(prof[0])
            if amounts:
                amount = int(amounts[0]) - 1
            else:
                amount = 0
            obj_prof.change_amount(amount, prof[0])
            obj_worcker.del_worcker()
            print("Работник удален")
            print()

    # функция для изменения имени работника
    def change_name(self):
        ans = self.check()
        if ans == 0:
            return
        else:
            print("Введите новое имя")
            name = input()
            obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
            obj_worcker.change_worcker_name(name)
            print("Имя успешно изменено")
            print()

    # функция для изменения фамилии работника
    def change_first_name(self):
        ans = self.check()
        if ans == 0:
            return
        else:
            print("Введите новую фамилию")
            first_name = input()
            obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
            obj_worcker.change_worcker_first_name(first_name)
            print("Фамилия успешно изменена")
            print()

    # функция для изменения адреса работника
    def change_address(self):
        ans = self.check()
        if ans == 0:
            return
        else:
            print("Введите новый адресс работника")
            address = input()
            obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
            obj_worcker.change_worcker_address(address)
            print("Адресс изменен")
            print()

    # функция для удаления адреса работника
    def del_address(self):
        ans = self.check()
        if ans == 0:
            return
        else:
            obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
            obj_worcker.del_worcker_address()
            print("Адресс успешно удален")
            print()

    # функция для добавления телефона работнику
    def add_phone(self):
        ans = self.check()
        if ans == 0:
            return
        else:
            print("Введите номер телефона")
            while True:
                phones = input()
                try:
                    phone = int(phones)
                    break
                except:
                    print("Неправильный номер, пожалуйста введите правильный номер")
            obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
            obj_worcker.change_worcker_phone(phone)
            print("Номер изменен")
            print()

    # функция для удаления телефона работника
    def del_phone(self):
        ans = self.check()
        if ans == 0:
            return
        else:
            obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
            obj_worcker.del_worcker_phone()
            print("Номер телефона успешно удалён")
            print()

    # функция для проверки данных перед каким либо действием
    def check(self):
        obj = Worckers()
        obj.create_table()
        ls_id = []
        ls_names = []
        all_id = obj.get_id()
        for row in all_id:
            ls_id.append(int(row[0]))
        all_name = obj.show_worckers()
        for row in all_name:
            ls_names.append([row[0], row[1]])

        print("Ведите id работника или его имя и фамилию сначала имя затем фамилию, для возврата введите 0")
        ans = input().split()
        if ans[0] == '0':
            return 0

        elif len(ans) > 1:
            name = ans[-2]
            first_name = ans[-1]
            if [name, first_name] in ls_names:
                self.name = ans[-2]
                self.first_name = ans[-1]
            else:
                print("Такого работника нет в базе данных, пожалуйста проверьте имя и фамилию")
                print()
                self.check()

        else:
            id = int(ans[0])
            if id in ls_id:
                self.id = id
            else:
                print("Такого id нет в базе данных")
                print()
                self.check()

    # главная функция для работы с работниками
    def work(self):
        while True:
            doit = {
                "1": self.add_worcker,
                "3": self.del_worcker,
                "4": self.change_prof,
                "5": self.change_name,
                "6": self.change_first_name,
                "7": self.change_address,
                "8": self.del_address,
                "9": self.add_phone,
                "10": self.del_phone,
                "11": self.change_status,
                "Добавить нового работника": self.add_worcker,
                "Удалить работника": self.del_worcker,
                "Изменить название профессии работника": self.change_prof,
                "Изменить имя работника": self.change_name,
                "Изменить фамилию работника": self.change_first_name,
                "Добавить или изменить адресс работника": self.change_address,
                "Удалить адресс работника": self.del_address,
                "Добавить или изменить телефон работника": self.add_phone,
                "Удалить телефон работника": self.del_phone,
                "Изменить статус работника": self.change_status,
            }
            print(
                f"""Вы выбрали работу с работниками, выберите команду:
                      1 - Добавить нового работника
                      2 - Посмотреть всех работников
                      3 - Удалить работника
                      4 - Изменить название профессии работника
                      5 - Изменить имя работника
                      6 - Изменить фамилию работника
                      7 - Добавить или изменить адресс работника
                      8 - Удалить адресс работника
                      9 - Добавить или изменить телефон работника
                      10 - Удалить телефон работника
                      11 - Изменить статус работника
                      12 - Посмотреть все данные таблицы
                      13 - Назат
                      14 - Выход"""
            )
            answer = input()
            if int(answer) == 13 or answer.lower() == "назат":
                return
            elif int(answer) == 14 or answer.lower() == "выход":
                return 7
            elif int(answer) == 12 or answer.lower() == "посмотреть все данные таблицы":
                obj_worcker = Worckers(
                    self.id, name=self.name, first_name=self.first_name
                )
                wrks = obj_worcker.show_all()
                flag = True
                for row in wrks:
                    print(f"id: {row[0]},\nимя: {row[1]},\nфамилия: {row[2]}\nадресс: {row[3]},\nтелефон: {row[4]},\nпрофессия: {row[5]},\nстатус: {row[6]}")
                    print("--------------------------")
                    flag = False
                    print()
                if flag:
                    print("В базе пока нет ниодного работника")
                input()
                return
            elif int(answer) == 2 or answer.lower() == "посмотреть всех работников":
                self.show_worckers()
                input()
                return
            else:
                doit[answer.lower()]()
