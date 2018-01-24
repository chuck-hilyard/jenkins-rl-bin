
import boto3
import json
import re
import os

class RestartEcs():
  # the hammer
  def restart_ecs_containers(self, clustername, containerids, region):
    client = boto3.client('ecs')
    tasks = client.list_tasks(cluster=clustername)['taskArns']
    print("TASKS: ", tasks)
    for taskid in tasks:
      response = client.stop_task(cluster=clustername, task=taskid, reason="deploying software")
      print("response: ", response)

  def get_ecs_containers(self, clustername, region):
    client = boto3.client('ecs')
    containers = client.list_container_instances(cluster=clustername)['containerInstanceArns']
    if not containers:
      raise Exception("no containers found in ecs cluster {0}".format(clustername))
    else:
      return client.list_container_instances(cluster=clustername)['containerInstanceArns']

