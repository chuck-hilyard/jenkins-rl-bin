#!/usr/bin/env python3

#
# curl http://config-server.media.dev.usa.reachlocalservices.com:8080/media-core-gateway/sandbox/usa
#

import argparse



class Main():

  def __init__(self):
    print("Main.init")

  def __del__(self):
    pass

  def validate_args(self):
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=str, help="provide the github project name")
    parser.add_argument("environment", type=str, help="provide the environment (eg dev,qa,prod)")
    parser.add_argument("platform", type=str, help="provide the platform (eg aus,can,eur)")
    return parser.parse_args()



if __name__ == '__main__':
  main = Main()


