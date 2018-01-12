import json
import os

class CmrApprovalGate():

  def __init__(self):
    self.build_display_name = os.environ['BUILD_DISPLAY_NAME']
    self.build_number       = os.environ['BUILD_NUMBER']
    self.run_display_url    = os.environ['RUN_DISPLAY_URL']
    self.job_name           = os.environ['JOB_NAME']
    self.jira_cmr           = os.environ['JIRA_CMR']

  def get_build_number(self):
    return self.build_number

  def get_cmr_number(self):
    return self.jira_cmr

  def output(self):
    print("build display name: ", format(self.build_display_name))
    print("build number: ", format(self.build_number))
    print("run display url: ", format(self.run_display_url))
    print("job name: ", format(self.job_name))
    print("jira_cmr: ", format(self.jira_cmr))

