from utils import *

PATH = '/home/vitaly/Coursework_3/src/clients_operations.json'

for operation in load_clients_operations(PATH)[:5]:
    print(get_date_operation(operation), get_description_operation(operation))

