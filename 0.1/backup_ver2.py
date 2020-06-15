import os
import time

source_dir = "C:\\users\\Пользователь\\PycharmProjects\\"
target_dir = "F:\\backup"
today = target_dir + "_" + time.strftime('%d%m%Y')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)
target = today + os.sep + now + '.zip'
zip_command = '"c:\\program files\\winrar\\rar.exe" a -ag -r {0} {1} {2}'.format(target, '', source_dir)
if os.system(zip_command) == 0:
    print("Резервная копия успешно создана в", target)
else:
    print("Создание резарвной копии не удалось")
