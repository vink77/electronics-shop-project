"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

@pytest.fixture
def smart():
    return Item("Смартфон", 10000, 20)

def get(smart):
    assert smart.name == "Смартфон"
    assert smart.price == 10000
    assert smart.quantity == 20
def test_calculate_total_price(smart):
    assert smart.calculate_total_price() == 200000

def test_apply_discount(smart):
    smart.pay_rate = 0.5
    assert smart.apply_discount() == 5000.0

    smart.pay_rate = 1.5
    assert smart.apply_discount() == 15000.0