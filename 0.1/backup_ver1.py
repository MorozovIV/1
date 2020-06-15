import os
import time

source_dir = "C:\\users\\Пользователь\\PycharmProjects\\"
target_dir = "F:\\backup"
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# print('StartPath')
# print(source_dir)
# print(type(source_dir))
# print(target_dir)
# print(type(target_dir))
# print(target)
# print(type(target))
# print('EndPath')
# zip_command = "zip -qr {0} {1}".format(target_dir,' '.join(source_dir))   #It's no work
# zip_command = '"c:\\program files\\winrar\\rar.exe" a -ag -m5 -r F:\\backup C:\\users\\Пользователь\\PycharmProjects\\' # It's work
# zip_command = '"c:\\program files\\winrar\\rar.exe" a -ag -r F:\\backup C:\\users\\Пользователь\\PycharmProjects\\'# It's work
zip_command = '"c:\\program files\\winrar\\rar.exe" a -ag -r {0} {1} {2}'.format(target_dir, '', source_dir)
# print(type(zip_command))
# zip_command = '"c:\\program files\\winrar\\rar.exe" a -ag -r {0} {1}'.format(target_dir,' '.join(source_dir))"
print(zip_command)
# print(type(zip_command))
if os.system(zip_command) == 0:
    print("Резервная копия успешно создана в", target)
else:
    print("Создание резарвной копии не удалось")
