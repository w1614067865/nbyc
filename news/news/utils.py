from os.path import realpath, dirname
import json


def get_config(name):
    try:
        path = dirname(realpath(__file__)) + '\\configs\\' + name + '.json'
        with open(path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
        with open(path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())



# if __name__ == '__main__':
#     result = get_config('gaoxinbendidongtai')
#     print(result)