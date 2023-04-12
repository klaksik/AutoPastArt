from get_data import *
import random
import os


def createbuff(n):
    used_ph = readjson('data')
    photos = []
    for i in range(n):
        pathf = random.choice(os.listdir(f"ph"))
        path = f'ph/'
        fullpath = path + pathf
        if pathf in used_ph:
            os.remove(fullpath)
            print("удалил")
        else:
            used_ph.append(pathf)
            print(fullpath)
            try:
                size = os.stat(fullpath)
            finally:

                if size.st_size < 11662732:
                    photos.append(fullpath)

                dumpjson('data', used_ph)

    return photos