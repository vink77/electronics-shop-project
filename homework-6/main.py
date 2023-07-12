from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('../src/items_test_fail.csv')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('../src/items_test_failed.csv')
    # InstantiateCSVError: Файл item.csv поврежден

    # В файле items.csv количество товара не целое число.
    Item.instantiate_from_csv('../src/items_test_float.csv')
    # NotIntegerError: Количество товара не целое
