import json
import os
from jira import JIRA

class CmrApprovalGate():
  def __init__(self):
    self.build_number  = os.environ['BUILD_NUMBER']
    self.build_id      = os.environ['BUILD_ID']
    self.build_url     = os.environ['BUILD_URL']
    self.job_name      = os.environ['JOB_NAME']
    self.job_base_name = os.environ['JOB_BASE_NAME']
    self.git_commit    = os.environ['GIT_COMMIT']
    self.jira_cmr      = os.environ['JIRA_CMR']
    self.user          = os.environ['user']

  def get_build_number(self):
    return self.build_number

  def output(self):
    print("build number: ", format(self.build_number))
    print("build id: ", format(self.build_id))
    print("job name: ", format(self.job_name))
    print("job base name: ", format(self.job_base_name))
    print("build url: ", format(self.build_url))
    print("git commit: ", format(self.git_commit))
    print("jira_cmr: ", format(self.jira_cmr))
    print("user: ", format(self.user))


class Jira():
  def __init__(self):
    print("connecting to https://tickets.reachlocal.com")
    options = { 'server': 'https://tickets.reachlocal.com'}
    jira = JIRA(options)
    issue = jira.issue('CMR-2924')
