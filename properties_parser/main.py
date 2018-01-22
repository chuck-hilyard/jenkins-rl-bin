#!/usr/bin/env python3

import properties_parser
import credentials_handler
import consul_handler
import properties_writer


class Main():

  def __init__(self):
    print("Main()")

  def run(self):
    aph = properties_parser.PropertiesParser()
    ch = consul_handler.ConsulHandler()
    all_kv = ch.get_all_keys()
    pw = properties_writer.PropertiesWriter()
    pw.create_properties_file(all_kv)
    try:
      prop_file = open('application.properties', 'w')
      for key,value in all_kv.items():
        print("writing {0}={1}".format(key, value))
        line = "{0}={1}\n".format(key, value)
        prop_file.write(line)
    except:
      print("unexpected error writing to ./application.properties")
      raise

    # future project (if we decide to add comments to the tickets)
    #credentials = credentials_handler.CredentialsHandler()
    #password = credentials.get_password()
    username = 'anonymous'
    password = 'anonymous'



if __name__ == '__main__':
  main = Main()
  main.run()
