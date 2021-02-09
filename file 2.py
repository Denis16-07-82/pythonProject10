if __name__ == '__main__':
    # name_file = input('Введите имя файла: ')
    with open('test_0.txt', 'w', encoding='utf-8') as my_file:
        while True:
            my_str = input('Введите числа: ')
            if my_str== '': break
            my_file.write(my_str +' ')

    with open('test_0.txt','r') as my_file:
        new_line=my_file.readline()
        my_list=new_line.split()
        p=0
        for ls in my_list:
            p+=int(ls)
    print(p)

