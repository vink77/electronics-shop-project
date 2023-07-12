"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def smart():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(smart):
    assert smart.calculate_total_price() == 200000


def test_apply_discount(smart):
    smart.pay_rate = 1.2
    assert smart.apply_discount() == 12000.0


def test_name(smart):
    smart.name = "Суперсмартфон"
    assert smart.name == 'Суперсмарт'
    smart.name = "смарт"
    assert smart.name == 'смарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item2 = Item.all[2]
    assert len(Item.all) == 5
    assert item2.name == 'Кабель'


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


