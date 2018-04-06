
import pytest
import sys
from spring_config_parser import main



def test_pass_no_cli_args():
  '''ensure we get a help message when no args are passed'''
  with pytest.raises(SystemExit) as e:
    main2 = main.Main()
    assert e.type == SystemExit
    assert e.value == 2

def test_pass_bad_cli_args():
  '''pass a bad arg get the default help message'''
  with pytest.raises(SystemExit) as e:
    sys.argv[1] = "-BADARG"
    main2 = main.Main()
    assert e.type == SystemExit
    assert e.value == 2


def test_validate_arg_syntax():
  '''ensure the args passed are syntactically correct'''
  sys.argv.remove('-BADARG')
  sys.argv.append('project')
  sys.argv.append('environment')
  sys.argv.append('platform')
  main2 = main.Main()
  assert main2.validate_project_arg() == True
