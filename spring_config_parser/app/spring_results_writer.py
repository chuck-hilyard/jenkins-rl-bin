
import abc


class SpringResultsWriter():

    def __init__(self, formatted_results):
        print("SpringResultsWriter.init")
        self._formatted_results = formatted_results

    def __del__(self):
        print("SpringResultsWriter.del")

    @abc.abstractmethod
    def write_formatted_results(self):
        print("in write_formatted_results spring_results_writer base class")