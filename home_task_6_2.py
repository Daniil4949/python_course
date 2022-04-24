import json
import csv
import openpyxl


def main():
    data = {
        'Slava': ['111111', '47', 'Minsk', '111098'],
        'Oleg': ['222043', '34', 'Berlin', '555678'],
        'Sergey': ['679432', '25', 'Paris', '232345']
    }
    fieldnames = ['Name', 'ID', 'Age', 'City', 'Number']
    info = list(data.values())
    names = list(data.keys())

    with open('file_7.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(data.keys())):
            writer.writerow({'Name': names[i], 'ID': info[i][0], 'Age': info[i][1], 'City': info[i][2], 'Number': info[i][3]})
    with open('file_7.csv', 'r') as file:
        info_3 = []
        for row in file:
            temp = []
            temp = row
            info_3.append(row)
    info_2 = []
    for i in range(len(info_3)):
        if i % 2 == 0:
            info_2.append(info_3[i])
    book = openpyxl.Workbook()
    sheet = book.active
    for i in range(len(data.keys())):
        sheet[chr(66 + i) + '1'] = 'person'+str(i + 1)
    for i in range(len(data.keys())):
        sheet[chr(65) + str(i + 2)] = fieldnames[i]
    for i in range(len(data.keys())):
        sheet[chr(66 + i) + '2'] = names[i]
    for i in range(len(data.keys())):
        sheet[chr(66 + i) + '3'] = info[i][0]
    for i in range(len(data.keys())):
        sheet[chr(66 + i) + '4'] = info[i][3]
    book.save('my_book2.xlsx')
    book.close()


main()