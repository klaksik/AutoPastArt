import json

def readjson(name):
    with open(name, 'r') as fr:
        # читаем из файла
        used_ph = json.load(fr)
        return used_ph
def dumpjson(name, used_ph):
    with open(name, 'w') as fw:
        # записываем
        json.dump(used_ph, fw)