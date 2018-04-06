
# configs stored in ini

import configparser


class ConfigLoader():

    def __init__(self):
        print("ConfigLoader.init")
        print("loading config.ini")
        f = open('config.ini', 'r')