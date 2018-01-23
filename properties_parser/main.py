#!/usr/bin/env python3

import key_formatter
import credentials_handler
import consul_handler
import properties_writer


class Main():

  def __init__(self):
    print("Main()")

  def run(self):
    ch = consul_handler.ConsulHandler()
    raw_kv = ch.get_all_keys()

    pf = key_formatter.KeyFormatter()
    formatted_keys = pf.format_keys(raw_kv)

    pw = properties_writer.PropertiesWriter()
    pw.create_properties_file(formatted_keys)

    # future project (if we decide to add comments to the tickets)
    #credentials = credentials_handler.CredentialsHandler()
    #password = credentials.get_password()



if __name__ == '__main__':
  main = Main()
  main.run()
