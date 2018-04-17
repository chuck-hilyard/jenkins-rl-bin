#!/usr/bin/env python3


import argparse
import app.config_loader as config_loader
import app.spring_reader as spring_reader
import app.spring_results_formatter as spring_results_formatter
import app.property_writer as property_writer


class Main():

  def __init__(self):
      print("Main.init\n")
      self.arg_parse()

  def __del__(self):
      print("Main.del\n")

  def arg_parse(self):
      parser = argparse.ArgumentParser()
      parser.add_argument("project", type=str, help="provide the github project name")
      parser.add_argument("environment", type=str, help="provide the environment (eg dev,qa,prod)")
      parser.add_argument("platform", type=str, help="provide the platform (eg aus,can,eur)")
      parser.parse_args()


if __name__ == '__main__':
    main = Main()
    config = config_loader.ConfigLoader()
    spring_reader = spring_reader.SpringReader(config)
    formatted_results = spring_results_formatter.SpringResultsFormatter(spring_reader.results, config.output_type)
    property_writer.PropertyWriter(formatted_results.formatted_results)

