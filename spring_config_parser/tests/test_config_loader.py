
import pytest
from app.config_loader import ConfigLoader

def test_instantiate_config_loader():
    '''init should read in the config.ini file successfully'''
    config = ConfigLoader()
    assert isinstance(config, ConfigLoader) == True
