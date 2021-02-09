with open('firma.txt','r',encoding='utf=8') as my_firm :
    my_dict = {}
    sum_profit=0
    while True:
        my_strin=my_firm.readline().rstrip('\n')
        print(my_strin)
        if my_strin=='':break
        ln=my_strin.split()
        my_dict.update(my_dict.fromkeys([ln[0].rstrip(':')]))
        profit=int(ln[2])-int(ln[3])
        i=0
        if profit >= 0:
            sum_profit+=profit
            i+=1
        my_dict[ln[0].rstrip(':')]=profit
    print(my_dict)
    new_dict=dict.fromkeys(['average_profit'])
    if i !=0:
        new_dict['average_profit']=sum_profit/i
    print(new_dict)
    my_list=[my_dict,new_dict]
    print(my_list)
import json
with open('json_file.json','w',encoding='utf=8') as json_text:
    json.dump(my_list,json_text)
with open('json_file.json','r',encoding='utf=8') as json_text:
    data=json.load(json_text)
    print(data)