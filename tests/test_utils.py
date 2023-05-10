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


