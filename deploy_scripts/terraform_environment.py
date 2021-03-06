#!/usr/bin/env python3

import argparse
import requests
import json
import re
import os
import sys

def get_config_from_consul():
  if SUBDOMAIN:
    url = "https://consul-jenkins.{}.{}.{}.media.reachlocalservices.com/v1/kv/{}/config?recurse".format(SUBDOMAIN, ENVIRONMENT, PLATFORM, PROJECT)
  else:
    url = "https://consul-jenkins.{}.{}.media.reachlocalservices.com/v1/kv/{}/config?recurse".format(ENVIRONMENT, PLATFORM, PROJECT)
  try:
    response = requests.get(url, timeout=5.0)
  except:
    #print("an exception occurred: ", sys.exc_info()[0])
    raise
    sys.exit(1)
  if response.status_code == 200:
    return response.json()
  else:
    print(response.raise_for_status())
    sys.exit(1)

def get_raw_value_from_consul(key):
  if SUBDOMAIN:
    url = "https://consul-jenkins.{}.{}.{}.media.reachlocalservices.com/v1/kv/{}/config/{}?raw".format(SUBDOMAIN, ENVIRONMENT, PLATFORM, PROJECT, key)
  else:
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
  parser.add_argument("--subdomain", help="e.g. \"admctr2\"")
  parser.add_argument("ENVIRONMENT", help="e.g. \"dev\"")
  parser.add_argument("PLATFORM", help="e.g. \"usa\"")
  args = parser.parse_args()
  global PROJECT
  global SUBDOMAIN
  global ENVIRONMENT
  global PLATFORM
  SUBDOMAIN = args.subdomain
  PROJECT = args.PROJECT
  ENVIRONMENT = args.ENVIRONMENT
  PLATFORM = args.PLATFORM

def json_cleanup(json_response):
  kv = {}
  for index in json_response:
    key_raw = index['Key']
    key = key_raw.rsplit(sep='/', maxsplit=1)[1]
    # values in consul are encrypted in a recursive call, each value must be called individually to get raw values
    value = get_raw_value_from_consul(key)
    kv[key] = value
  return kv

def write_env_file(kv):
  envfile = open('deploy_environment_vars.txt', 'w')
  envfile.write("PROJECT={}\n".format(PROJECT))
  for k,v in kv.items():
    envfile.write("{}={}\n".format(k,v))
  envfile.close()


def main():
  validate_args()
  json_response = get_config_from_consul()
  kv = json_cleanup(json_response)
  write_env_file(kv)

if __name__ == '__main__':
  main()
