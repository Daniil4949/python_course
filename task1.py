def longest_words(file):
    with open(file, 'rb') as file:
        content = file.read().decode('utf-8')
    info = []
    content = content.split()
    l = []
    for i in content:
        l.append(len(i))
    m = max(l)
    result = []
    for i in content:
        if len(i) == m:
            result.append(i)
    result = set(result)
    result = list(result)
    if len(result) == 1:
        return result[0]
    elif len(result) > 1:
        return result


def main():
    try:
        name_file = input('Enter name of txt-file:') + '.txt'
        with open(name_file, 'rb') as file:
            pass
    except FileNotFoundError as ex:
        print('Most likely, these file does not exist.')
        print(ex)
    else:
        file.close()
        print(longest_words(name_file))


main()
