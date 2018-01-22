


class PropertiesWriter():

  def __init__(self):
    print("PropertiesWriter()")

  def create_properties_file(self, all_kv):
    try:
      prop_file = open('application.properties', 'w')
      for key,value in all_kv.items():
        print("writing {0}={1}".format(key, value))
        line = "{0}={1}\n".format(key, value)
        prop_file.write(line)
    except:
      print("unexpected error writing to ./application.properties")
      raise
