
import consul_kv

class Consul():

  def __init__(self):
    print("Consul()")

  def get_role_id(self):
    conn = consul_kv.Connection(endpoint="http://consul.media.dev.usa.reachlocalservices.com:8500/v1/")
    target_path = "base-camp-vault/config/role_id"
    try:
      raw_target_path = conn.get(target_path)
      role_id = raw_target_path['base-camp-vault/config/role_id']
      return role_id
    except:
      print("problem scraping consul role_id...ignoring")
      return None
