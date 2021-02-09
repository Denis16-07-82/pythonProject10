with open('test.txt','r',encoding='utf=8') as my_file:
    ln=[]
    while True:
        content=my_file.readline().rstrip('\n')
        if content=='':break
        ln.append(content)
    sum_salary=0
    for i in range(len(ln)):
        salary=int(ln[i].split(',')[1].split(':')[1])
        if salary < 20000:
            print(ln[i])
        sum_salary+=salary
    print(f"Средний оклад:{sum_salary/len(ln)}")