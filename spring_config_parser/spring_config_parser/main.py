#!/usr/bin/env python3

#
# curl http://config-server.media.dev.usa.reachlocalservices.com:8080/media-core-gateway/sandbox/usa
#

import argparse
import sys



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
    project = sys.argv[1]
    state = False
    # load available projects from a config_loader
    # compare the user supplied project value to those in the config_loader
    return state


if __name__ == '__main__':
  main = Main()

