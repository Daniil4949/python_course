import re


class City:

    def __init__(self, index: str):
        self.__index = index

    def __str__(self):
        return f'This class was created to define cities and towns in Belarus by indexes.'

    def __len__(self):
        return len(self.__index)

    def define_city(self) -> str:

        if re.fullmatch(r'220000', self.__index):
            return 'Minsk'
        elif re.fullmatch(r'224000', self.__index):
            return 'Brest'
        elif re.fullmatch(r'210000', self.__index):
            return 'Vitebsk'
        elif re.fullmatch(r'246000', self.__index):
            return 'Gomel'
        elif re.fullmatch(r'212000', self.__index):
            return 'Mogilev'
        elif re.fullmatch(r'230000', self.__index):
            return 'Grodno'
        elif len(self) != 6:
            raise IndexError('This city does not exist.')
        else:
            raise IndexError('This city is not a regional center.')


city1 = City('220000')
print(city1.define_city())
print(city1)

"""
CREATE NEW DATABASE

CREATE DATABASE Lesson;

USE Lesson;

CREATE TABLE computer(
code INT,
model VARCHAR(50),
speed SMALLINT,
ram SMALLINT,
hd real,
cd VARCHAR(10),
price INT);

INSERT INTO computer VALUES(
1,
"Asus",
2,
8,
1000,
null,
800);

INSERT INTO computer VALUES(
2,
"Acer",
3,
16,
1200,
null,
1100);

INSERT INTO computer VALUES(
3,
"HP",
4,
32,
1200,
null,
1500);


INSERT INTO computer VALUES(
4,
"Lenovo",
1,
4,
700,
null,
300);


SELECT model, speed, cd FROM computer WHERE ram between 8 and 16;
SELECT price FROM computer WHERE hd < 1000;
SELECT * FROM computer;
UPDATE computer SET price = price * 2 WHERE price < 400;

"""