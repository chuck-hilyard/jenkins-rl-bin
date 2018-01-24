
import consul_kv


class ConsulHandler():

  _allkeys = None

  def __init__(self):
    # example: curl -s http://consul.media.dev.usa.reachlocalservices.com:8500/v1/kv/tf_managed/media-gateway?keys
    #response = requests.get("http://consul.media.dev.usa.reachlocalservices.com:8500/v1/kv/tf_managed/media-gateway?keys")
    self.conn = consul_kv.Connection(endpoint='http://consul.media.dev.usa.reachlocalservices.com:8500/v1/')

  def get_all_keys(self):
    allkeys = self.conn.get('tf_managed/media-gateway', recurse=True)
    return allkeys

  def get_key(self, project, key):
    connection_path = "tf_managed/{0}/{1}".format(project, key)
    specific_kv = self.conn.get(connection_path)
    return specific_kv
