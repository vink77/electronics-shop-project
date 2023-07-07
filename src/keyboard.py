from src.item import Item


class MixinKeyboard:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
        return self


class Keyboard(Item, MixinKeyboard):

    def __str__(self):
        return self.name

    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        MixinKeyboard.__init__(self)