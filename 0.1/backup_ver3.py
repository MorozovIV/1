# -*- coding: UTF-8 -*-
import os
import time

source_dir = "C:\\users\\Пользователь\\PycharmProjects\\"
target_dir = "F:\\backup"
today = target_dir + "_" + time.strftime('%d%m%Y')
#now = time.strftime('%H%M%S')
comment = input("Введите комментарий -->")
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)
if len(comment) == 0:
    target = today + os.sep + '.zip'
else:
    target = today + os.sep + '_' + comment.replace(' ', '_') + '_' + '.zip'

#target = today + os.sep + now + '.zip'
zip_command = '"c:\\program files\\winrar\\rar.exe" a -agDDMMYYYY -r {0} {1}'.format(target, ''.join(source_dir))
if os.system(zip_command) == 0:
    print('Каталог успешно создан', today)
    print("Резервная копия успешно создана в", target)
else:
    print("Создание резарвной копии не удалось")
