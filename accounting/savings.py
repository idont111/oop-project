class Savings:
    def __init__(self, money: float):
        if isinstance(money, float) or isinstance(money, int):
            self.__money = money
        else:
            raise ValueError("Wrong type. Can`t create money from others type")

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, new_money: float):
        if isinstance(new_money, float) or isinstance(new_money, int):
            self.__money = new_money
        else:
            raise ValueError("Wrong type. Can`t create money from others type")

    def add_money(self, money: float):
        if isinstance(money, float) or isinstance(money, int):
            self.__money += money
        else:
            raise ValueError("Wrong type")

    def withdraw_money(self, money: float):
        if isinstance(money, float) or isinstance(money, int):
            if self.__money < money:
                print("Not enough money to withdraw ")
                self.__money = money
            self.__money -= money
        else:
            raise ValueError("Wrong type")
