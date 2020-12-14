import time
a = time.strftime("%H", time.localtime())
a=0 # доп условие

while True:
    while int(a)>5 and int(a)<23:
        x = 10
        print("Освещение работает")
        print("Осталось", 23-int(a),"часов")
        print(a)
        print(x)
    else:
        x=20
        print("Освещение выключено")
        print("Осталось", 6-int(a),"часов")

        print(a)
        print(x)
pass
print("Конец")



