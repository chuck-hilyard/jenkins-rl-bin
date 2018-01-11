import json
import os
import jira

class CmrApprovalGate():

  def __init__(self):
    self.build_number  = os.environ['BUILD_NUMBER']
    self.build_id      = os.environ['BUILD_ID']
    self.build_url     = os.environ['BUILD_URL']
    self.job_name      = os.environ['JOB_NAME']
    self.job_base_name = os.environ['JOB_BASE_NAME']
    self.git_commit    = os.environ['GIT_COMMIT']

  def get_build_number(self):
    return self.build_number

  def output(self):
    print("build number: ", format(build_number))
    print("build id: ", format(build_id))
    print("job name: ", format(job_name))
    print("job base name: ", format(job_base_name))
    print("build url: ", format(build_url))
    print("git commit: ", format(git_commit))

