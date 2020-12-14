import random

tries = 0

number = random.randint(1, 50)

print('Ну что??? Получится угадать число от 1 до 50??? Попробуй!!!')

while tries < 6:
    guess = int(input("Введи число:"))

    tries += 1

    if guess < number:
        print('Маловато')

    if guess > number:
        print('Многовато')

    if guess == number:
        print(f'Поздравляю ты угадал мое число за {tries} попыток')
        break
    if guess != number and tries == 6:
        print(f"Извини ты не угадал. Мое число было: {number}")
        break

