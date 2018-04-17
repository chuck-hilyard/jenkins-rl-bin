

import json
import re

# formats the spring query results into the desired format (set in config.ini)
# this should eventually be a base class

class SpringResultsFormatter():

    def __init__(self, results, output_type):
        print("SpringResultsFormatter.init")
        if output_type == 'consul':
            print("output type is consul")
            formatted_results = "output type is consul"
        elif output_type == 'properties_kv':
            print("output type is properties_kv")
            self.formatted_results = self.properties_kv(results)
        elif output_type == 'spring_native':
            print("output type is spring_native")
            self.formatted_results = self.spring_native(results)
        else:
            formatted_results = "something went srsly wrong"

    def __del__(self):
        print("SpringResultsFormatter.del")

    def properties_kv(self, results):
        json_formatted_results = json.loads(results)
        str_formatted_results = json.dumps(json_formatted_results["propertySources"][0]["source"], sort_keys=True, indent=0, separators=('', '='))
        #TODO - anything except the below
        firstreplace = re.sub('\"', '', str_formatted_results)
        secondreplace = re.sub('\{', '', firstreplace)
        lastreplace = re.sub('\}', '', secondreplace)
        return lastreplace

    def consul(self, results):
        print("doing consul stuff")

    def spring_native(self, results):
        json_formatted_results = json.loads(results)
        print("writing only to stdout:\n", json.dumps(json_formatted_results, sort_keys=True, indent=2, separators=('', '=')))
        return None

