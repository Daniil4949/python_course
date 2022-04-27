"""Домашнее задание, пункт номер 2"""
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, price: int,  weight: int, shelf_time: str):
        self.__price = price
        self.__weight = weight
        self.__shelf_time = shelf_time

    @abstractmethod
    def method_1(self):
        pass


class Milk(Product):
    def method_1(self):
        print('Молоко')


class Meat(Product):
    def method_1(self):
        print("Мясо")


milk1 = Milk(price=10, weight=20, shelf_time='Один месяц')
meat1 = Meat(price=40, weight=60, shelf_time='Неделя')

milk1.method_1()
meat1.method_1()

