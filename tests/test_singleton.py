import pytest

from singleton import Logger


@pytest.fixture(scope="module")
def logger():

    logger = Logger()
    return logger


def test_total(logger):
    logger2 = Logger()
    assert logger == logger2


