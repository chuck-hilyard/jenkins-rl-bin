
from .spring_results_writer import SpringResultsWriter


class PropertiesKVWriter(SpringResultsWriter):

    def __init__(self, formatted_results):
        print("PropertiesKVWriter.init")
        self.formatted_results = formatted_results
        self.write_formatted_results()

    def __del__(self):
        print("PropertiesKVWriter.del")


    def write_formatted_results(self):
        print("in write_formatted_results properties_kv_writer ")
        print("writing to file: ", self.formatted_results)


