
import json
import requests
import hvac
import os


class Vault():

  vault_url = "http://base-camp-vault.media.dev.usa.reachlocalservices.com:8200"

  def __init__(self, role_id, secret_id):
    print("Vault.init")
    self.role_id = role_id
    self.secret_id = secret_id
    self.vault_login()
    self.get_credentials()

  def get_credentials(self):
    print("Vault.get_credentials")
    path = "/v1/secret/data/jenkins"
    vault_url = "{}{}".format(Vault.vault_url, path)
    headers = { "X-Vault-Token": self.client_token }
    response = requests.get(vault_url, headers=headers)
    response_json = json.loads(response.text)
    self.username = response_json['data']['username']
    self.password = response_json['data']['password']

  def vault_login(self):
    print("Vault.login")
    auth_payload = { "role_id": self.role_id, "secret_id": self.secret_id }
    print("AUTH PAYLOAD: ", auth_payload)
    path = "/v1/auth/approle/login"
    vault_url = "{}{}".format(Vault.vault_url, path)
    response = requests.post(vault_url, data=json.dumps(auth_payload))
    response_json = json.loads(response.text)
    self.client_token = response_json['auth']['client_token']
