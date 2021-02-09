with open('test_1.txt', 'r', encoding='utf=8') as my_file:
    ln = []
    while True:
        my_string = my_file.readline().rstrip('\n')#удаляет \n
        if my_string == '':break
        ln.append(my_string)#добавляет строку в список
    print(ln)
with open('test_2','w',encoding='utf=8') as file_write:
    ln_rus = ['Один', 'Два', 'Три', 'Четыре']
    for i in range(len(ln)):
        ln_new = ln[i].split('-')
        ln_new.insert(0, ln_rus[i])#добавляет в список ln_new на позицию 0 строку с индексом i из списка ln_rus
        ln_new.pop(1)#удаляет из списка строку с индексом 1
        print(ln_new)
        file_write.write('-'.join(ln_new)+'\n')#объеденяет строки в строку с разделителем '-'
