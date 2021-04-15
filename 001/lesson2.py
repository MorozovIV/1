HELP = """Доступные коммандыЖ
help - Напечатать справку
add - Добавить задачу в список
print - Напечатать все задачи из списка"""


stop = False
while not stop:
    command = input('Введите комманду\n ')
    command = command.strip().lower()
    if command == 'help':
        print(HELP)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        stop = True
    elif command == 'todo':
        task = input('Введите задачу: ')
        todos.append(task)
        print(f'задача{task}добавлена')
    elif command == 'print':
        print(todos)
    else:
        print('Неизвестная комманда!')
        stop = True
