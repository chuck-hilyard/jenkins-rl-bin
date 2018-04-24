
from .spring_results_writer import SpringResultsWriter


class PropertiesKVWriter(SpringResultsWriter):

    def write_formatted_results(self):
        print("in write_formatted_results properties_consul_writer ")