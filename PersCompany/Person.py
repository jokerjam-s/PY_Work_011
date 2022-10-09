# класс Person

class Person:
    def __init__(self, first_name, second_name, last_name, dict_phones: dict):
        self.phones = dict_phones
        self.FIO = [first_name, second_name, last_name]

    def get_phone(self):
        return self.phones.get('private')

    def get_name(self):
        return " ".join(self.FIO)

    def get_work_phone(self):
        return self.phones.get('work')

    def get_sms_text(self):
        return f"Уважаемый {self.FIO[0]} {self.FIO[1]}! Примите!"