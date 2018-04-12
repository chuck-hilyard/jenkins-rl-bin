#!/usr/bin/env python3

# curl http://config-server.media.dev.usa.reachlocalservices.com:8080/media-core-gateway/sandbox/usa
#

import argparse
import sys
import app.config_loader as config_loader


class Main():

  def __init__(self):
    print("Main.init\n")
    self.arg_parse()

  def __del__(self):
    print("Main.del\n")

  def arg_parse(self):
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=str, help="provide the github project name")
    parser.add_argument("environment", type=str, help="provide the environment (eg dev,qa,prod)")
    parser.add_argument("platform", type=str, help="provide the platform (eg aus,can,eur)")
    parser.parse_args()

  def validate_project_arg(self):
    project_val = sys.argv[1]
    config = config_loader.ConfigLoader()
    return config.validate("projects", project_val)


if __name__ == '__main__':
  main = Main()
  main.validate_project_arg()


