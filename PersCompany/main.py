from os import system
from Person import Person
from Company import Company


def send_sms(*args):
    for el in args:
        if not el.get_phone() == None:
            print(f"Sms send to {el.get_phone()} with {el.get_sms_text()}")
        else:
            print(f'Sms did not send to {el.get_name()}')


def main():
    system('cls')

#    person1 = Person("Ivan", "Ivanovich", "Ivanov", {'private': 7543})
#    person2 = Person("Alex", "Ivanovich", "Borisov", {'private': 73543, 'work': 15678})
#    company1 = Company("Ozon", 'Marketplace', {'contact':6789}, person1,person2)
#    company2 = Company("Azon", 'Market', {'private':6789}, person1)
#
#    send_sms(person1,person2,company1,company2)


    person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
    person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
    person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
    person4 = Person("John", "Unknown", "Doe", {})
    company1 = Company("Bell", "OOO", {"contact": 111}, person3, person4)
    company2 = Company("Cell", "AO", {"non_contact": 222}, person2, person3)
    сотрапуЗ = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4) 

    send_sms(person1, person2, person3, person4, company1, company2, сотрапуЗ)




if __name__ == "__main__":
    main()