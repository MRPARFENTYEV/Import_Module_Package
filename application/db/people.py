import phonenumbers
from phonenumbers import timezone, carrier

workers = {'System analyst': ['Геннадий Черепанов, Алексей Коршунов'], 'Product manager': ['Сергей Духарев']}
phones = {'Геннадий Черепанов': '88005553535', 'Алексей Коршунов': '89036842085', 'Сергей Духарев': '+74955987109'}


def get_employees(speciality):
    for worker_spec, worker_data in workers.items():
        if speciality in worker_spec:
            return worker_data
    return 'Not found'


def get_phone_by_name(Worker_name):
    for name, phone_num in phones.items():
        if Worker_name[0] in name:
            return phone_num
    return 'Not found'


number_1 = phonenumbers.parse(get_phone_by_name(get_employees('Product manager')))
time_zone = timezone.time_zones_for_number(number_1)
valid = phonenumbers.is_valid_number(number_1)
