import pytest
from adapter import JSONAdapter, CSVToJSONAdapter


@pytest.fixture
def data():
    return [
        ['John', 28, '123 Main St.'],
        ['Jane', 32, '456 Oak Ave.'],
        ['Bob', 45, '789 Elm St.']
    ]


@pytest.fixture
def json_data():
    return [
        {'name': 'Jane', 'age': 32, 'address': '456 Oak Ave.'}
        ]


def test_JSONAdapter_get_data_raises_ValueError(data):
    with pytest.raises(ValueError):

        JSONAdapter(data)


def test_JSONAdapter_get_data_get_value(json_data):
    json_adapter = JSONAdapter(json_data)
    assert json_adapter.get_value(0) == {'name': 'Jane', 'age': 32, 'address': '456 Oak Ave.'}


def test_CSVToJSONAdapter_get_data(data):

    csv_to_json_adapter = CSVToJSONAdapter(data)

    transformed_data = csv_to_json_adapter.get_data()

    assert isinstance(transformed_data, list)
    assert all(isinstance(d, dict) for d in transformed_data)



