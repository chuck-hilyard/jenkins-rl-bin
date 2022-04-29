
import consul_kv

class Consul():

  def __init__(self):
    print("Consul()")

  def get_role_id(self):
    #TODO: delete this after 06/2022
    #conn = consul_kv.Connection(endpoint="http://consul.media.dev.usa.reachlocalservices.com:8500/v1/")
    conn = consul_kv.Connection(endpoint="https://consul.dev.usa.media.reachlocalservices.com/v1/")
    target_path = "jenkins-rl-bin/config/role_id"
    try:
      raw_target_path = conn.get(target_path)
      role_id = raw_target_path['jenkins-rl-bin/config/role_id']
      return role_id
    except:
      print("problem scraping consul role_id...ignoring")
      return None

  def get_secret_id(self):
    #TODO: delete this after 06/2022
    #conn = consul_kv.Connection(endpoint="http://consul.media.dev.usa.reachlocalservices.com:8500/v1/")
    conn = consul_kv.Connection(endpoint="https://consul.dev.usa.media.reachlocalservices.com/v1/")
    target_path = "jenkins-rl-bin/config/secret_id"
    try:
      raw_target_path = conn.get(target_path)
      secret_id = raw_target_path['jenkins-rl-bin/config/secret_id']
      return secret_id
    except:
      print("problem scraping consul secret_id...ignoring")
      return None
