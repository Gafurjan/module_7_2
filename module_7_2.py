import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    for i  in strings: # write text into the file
        file.write(i + '\n')
    file.close()

    file = open(file_name, 'r', encoding='utf-8')
    tpl = tuple()
    dct = dict()
    lns = 0
    while True:
        a = file.tell()
        # считываем строку
        line = file.readline()
        lns += 1

        # прерываем цикл, если строка пустая
        if not line:
            break

        dct[lns, a] = line.strip()
    # for key, value in dct.items():
    #     print(f"({key}: {value})")
    # закрываем файл
    file.close
    return dct


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


