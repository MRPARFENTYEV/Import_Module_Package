import datetime
import sys

sys.path.insert(1, 'application')
sys.path.insert(2, 'application/db')
from salary import calculate_salary
from people import get_employees, get_phone_by_name, number_1, time_zone, valid
import datetime

date = datetime.datetime.today()
if __name__ == '__main__':
    print(calculate_salary())
    print(''.join(get_employees('Product manager')))
    print(get_phone_by_name(get_employees('Product manager')))
    print(number_1)
    print(''.join(time_zone))
    print(f'Телефон активен: {valid}')
    print(date)
