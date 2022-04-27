"""Домашнее задание, пункт номер 1"""


class Student:

    def __init__(self, firtsName: str = 'Daniil', lastName: str = 'Kimstach', groupNumber: str = '121702', age: int = 18):
        self.__firstName = firtsName
        self.__lastName = lastName
        self.__groupNumber = groupNumber
        self.__age = age

    def getfullName(self):
        name = self.__firstName + ' ' + self.__lastName
        return name

    def get_age(self):
        return self.__age

    def get_group_number(self):
        return self.__groupNumber

    def SetNameAge(self, fname: str, lname: str, age: int):
        self.__firstName = fname
        self.__lastName = lname
        self.__age = age

    def SetGroupNumber(self, group: str):
        self.__groupNumber = group

    def __str__(self):
        print('Описывается класс студента')


student1 = Student()
student2 = Student('Igor', 'Larin', '121701', 18)
print(student2.getfullName())
student2.SetGroupNumber('121701')
print(student2.get_group_number())
student2.SetNameAge('Alex', 'Swak', 17)
print(student2.getfullName())
print(student1.getfullName())
student3 = Student('Igor', 'Laptcky', '124702', 19)
print(student3.get_age())
student3.SetGroupNumber('121701')
print(student3.get_group_number())
Student.__str__(student1)