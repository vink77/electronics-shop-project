import pytest
from src.item import Item, InstantiateCSVError

def test_InstantiateCSVError():
    # ���� ���������
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/items_test_failed.csv')
        raise InstantiateCSVError

def test_instantiate_from_csv():
    # ���������� ������ �� ����� �����
    with pytest.raises(ValueError):
        Item.instantiate_from_csv('../src/items_test_float.csv')
        raise ValueError

    # ���� �����������
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/items_test_flo.csv')
        raise FileNotFoundError

