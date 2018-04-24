# formats the spring query results into the desired format (set in config.ini)

import json
import re


class SpringResultsFormatter():

    def __init__(self, results, output_type):
        print("SpringResultsFormatter.init")
        self.results = results
        self.output_type = output_type

    def __del__(self):
        print("SpringResultsFormatter.del")

    def run(self):
        if self.output_type == 'consul':
            print("output type is consul")
            formatted_results = "output type is consul"
        elif self.output_type == 'properties_kv':
            print("output type is properties_kv")
            self.formatted_results = self.properties_kv()
            return self.formatted_results
        elif self.output_type == 'spring_native':
            print("output type is spring_native")
            self.formatted_results = self.spring_native()
        else:
            formatted_results = "something went srsly wrong"

    def properties_kv(self):
        json_formatted_results = json.loads(self.results)
        str_formatted_results = json.dumps(json_formatted_results["propertySources"][0]["source"], sort_keys=True, indent=0, separators=('', '='))
        #TODO - anything other than what's below
        firstreplace = re.sub('\"', '', str_formatted_results)
        secondreplace = re.sub('\{', '', firstreplace)
        lastreplace = re.sub('\}', '', secondreplace)
        return lastreplace

    def consul(self):
        print("doing consul stuff")

    def spring_native(self):
        print("SPRING_NATIVE APPS DON'T USE THIS TOOL")
        return None

