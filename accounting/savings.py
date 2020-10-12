class Savings:
    def __init__(self, money: float):
        self.__money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, new_money: float):
        self.__money = new_money

    def add_money(self, money: float):
        self.__money += money

    def withdraw_money(self, money: float):
        if self.__money < money:
            print("Not enough money to withdraw ")
            self.__money = money
        self.__money -= money
