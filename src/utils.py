# импортируем json чтобы работать с json файлом
import json
# импортируем datetime чтобы отформатировать время в функции get_date_operation()
from datetime import datetime


def load_clients_operations(path):
    """
       Функуия загружает информацию из файла clients_operations.json
       :return: отсортированный по дате и статусу банковской операции список словарей
    """
    # вызываем менеджер контеста чтобы рабтать с json файлом
    with open(path, encoding='utf-8') as operations_file:
        # загружаем информацию
        data = json.load(operations_file)
        # сортируем список словрей где ключи имеют значение, а операции исполнены
        data = [x for x in data if x.keys() and x['state'] == 'EXECUTED']
        # сортируем по дате
        sorted_operations = sorted(data, key=lambda x: x['date'], reverse=True)
        return sorted_operations


def get_date_operation(operation):
    """
    Функция форматирует дату под нужный формат
    :return: печатает дату в нужном формате
    """
    # берем отрезок перых 10 цифр
    date_str = operation['date'][:10]
    # строка с датой преобразуется в объект `datetime` с помощью метода `strptime()`
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    # преобразуется обратно в строку с помощью метода `strftime()`
    return date_obj.strftime('%d.%m.%Y')


def get_description_operation(operation):
    """
    Функция находит описание операции
    :return: возращает описание операции
    """
    return operation['description']



