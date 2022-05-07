"""Домашнее задание, пункт номер 3"""
import csv


class Restaurant:

    def __init__(self, number: int , price: int, name: str, tips: int):
        self.__number = number
        self.__price = price
        self.__name = name
        self.__tips = tips

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def get_price(self):
        return self.__price

    def get_tips(self):
        return self.__tips

    def set_name(self, name):
        self.__name = name  

    def set_price(self, price):
        self.__price = price

    def set_number(self, number):
        self.__number = number

    def set_tips(self, tips):
        self.__tips = tips

    price = property(get_price, set_price)
    name = property(get_name, set_name)
    tips = property(get_tips, set_tips)
    number = property(get_number, set_number)


def main():

    print('Добрый день! Сегодня у вас будет заказ!\n')
    print("Будьте добры, введите пару сведений о заказе\n")
    n = int(input('Введите количество заказов: '))
    info = []
    for i in range(n):
        number = int(input(f'Введите номер {i+1} столика: '))
        price = int(input(f'Введите стоимость {i+1} заказа: '))
        name = input(f'Введите имя {i+1} официанта: ')
        tips = input(f'Введите количество чаевых {i+1} заказа: ')
        i = Restaurant(number, price, name, tips)
        info.append(i)

    Names = []
    Numbers = []
    Tips = []
    Prices = []
    for i in range(n):
        Names.append(info[i].name)
        Numbers.append(info[i].number)
        Tips.append(info[i].tips)
        Prices.append(info[i].price)
    data = {
        "Name": Names,
        "Number": Numbers,
        "Price": Prices,
        "Tips": Tips,
    }
    fieldnames = ['Name', 'Number', 'Price', 'Tips']
    with open('task_3.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(n):
            writer.writerow({'Name': Names[i], 'Number': Numbers[i], 'Price': Prices[i], 'Tips': Tips[i]})

main()