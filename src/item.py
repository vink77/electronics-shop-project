import csv

import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'Файл items.csv поврежден'


class NotIntegerError(ValueError):
    def __init__(self, *args, **kwargs):
        self.message = 'не целое'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        """
        Создание экземпляра класса item.


        :param __name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        result = f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity})'
        return result

    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        try:
            with open('../src/items.csv', 'r', encoding='windows-1251') as csvfile:
                data = csv.DictReader(csvfile)
                for item in data:
                    name = item['name']
                    price = cls.string_to_number(item['price'])

                    if item['quantity'] is None:
                        raise InstantiateCSVError
                    else:
                        try:
                            int(item['quantity'])
                        except ValueError:
                            print("количество товара не целое")
                        quantity = cls.string_to_number(item['quantity'])
                    cls(name, price, quantity)

        except FileNotFoundError:
            print('Отсутствует файл item.csv')

        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(string_number):
        result = int(float(string_number))
        return result

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price
