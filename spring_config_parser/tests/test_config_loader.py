
import pytest
from app.config_loader import ConfigLoader

def test_instantiate_config_loader():
    '''init should read in the config.ini file successfully'''
    config = ConfigLoader()
    assert isinstance(config, ConfigLoader) == True

def test_pass_bad_project_arg_to_config_loader():
    '''config_loader should check and test a bad value used for the cli project arg'''
    project_val = "media-core-gateway"
    config = ConfigLoader()
    assert config.validate("projects", project_val) == 'true'
