#!/usr/bin/env python3

# curl example to create private key
# curl -k -v --header "X-Vault-Token:7da38c81-6bcb-7639-05cd-2f48b952ce13" --request POST --data @docker-build-jenkins-private-key.json https://10.233.136.68:8200/v1/secret/data/${env}/${platform}/cert/jenkins
# curl -k -v --header "X-Vault-Token:7da38c81-6bcb-7639-05cd-2f48b952ce13" --request DELETE https://10.233.136.68:8200/v1/secret/data/${env}/${platform}/cert/jenkins

import base64
import hvac
import json
import os
import requests
import sys
import difflib

VAULTKEY = os.environ['VAULTKEY']

def create(key_type):
  headers = {'X-Vault-Token': VAULTKEY }
  url     = "https://10.233.136.68:8200/v1/secret/data/{env}/{platform}/{key_type}/jenkins".format(env=environment, platform=platform, key_type=key_type)
  file = open('jenkins-agent-private-key.pem', 'r')
  string = file.read()
  json_formatted = json.dumps( { 'key': string } )
  response = requests.post(url, headers=headers, data=json_formatted, verify=False)
  print(response.status_code)

def get(key_type):
  headers = {'X-Vault-Token': VAULTKEY }
  url     = "https://10.233.136.68:8200/v1/secret/data/{env}/{platform}/{key_type}/jenkins".format(env=environment, platform=platform, key_type=key_type)
  response = requests.get(url, headers=headers, verify=False)
  jsonstr = json.loads(response.text)
  string = jsonstr['data']['key']
  print(string)
  fw = open('id_rsa', 'w')
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
  main(action, key_type)
