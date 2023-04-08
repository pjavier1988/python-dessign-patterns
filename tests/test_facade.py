import pytest

from facade import (Item, Order)


@pytest.fixture(scope="module")
def order():

    item1 = Item("Product1", 20)
    item2 = Item("Product2", 10)
    items = [item1, item2]
    order = Order(items)
    return order


def test_total(order):
    assert order.get_total() == 30


