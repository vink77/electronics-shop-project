from src.item import Item
class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim: int) -> None:
        print("Инициализация Phone")
        super().__init__(name, price, quantity)
        print("Инициализация Phone1")

        self._number_of_sim = number_of_sim
        print(self.number_of_sim)

        print("Инициализация Phone2")

        print(number_of_sim)


    def __repr__(self):
        result =f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'
        return result

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        print(self._number_of_sim)
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, news_number):
        if type(news_number) == int and news_number > 0:
            self._number_of_sim = news_number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")


