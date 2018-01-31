
import consul_kv


class ConsulHandler():

  _allkeys = None

  def __init__(self):
    # example: curl -s http://consul.media.dev.usa.reachlocalservices.com:8500/v1/kv/tf_managed/media-gateway?keys
    #response = requests.get("http://consul.media.dev.usa.reachlocalservices.com:8500/v1/kv/tf_managed/media-gateway?keys")
    # this dictionary is a kludge until networking is sorted out for consul
    # see terraform-configurations/aws_core_services/consul
    endpoints = {
      'dev-usa': 'http://consul.media.dev.usa.reachlocalservices.com:8500/v1/',
      'prod-gbr': 'https://consul-external.media.prod.gbr.reachlocalservices.com/v1/'
      }
    self.conn = consul_kv.Connection(endpoint=endpoints["prod-gbr"])

  def get_all_keys(self):
    allkeys = self.conn.get('tf_managed/media-gateway', recurse=True)
    return allkeys

  def get_key(self, project, key):
    connection_path = "tf_managed/{0}/{1}".format(project, key)
    specific_kv = self.conn.get(connection_path)
    return specific_kv
