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

  # these should be positional args handled by argparse, another time
  # the positons are as follows
  # 1 - aws region (eg "us-west-2")
  # 2 - environment-platform (eg "dev-usa")
  # 3 - which keys from consul: all, common or config
  #   all    - both common and config keys
  #   common - only common keys from consul
  #   config - only project specific configuration keys
  def run(self, args):
    profile = args[2]
    ch = consul_handler.ConsulHandler(profile)
    project = re.sub('-build', '', os.environ['Job'])
    raw_kv = ch.get_all_keys(project)
    common_keys = ch.get_common_keys(project)

    pf = key_formatter.KeyFormatter()
    formatted_keys = pf.format_keys(raw_kv, project)
    formatted_common_keys = pf.format_common_keys(common_keys)

    pw = properties_writer.PropertiesWriter()

    if args[3] == 'config':
      pw.create_properties_file(formatted_keys)
    elif args[3] == 'common':
      pass
    else:
      pw.create_properties_file(formatted_keys)
      pw.append_properties_file(formatted_common_keys)


    # future project (if we decide to add comments to the tickets)
    #credentials = credentials_handler.CredentialsHandler()
    #password = credentials.get_password()



if __name__ == '__main__':
  main = Main()
  main.run(sys.argv)
