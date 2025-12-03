import string
import time

while True:
    text = 'ROSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    tempo =''
    for ch in text:
        for i in string.printable:
            if i == ch or ch == i:
                time.sleep(0.02)
                print(tempo+i)
                tempo +=ch
                break
        else:
            time.sleep(0.02)
            print(tempo+i)


    for i in range(len(text), 0, -1):
        time.sleep(0.02)
        print(text[:i - 1])