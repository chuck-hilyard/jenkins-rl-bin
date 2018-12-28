#!/usr/bin/env python3

# create/delete keys in our vault install

import json
import os
import requests
import sys
import urllib3

VAULTKEY = os.environ['VAULTKEY']

def create(key_type):
  headers = {'X-Vault-Token': VAULTKEY }
  url     = "http://base-camp-vault.media.dev.usa.reachlocalservices.com:8200/v1/secret/data/{env}/{platform}/{key_type}/{unique_name}".format(env=environment, platform=platform, key_type=key_type, unique_name=unique_name)
  file = open(thefile, 'r')
  string = file.read()
  json_formatted = json.dumps( { 'key': string } )
  response = requests.post(url, headers=headers, data=json_formatted, verify=False)
  print(response.status_code)

def get(key_type):
  urllib3.disable_warnings()
  headers = {'X-Vault-Token': VAULTKEY }
  url     = "http://base-camp-vault.media.dev.usa.reachlocalservices.com:8200/v1/secret/data/{env}/{platform}/{key_type}/{unique_name}".format(env=environment, platform=platform, key_type=key_type, unique_name=unique_name)
  response = requests.get(url, headers=headers, verify=False)
  jsonstr = json.loads(response.text)
  string = jsonstr['data']['key']
  fw = open(thefile, 'w')
  fw.write(string)
  fw.close()

def delete(key_type):
  pass

def main(action, filename):
  if action == 'create':
    create(key_type)
  if action == 'delete':
    delete(key_type)
  if action == 'get':
    get(key_type)


if __name__ == '__main__':
  action      = sys.argv[1] # { create, delete, get }
  key_type    = sys.argv[2] # { cert, aws, pem }
  environment = sys.argv[3] # { dev, qa, stg, prod }
  platform    = sys.argv[4] # { aus, can, eur, gbr, jpn, usa }
  thefile     = sys.argv[5] # (absolute or relative path) used as a source or destination (depends on action)
  unique_name = sys.argv[6] # e.g. "jenkins-master-private-key"
  main(action, key_type)
