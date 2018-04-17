
# curl http://config-server.media.dev.usa.reachlocalservices.com:8080/media-core-gateway/sandbox/usa

import requests


class SpringReader():

    def __open_connection(self, url):
        results = self.__connection = requests.get(url)
        print("status_code: ", results.status_code)
        self.results = results.text

    def __init__(self, config):
        print("SpringReader.init")
        path = "/{}/{}/{}".format(config.project, config.environment, config.platform)
        self.__spring_endpoint = "{}{}".format(config.url, path)
        self.__connection = self.__open_connection(self.__spring_endpoint)

    def __del__(self):
        print("SpringReader.del")
