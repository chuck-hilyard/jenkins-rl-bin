#!/usr/bin/env python3

#
# curl http://config-server.media.dev.usa.reachlocalservices.com:8080/media-core-gateway/sandbox/usa
#

import argparse



class Main():

  def __init__(self):
    print("Main.init {}".format(__name__))

  def __del__(self):
    pass

  def validate_args(self, **kwargs):
    parser = argparse.ArgumentParser()
    parser.parse_args()

if __name__ == '__main__':
  main = Main()
