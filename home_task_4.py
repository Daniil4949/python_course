
# from datetime import date
# from datetime import time
# from datetime import datetime
#
#
#
# def SumRange(start: int, end: int) -> int:
#     if start > end:
#         start, end = end, start
#     lst = [i for i in range(start, end + 1)]
#     result = sum(lst)
#     return result
#
#
# def sum_numbers(number: int) -> int:
#     number = str(number)
#     number = list(number)
#     result = 0
#     for i in range(len(number)):
#         result += int(number[i])
#     return result
#
#
# def date_2(i):
#     i = datetime.now()
#     return i
#
#
# def date_result():
#     A = [date_2(i) for i in range(10)]
#     for i in A:
#         print(A)
#
#
#
# date_result()
#
# from datetime import datetime
#
#
# def speedTest(func):
#     def wrapper(lst):
#         start = datetime.now()
#         result = func(lst)
#         end = datetime.now()
#         print(f'Время выполнения: {end-start} секунд')
#      return wrapper
# @speedTest
# def fetch_webpage(lst):
#     lst = sum(lst)
#
# @speedTest
# def test(count):
#     for i in range(count):
#         pass

#fetch_webpage('https://google.com')"""

from random import randint


#def decorator_function(func):
 #   def wrapper():
  #      print('Выполняю генерацию списка со случайными числами!')
  #      print(func())
   #     print('Операция завершена!')
   # return wrapper()


#@decorator_function
#def random_list(): return [randint(1, 100) for i in range(10)]


#def filter_2(function, lst):
 #   result = []
  #  for i in range(len(lst)):
   #     if function(lst[i]):
    #        result.append(lst[i])
    #return result

#print(filter_2(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6]))


# import requests
#
#
# def speed_test(func):
#     """Определение скорости выполнения программы"""
#     def wrapper(site):
#         import time
#         start = time.time()
#         func(site)
#         end = time.time()
#         print(f'Запрос был выполнен за {end - start} секунд')
#     return wrapper
#
#
# @speed_test
# def fetch_webpage(website):
#      webpage = requests.get(website)
#
#
# fetch_webpage('https://google.com')

# def decorator_function(func):
#     """Фунция-декоратор"""
#     def wrapper(lst: list) -> list:
#         import time
#         result = []
#         print('Выполняется поиск элементов, кратных трем!')
#         result = func(lst)
#         print(result)
#         print("Поиск выполнен!")
#         end = time.time()
#         return result
#     return wrapper
#
#
# @decorator_function
# def function_2(lst: list) -> list:
#     result = list(filter(lambda x: x % 3 == 0, lst))
#     return result
#
#
# function_2([1, 2, 3, 5, 6, 9, 12, 16, 18, 24])
# print(decorator_function.__doc__)

# def decorator_function(func):
#     def wrapper(lst):
#         import time
#         start = time.time()
#         result = []
#         print('Начало работы программы!')
#         result = func(lst)
#         print(result)
#         print('Программа завершила свою работу!')
#         end = time.time()
#         print(f'Программа завершила работу за {end - start} секунд')
#         return result
#     return wrapper
#
#
#
#
# F = lambda x: x **3
#
#
# def map_2(func, lst: list) -> list:
#     for i in range(len(lst)):
#         lst[i] = func(lst[i])
#     return lst
#
#
# @decorator_function
# def cube(lst):
#     result = map_2(F, lst)
#     return result
#
#
# @decorator_function
# def check(lst):
#     result = list(filter(lambda x: x % 2 ==0, lst))
#     return result
#
#
# check([1, 2, 3, 4])
# import re
#
#
# def check_str(s: str):
#     if s == '0':
#         pass
#     elif s.isdigit():
#         print(f'Вы ввели положительное целое число: {s}')
#         result = int(s)
#     elif s[1::].isdigit() and s[0] == '-':
#         print(f'Вы ввели отрицательное целое число: {s}')
#         result = int(s)
#         result *= -1
#     elif s[0] == '-':
#         fact = False
#         if s.count('.') == 1:
#             fact = True
#         else:
#             print('Введено неверное значение!')
#             return -1
#         if fact:
#             result = float(s[1::])
#             print(f'Вы ввели дробное отрицательное число: {s}')
#             result *= -1
#             return result
#     elif s[0] != '-' and '.' in s:
#         fact = False
#         if s.count('.') == 1:
#             fact = True
#         else:
#             print('Введено неверное значение!')
#             return -1
#         if fact:
#             result = float(s)
#             print(f'Вы ввели дробное положительное число: {s}')
#             return result


# def check(s):
#     fact = False
#     pattern = r'[0-9]\-\.'
#     for i in s:
#         if re.search(pattern, i):
#             fact = True
#         else:
#             return False
#     return fact

# def check(s):
#     if bool(float(s[1::])) == True or bool(float(s)) == True:
#         return True
#     else:
#         return False
#
#
# print('799.6'.isdigit())



# def isfloat(s):
#     find = re.findall(r"\d+(\.*)(\d*)", s)
#
#     if find[0][0] and find[0][1]:
#         pattern = r'[0-9]\-\.'
#         for i in s:
#             if re.search(pattern, i):
#                 fact = True
#             else:
#                 return False
#     else:
#         return False
import re


def isfloat(s: str) -> bool:
    find = re.fullmatch(r"\d*\.\d+", s)
    if find:
        return True
    else:
        return False


def check(s):
    fact = False
    pattern = r'[0-9]'
    for i in s:
        if re.search(pattern, i):
            fact = True
        else:
            return False
    return fact


def check_str(s: str):
    if isfloat(s) or check(s) or (check(s[1:]) and s[0] == '-') or (isfloat(s[1:]) and s[0] == '-'):
        if s.isdigit():
            print(f'Вы ввели положительное целое число: {s}')
            result = int(s)
        elif s[1::].isdigit() and s[0] == '-':
            print(f'Вы ввели отрицательное целое число: {s}')
            result = int(s)
            result *= -1

        elif isfloat(s[1:]) and s[0] == '-':
            print(f'Вы ввели дробное отрицательное число: {s}')
            result = float(s[1:])
            result *= -1
        elif isfloat(s) == True:
            result = float(s)
            print(f'Вы ввели дробное положительное число: {s}')
            return result

    else:
        print(f'Вы ввели некорректное число: {s}')
        return -1


check_str('55')
check_str('-55')
check_str('55.1')
check_str('-55.11')
check_str('р3grvfd')

