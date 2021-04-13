from termcolor import colored, cprint
while True:
    try:
        money = int(input('Введите колличество денег на покупки   :'))
        while money > 1:
            item = int(input('Введите колличество покупаемых товаров   :'))
        else:
            cprint('Не верно введено число', 'red')

    except ValueError:
        cprint('Не верно введено число', 'red')

s=0
for item in range (0,item):
    price = int(input('Введите цену товара :'))
    s=s+price
    item -=1
if money >=s:
    cprint('Денег хватает, можно брать!!!','green')
else:
    cprint('Денег не хватает, не возьмем!','red')
print()
print('Конец программы')