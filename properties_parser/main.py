#!/usr/bin/env python3

import key_formatter
import credentials_handler
import consul_handler
import properties_writer
import sys
import re
import os


class Main():

  def __init__(self):
    print("Main()")

  def run(self, region, profile):
    ch = consul_handler.ConsulHandler(profile)
    project = re.sub('-build', '', os.environ['Job'])
    raw_kv = ch.get_all_keys(project)

    pf = key_formatter.KeyFormatter()
    formatted_keys = pf.format_keys(raw_kv, project)

    pw = properties_writer.PropertiesWriter()
    pw.create_properties_file(formatted_keys)

    # future project (if we decide to add comments to the tickets)
    #credentials = credentials_handler.CredentialsHandler()
    #password = credentials.get_password()



if __name__ == '__main__':
  main = Main()
  main.run(sys.argv[1], sys.argv[2])
