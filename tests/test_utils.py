from src.utils import *
import pytest


@pytest.fixture
def operation():
    path = '/home/vitaly/Coursework_3/src/clients_operations.json'
    operation = load_clients_operations(path)[-1]
    return operation


def test_load_clients_operation():
    path = '/home/vitaly/Coursework_3/src/clients_operations.json'
    assert type(load_clients_operations(path)) == list


def test_get_date_operation(operation):
    assert len(get_date_operation(operation)) == 10


def test_get_description_operation(operation):
    assert type(get_description_operation(operation)) == str


def test_get_from_operation_no_information(operation):
    del operation['from']
    assert get_from_operation(operation) == 'There is no information -->'


def test_get_from_operation_account(operation):
    operation['from'] = 'Счет 84903904838482056710'
    assert get_from_operation(operation) == 'Счет **6710 -->'


def test_get_from_operation_any(operation):
    operation['from'] = 'Visa Classic 2832738287462912'
    assert get_from_operation(operation) == 'Visa Classic 2832 73** **** 2912 -->'


def test_get_from_operation(operation):
    assert get_from_operation(operation) == 'Visa Classic 8906 17** **** 3215 -->'


def test_get_to_operation_account(operation):
    operation['to'] = "Счет 96527012349577388612"
    assert get_to_operation(operation) == 'Счет **8612'


def test_get_to_operation(operation):
    assert get_to_operation(operation) == 'Visa Classic 8906 17** **** 3215'


def test_get_amount(operation):
    operation['operationAmount']['amount'] = '34353.3'
    assert get_amount(operation) == '\x1b[31m34353.3\x1b[0m'


def test_get_amount_incorrect(operation):
    operation['operationAmount']['amount'] = '343r53.3'
    assert get_amount(operation) == '\x1b[31mValueError: Incorrect amount\x1b[0m'


def test_get_currency(operation):
    assert len(get_currency(operation)) == 3


def test_get_currency_incorrect(operation):
    operation['operationAmount']['currency']['name'] = 'U3D'
    assert get_currency(operation) == "Unknow currency"
