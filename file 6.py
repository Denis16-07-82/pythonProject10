with open('lessen_file.txt','r',encoding='utf=8') as my_less :
    my_dict = {}
    while True:
        my_strin=my_less.readline().rstrip('\n')
        print(my_strin)
        if my_strin=='':break
        ln=my_strin.split()
        my_dict.update(my_dict.fromkeys([ln[0].rstrip(':')]))
        les_time=int(ln[1].rstrip('(л)'))+int(ln[2].rstrip('(п)'))
        my_dict[ln[0].rstrip(':')]=les_time
    print(my_dict)
    print(my_dict.get('химия'))
