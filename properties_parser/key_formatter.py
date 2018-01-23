
import re

class KeyFormatter():

  def __init__(self):
    print("PropertiesParser()")

  def format_keys(self, raw_kv):
    raw_key_dictionary = {}
    for raw_key,raw_value in raw_kv.items():
      regex_string = "^tf_managed\/media-gateway\/"
      new_key = re.sub(regex_string, '', raw_key)
      raw_key_dictionary[new_key] = raw_value
    return raw_key_dictionary
