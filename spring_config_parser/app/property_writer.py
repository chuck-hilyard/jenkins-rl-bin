


class PropertyWriter():

    def __init__(self, app_config):
        print("PropertyWriter.init")
        self.app_config = app_config

    def __del__(self):
        print("PropertyWriter.del")
