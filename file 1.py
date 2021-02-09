if __name__ == '__main__':
    name_file = input('Введите имя файла: ')
    with open(name_file, 'w', encoding='utf-8') as my_file:
        while True:
            my_str = input('Введите сообщение: ')
            if my_str== '': break
            my_file.write(my_str + '\n')

# my_file.close()
