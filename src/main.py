from utils import *

for operation in load_clients_operations()[:5]:
    print(get_date_operation(operation), get_description_operation(operation))
    print(get_from_operation(operation), get_to_operation(operation))
    print(get_amount(operation), get_currency(operation))
    print()
