
import configparser
import os
import sys

class ConfigLoader():

    def __load_config_file(self):
        print("loading config.ini")
        fn = os.path.join(os.path.dirname(__file__), 'config.ini')
        with open(fn, 'r') as configfile:
            self.parser = configparser.ConfigParser()
            self.parser.sections()
            self.parser.read(fn)
            return self.parser

    def __init__(self):
        print("ConfigLoader.init")
        fn = os.path.join(os.path.dirname(__file__), 'config.ini')
        try:
            f = open(fn, 'r')
        except FileNotFoundError as fnfe:
            print("config.ini file not found!")
        except:
            print("config.ini unexpected error: ", sys.exc_info()[0])
            close(fn)
        self.__parser = self.__load_config_file()

    def __del__(self):
        print("ConfigLoader.del")

    def validate(self, arg_type, arg_value):
        state = self.__parser[arg_type][arg_value]
        return state

