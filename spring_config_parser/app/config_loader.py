
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

    def __validate_args(self):
        project_val = sys.argv[1]
        environment_val = sys.argv[2]
        platform_val = sys.argv[3]
        self.project = project_val
        self.output_type = self.__validate_arg("projects", project_val)
        self.environment = self.__validate_arg("environments", environment_val)
        self.platform = self.__validate_arg("platforms", platform_val)
        springendpoints_key = "{}-{}".format(self.environment, self.platform)
        self.url = self.__validate_arg("springendpoints", springendpoints_key)

    def __validate_arg(self, arg_type, arg_value):
        state = self.__parser[arg_type][arg_value]
        return state

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
        args = self.__validate_args()

    def __del__(self):
        print("ConfigLoader.del")


