#!/usr/bin/env python3
import os
import sys
import restart_ecs
import re


class Main():

  def __init__(self):
    print("Main()")

  def run(self, region):
    clustername = re.sub('deploy-', '', os.environ['JOB_NAME'])
    #ch = consul_handler.ConsulHandler()
    #region = ch.get_key("REGION")
    ecs = restart_ecs.RestartEcs()
    containerids = ecs.get_ecs_containers(clustername, region)
    ecs.restart_ecs_containers(clustername, containerids, region)


if __name__ == '__main__':
  main = Main()
  main.run(sys.argv[1])

