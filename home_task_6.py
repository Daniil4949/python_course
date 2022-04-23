def find_number(lst: list) -> list:
    n = len(lst)
    temp = set(lst)
    temp = list(temp)
    result = []
    for i in range(len(temp)):
        result.append(lst.count(temp[i]))
    return result


def main():
    n = int(input('Введите количество элементов списка: '))
    info = []
    for i in range(n):
        print(f'Введите {i+1} элемент списка:')
        temp = int(input())
        info.append(temp)
    result = find_number(info)
    info = set(info)
    info = list(info)
    k = len(result)
    for i in range(len(result)):
        print(f'Количество повторений числа {info[i]}: {result[i]}')
        print()


main() 

