#!/usr/bin/env python3

import argparse
import requests
import json
import re
import os

def get_config_from_consul():
  url = "https://consul-jenkins.{}.{}.media.reachlocalservices.com/v1/kv/{}/config?recurse".format(ENVIRONMENT, PLATFORM, PROJECT)
  response = requests.get(url, timeout=5.0)
  if response.status_code == 200:
    return response.json()
  else:
    print(response.raise_for_status())
    sys.exit()

def get_raw_value_from_consul(key):
  url = "https://consul-jenkins.{}.{}.media.reachlocalservices.com/v1/kv/{}/config/{}?raw".format(ENVIRONMENT, PLATFORM, PROJECT, key)
  response = requests.get(url, timeout=5.0)
  if response.status_code == 200:
    return response.text
  else:
    print("something happened while retrieving k/v: {}".format(response.text))
    return None


def validate_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("PROJECT", help="e.g. \"google-mc-connector\"")
  parser.add_argument("ENVIRONMENT", help="e.g. \"dev\"")
  parser.add_argument("PLATFORM", help="e.g. \"usa\"")
  args = parser.parse_args()
  global PROJECT
  global ENVIRONMENT
  global PLATFORM
  PROJECT = args.PROJECT
  ENVIRONMENT = args.ENVIRONMENT
  PLATFORM = args.PLATFORM

def json_cleanup(json_response):
  for index in json_response:
    key_raw = index['Key']
    key = key_raw.rsplit(sep='/', maxsplit=1)[1]
    # values in consul are encrypted in a recursive call must be called individually to get raw values
    value = get_raw_value_from_consul(key)
    #print("k:{} v:{}".format(key, value))
    os.environ[key] = value



def main():
  validate_args()
  json_response = get_config_from_consul()
  json_cleanup(json_response)

if __name__ == '__main__':
  main()