
import consul_kv


class ConsulHandler():

  _allkeys = None

  def __init__(self, profile):
    # example: curl -s http://consul.media.dev.usa.reachlocalservices.com:8500/v1/kv/tf_managed/media-gateway?keys
    #response = requests.get("http://consul.media.dev.usa.reachlocalservices.com:8500/v1/kv/tf_managed/media-gateway?keys")
    # this dictionary is a kludge until networking is sorted out for consul
    # see terraform-configurations/aws_core_services/consul
    endpoints = {
      'dev-usa': 'http://consul.media.dev.usa.reachlocalservices.com:8500/v1/',
      'qa-aus': 'http://consul.media.qa.aus.reachlocalservices.com:8500/v1/',
      'qa-can': 'http://consul.media.qa.can.reachlocalservices.com:8500/v1/',
      'qa-eur': 'http://consul.media.qa.eur.reachlocalservices.com:8500/v1/',
      'qa-gbr': 'http://consul.media.qa.gbr.reachlocalservices.com:8500/v1/',
      'qa-jpn': 'http://consul.media.qa.jpn.reachlocalservices.com:8500/v1/',
      'qa-usa': 'http://consul.media.qa.usa.reachlocalservices.com:8500/v1/',
      'prod-aus': 'https://consul-external.media.prod.aus.reachlocalservices.com/v1/',
      'prod-can': 'https://consul-external.media.prod.can.reachlocalservices.com/v1/',
      'prod-gbr': 'https://consul-external.media.prod.gbr.reachlocalservices.com/v1/',
      'prod-eur': 'https://consul-external.media.prod.eur.reachlocalservices.com/v1/',
      'prod-jpn': 'https://consul-external.media.prod.jpn.reachlocalservices.com/v1/',
      'prod-usa': 'https://consul-external.media.prod.usa.reachlocalservices.com/v1/'
      }
    self.conn = consul_kv.Connection(endpoint=endpoints[profile])

  def get_all_keys(self, project_name):
    print("getting all keys for: ", project_name)
    target_path = "tf_managed/{0}".format(project_name)
    allkeys = self.conn.get(target_path, recurse=True)
    return allkeys

  def get_common_keys(self, project_name):
    print("getting common keys for: ", project_name)
    target_path = "tf_managed/common"
    common_keys = self.conn.get(target_path, recurse=True)
    return common_keys

  def get_key(self, project, key):
    connection_path = "tf_managed/{0}/{1}".format(project, key)
    specific_kv = self.conn.get(connection_path)
    return specific_kv

  def __del__(self):
    pass
