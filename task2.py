# import os
#
# for filename in os.listdir("task_2"):
#     with open(filename, 'r') as f:
#         f.read()

# import glob
# import os
# for filename in glob.glob("task_2/*.txt"):
#     print (filename)
# import os
# d = input('Введите название директории: ')
# for filename in os.listdir('task2'):
#     if os.path.exists(f'{dir}/{filename}'):
#         if os.path.isdir(f'{dir}/{filename}'):
#             pass
#         elif os.path.isfile(f'{dir}/{filename}'):
#             with open(f'{dir}/{file}', 'r') as file:
#                 print(file.read())
#         with open(f'task2/{filename}') as file:
#             print(file.read())
# import os
# import glob
#
# def read_file(file):
#     with open(file, 'r') as f:
#         return f.read()
#
#
# def check_dir(file):
#     result = os.path.isdir(file)
#     return file
#
#
# def check_file(file):
#     result = os.path.isfile(file)
#     return result
#
#
# def check(file):
#     result = os.path.exists(file)
#     return result
#
#
# def task():
#     try:
#         d = input('Введите название директории: ')
#
#     except FileNotFoundError as ex:
#         print('Скорее всего, данные файл не существует!')
#
#     else:
#         file.close()
#         for file in os.listdir(d):
#             if check(f'{d}/{file}'):
#                 if check_file(f'{d}/{file}'):
#                     print(read_file(f'{d}/{file}'))
#                 else:
#                     for filename in glob.glob(f"{d}/{file}/*.txt"):
#                         with open(filename, 'r') as f:
#                             print(f.read())
#
#
# def main():
#     task()
#
#
# main()

import os



def print_docs(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError('Данный файл не существует!')
    files = os.walk(directory)
    for dir in files:
        print(f'Директория {dir[0]} хранит:')
        print(f'Папки: {", ".join([folder for folder in dir[1]])}')
        print(f'Файлы: {", ".join([file for file in dir[2]])}')
        print()


print_docs('C:/')
#вводите здесь любую вашу папку