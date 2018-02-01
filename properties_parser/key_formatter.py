
import re

class KeyFormatter():

  def __init__(self):
    print("PropertiesParser()")

  def format_keys(self, raw_kv, project_name):
    raw_key_dictionary = {}
    for raw_key,raw_value in raw_kv.items():
      regex_string = "^tf_managed\/{0}\/".format(project_name)
      new_key = re.sub(regex_string, '', raw_key)
      raw_key_dictionary[new_key] = raw_value
    return raw_key_dictionary
