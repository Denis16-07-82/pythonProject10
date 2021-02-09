if __name__=='__main__':
    with open('test_word.txt','r') as my_file:
        strings=0
        while True:
            ln=my_file.readline()
            if ln=='':break
            strings+=1
            word_count=len(ln.split())
            print(f"Количество слов в {strings}й строке: {word_count}")
        print(f"Количество строк: {strings}")

