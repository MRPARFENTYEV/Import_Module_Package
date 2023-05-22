import datetime
from application import salary
from application.db import people



date = datetime.datetime.today()
if __name__ == '__main__':
    print(salary.calculate_salary())
    print(''.join(people.get_employees('Product manager')))
    print(people.get_phone_by_name(people.get_employees('Product manager')))
    print(people.number_1)
    print(''.join(people.time_zone))
    print(f'Телефон активен: {people.valid}')
    print(date)