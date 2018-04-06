
import pytest
from spring_config_parser import config_loader

def test_instantiate_config_loader():
    '''init should read in the config.ini file successfully'''
    config = config_loader.ConfigLoader()
    assert config == isinstance(config_loader.ConfigLoader)