
import pytest
from app.config_loader import ConfigLoader

def test_instantiate_config_loader():
    '''init should read in the config.ini file successfully'''
    config = ConfigLoader()
    assert isinstance(config, ConfigLoader) == True

def test_pass_bad_project_arg_to_config_loader():
    '''config_loader should raise an exception when a bad cli arg is passed'''
    arg_type = "projects"
    arg_val = "BADARGUMENT"
    config = ConfigLoader()
    with pytest.raises(KeyError) as ke:
        config.validate(arg_type, arg_val)
        assert KeyError in str(ke.value)

def test_pass_good_project_arg_to_config_loader():
    '''config_loader should return 'true' when a good cli arg and active project is passed'''
    arg_type = "projects"
    arg_val = "media-core-gateway"
    config = ConfigLoader()
    assert config.validate(arg_type, arg_val) == 'true'

def test_pass_good_project_arg_to_config_loader():
    '''config_loader should return 'false' when a good cli arg inactive project is passed'''
    arg_type = "projects"
    arg_val = "media-core-ui"
    config = ConfigLoader()
    assert config.validate(arg_type, arg_val) == 'false'

def test_pass_bad_environment_arg_to_config_loader():
    '''config_loader should raise an exception when a bad cli arg is passed'''
    arg_type = "environments"
    arg_val = "BADARGUMENT"
    config = ConfigLoader()
    with pytest.raises(KeyError) as ke:
        config.validate(arg_type, arg_val)
        assert KeyError in str(ke.value)

def test_pass_good_project_arg_to_config_loader():
    '''config_loader should return 'true' when a good cli arg and active project is passed'''
    arg_type = "environments"
    arg_val = "dev"
    config = ConfigLoader()
    assert config.validate(arg_type, arg_val) == 'dev'

def test_pass_bad_platform_arg_to_config_loader():
    '''config_loader should raise an exception when a bad cli arg is passed'''
    arg_type = "platforms"
    arg_val = "BADARGUMENT"
    config = ConfigLoader()
    with pytest.raises(KeyError) as ke:
        config.validate(arg_type, arg_val)
        assert KeyError in str(ke.value)

def test_pass_good_project_arg_to_config_loader():
    '''config_loader should return 'true' when a good cli arg and active project is passed'''
    arg_type = "platforms"
    arg_val = "usa"
    config = ConfigLoader()
    assert config.validate(arg_type, arg_val) == 'usa'