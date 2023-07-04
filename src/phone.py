from src.item import Item
class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        if type(number_of_sim)== int and number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")


    def __repr__(self):
        result =f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'
        return result

    def __str__(self):
        return f'{self.name}'

