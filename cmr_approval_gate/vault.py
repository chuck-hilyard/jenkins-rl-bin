#!/usr/bin/env python3

import json
import requests
import hvac
import os


class Vault():

  #role_id = os.environ['role_id']
  #secret_id = os.environ['secret_id']
  #role_id = "8b033c01-db63-5d3d-f247-29e034ecca0f"
  #secret_id = "951d465d-3596-1286-b691-ef8ac9f0d4f4"
  role_id = "b079f35b-4427-c676-7956-b44437d31a0d"
  secret_id = "4d9f10bd-b62c-be6f-a55e-35b42b2f908d"
  vault_url = "http://base-camp-vault.media.dev.usa.reachlocalservices.com:8200"

  def __init__(self):
    print("Vault()")
    self.client = hvac.Client(url=Vault.vault_url)
    self.set_client_token()
    self.set_credentials()

  def set_credentials(self):
    path = "/v1/secret/data/jenkins"
    vault_url = "{}{}".format(Vault.vault_url, path)
    headers = { "X-Vault-Token": self.client_token }
    response = requests.get(vault_url, headers=headers)
    response_json = json.loads(response.text)
    self.username = response_json['data']['username']
    self.password = response_json['data']['password']

  def set_client_token(self):
    auth_payload = { "role_id": Vault.role_id, "secret_id": Vault.secret_id }
    path = "/v1/auth/approle/login"
    vault_url = "{}{}".format(Vault.vault_url, path)
    response = requests.post(vault_url, data=json.dumps(auth_payload))
    response_json = json.loads(response.text)
    self.client_token = response_json['auth']['client_token']

