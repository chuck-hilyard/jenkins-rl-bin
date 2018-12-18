#!/usr/bin/env python3

import json
import requests
import hvac
import os


class Vault():

  vault_url = "http://base-camp-vault.media.dev.usa.reachlocalservices.com:8200"

  def __init__(self, role_id):
    print("Vault()")
    self.role_id = role_id
    self.set_client_token()
    self.set_credentials()

  def set_credentials(self):
    path = "/v1/secret/data/jenkinsb"
    vault_url = "{}{}".format(Vault.vault_url, path)
    headers = { "X-Vault-Token": self.client_token }
    response = requests.get(vault_url, headers=headers)
    response_json = json.loads(response.text)
    self.username = response_json['data']['username']
    self.password = response_json['data']['password']

  def set_client_token(self):
    auth_payload = { "role_id": self.role_id }
    path = "/v1/auth/approle/login"
    vault_url = "{}{}".format(Vault.vault_url, path)
    response = requests.post(vault_url, data=json.dumps(auth_payload))
    response_json = json.loads(response.text)
    self.client_token = response_json['auth']['client_token']

