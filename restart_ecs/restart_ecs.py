
import boto3
import json
import re
import os

class RestartEcs():

  def __init__(self):
    print("RestartEcs()")

  # the hammer
  def restart_ecs_containers(self, clustername, containerids, region, profile):
    session = boto3.Session(profile_name=profile)
    client = session.client('ecs', region_name=region)
    tasks = client.list_tasks(cluster=clustername)['taskArns']
    print("TASKS: ", tasks)
    for taskid in tasks:
      response = client.stop_task(cluster=clustername, task=taskid, reason="deploying software")
      print("response: ", response)

  def get_ecs_containers(self, clustername, region, profile):
    session = boto3.Session(profile_name=profile)
    client = session.client('ecs', region_name=region)
    containers = client.list_container_instances(cluster=clustername)['containerInstanceArns']
    if not containers:
      raise Exception("no containers found in ecs cluster {0}".format(clustername))
    else:
      return client.list_container_instances(cluster=clustername)['containerInstanceArns']

