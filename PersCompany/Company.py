# Класс Company

from Person import Person 

class Company():
    def __init__(self, company_name, type_company, phone_number: dict, *args: Person):
        self.worker_list = list(args)
        self.company_name = company_name
        self.type = type_company
        self.phones_company = phone_number

    def get_name(self):
        return self.company_name

    def get_phone(self):
        if not self.phones_company.get("contact") == None:
            return self.phones_company.get("contact")
        else:
            for worker in self.worker_list:
                if not worker.get_work_phone() == None:
                    return worker.get_work_phone()
            return None

    def get_sms_text(self):
        return f"Уважаемый {self.company_name}! Примите {self.type}!"