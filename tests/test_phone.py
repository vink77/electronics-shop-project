import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture
def smart():
    """фикстура Phone"""
    return Phone("iPhone 14", 120_000, 5, 2)

def test_repr(smart):
    """тест метода repr"""
    assert repr(smart) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str(smart):
    """тест метода str"""
    assert str(smart) == 'iPhone 14'

def test_init(smart):
    """тест инициализации"""
    assert smart.name == "iPhone 14"
    assert smart.price == 120_000
    assert smart.quantity == 5
    assert smart.number_of_sim == 2


def test_add():
    """тест сложения"""
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("Samsung", 20000, 15)
    assert item1 + phone1 == 35
    with pytest.raises(AssertionError):
        assert item1 + phone1 == 25

def test_number_of_sim(smart):
    """тест setter"""
    with pytest.raises(ValueError):
        smart.number_of_sim = 0
    smart.number_of_sim = 6
    assert smart.number_of_sim == 6



