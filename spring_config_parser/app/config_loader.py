
import configparser
import os
import sys

class ConfigLoader():

    def __init__(self):
        print("ConfigLoader.init")
        print("loading config.ini")
        fn = os.path.join(os.path.dirname(__file__), 'config.ini')
        try:
            f = open(fn, 'r')
        except FileNotFoundError as fnfe:
            print("config.ini file not found!")
        except:
            print("config.ini unexpected error: ", sys.exc_info()[0])
            raise

    def __del__(self):
        print("ConfigLoader.del")