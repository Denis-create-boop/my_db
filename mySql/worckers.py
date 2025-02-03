from my_test_db_worckers import Worckers


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

    def add_worcker(self):
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

    def show_all(self):
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        result = obj_worcker.show_all()
        for row in result:
            print(row)

    def show_worckers(self):
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        result = obj_worcker.show_worckers()
        ls = ["имя: ", "фамилия: "]
        for row in result:
            print(ls[0], str(row[0]) + "\n" + str(ls[1]), row[1])

    def change_prof(self):
        self.check()
        print("Введите новую профессию")
        profession = input()
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        obj_worcker.change_worcker_profession(profession)
        print("Профессия успешно изменена")

    def get_prof(self):
        obj_worcker = Worckers(id=self.id, name=self.name, first_name=self.first_name)
        return obj_worcker.get_prof()

    def del_worcker(self):
        from my_test_db_professions import Professions

        self.check()
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

    def change_name(self):
        self.check()
        print("Введите новое имя")
        name = input()
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        obj_worcker.change_worcker_name(name)
        print("Имя успешно изменено")

    def change_first_name(self):
        self.check()
        print("Введите новую фамилию")
        first_name = input()
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        obj_worcker.change_worcker_first_name(first_name)
        print("Фамилия успешно изменена")

    def change_address(self):
        self.check()
        print("Введите новый адресс работника")
        address = input()
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        obj_worcker.change_worcker_address(address)
        print("Адресс изменен")

    def del_address(self):
        self.check()
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        obj_worcker.del_worcker_address()
        print("Адресс успешно удален")

    def add_phone(self):
        self.check()
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

    def del_phone(self):
        self.check()
        obj_worcker = Worckers(self.id, name=self.name, first_name=self.first_name)
        obj_worcker.del_worcker_phone()
        print("Номер телефона успешно удалён")

    def check(self):
        print("Ведите id работника или его имя и фамилию сначала имя затем фамилию")
        ans = input().split()
        if len(ans) > 1:
            self.name = ans[-2]
            self.first_name = ans[-1]
        else:
            self.id = int(ans[0])

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
                "Добавить нового работника": self.add_worcker,
                "Удалить работника": self.del_worcker,
                "Изменить название профессии работника": self.change_prof,
                "Изменить имя работника": self.change_name,
                "Изменить фамилию работника": self.change_first_name,
                "Добавить или изменить адресс работника": self.change_address,
                "Удалить адресс работника": self.del_address,
                "Добавить или изменить телефон работника": self.add_phone,
                "Удалить телефон работника": self.del_phone,
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
                      11 - Посмотреть все данные таблицы
                      12 - Назат
                      13 - Выход"""
            )
            answer = input()
            if int(answer) == 12 or answer.lower() == "назат":
                return
            elif int(answer) == 13 or answer.lower() == "выход":
                return 7
            elif int(answer) == 11 or answer.lower() == "посмотреть все данные таблицы":
                obj_worcker = Worckers(
                    self.id, name=self.name, first_name=self.first_name
                )
                for row in obj_worcker.show_all():
                    print(
                        f"id: {row[0]},\nимя: {row[1]},\nфамилия: {row[2]}\nадресс: {row[3]},\nтелефон: {row[4]},\nпрофессия: {row[5]},\nстатус: {row[6]}"
                    )
                    print("--------------------------")
                    print()
                input()
                return
            elif int(answer) == 2 or answer.lower() == "посмотреть всех работников":
                self.show_worckers()
                input()
                return
            else:
                doit[answer.lower()]()
