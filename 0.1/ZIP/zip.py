import os
from zipfile import ZipFile

def zip(path, zpath):
    zfile = ZipFile(zpath,'w')
    if os.path.isfile(path):
        zfile.write(path)
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                zfile.write(root + "/" + file)
    zfile.close()

zip("..", "my.zip")