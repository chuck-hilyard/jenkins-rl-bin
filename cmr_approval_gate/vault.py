#!/usr/bin/env python3

#import json
#import requests
#import sys
import hvac
import os


class Vault():

  role_id = os.environ['role_id']
  vault_url = "http://base-camp-vault.media.dev.usa.reachlocalservices.com:8200"

  def __init__(self):
    self.client = hvac.Client(url=vault_url)

  def create(self):
    pass

  def get(self):
    pass

  def delete(self):
    pass
