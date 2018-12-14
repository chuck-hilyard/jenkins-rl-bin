
import json
import os
import xml.etree.ElementTree as et

class CmrApprovalGate():

  def __init__(self):
    print("CmrApprovalGate()")
    self.build_display_name = os.environ['BUILD_DISPLAY_NAME']
    print("**************************** CHANGE ME  BUILD_NUMBER_XML**********")
    self.build_number_xml   = et.fromstring(os.environ['BuildSelection'])
    #self.build_number_xml   = os.environ['BuildSelection']
    print("**************************** CHANGE ME BUILD_NUMBER**********")
    self.build_number       = self.build_number_xml[0].text
    #self.build_number       = self.build_number_xml
    self.deploy_url         = os.environ['BUILD_URL']
    self.run_display_url    = os.environ['RUN_DISPLAY_URL']
    self.job_name           = os.environ['JOB_NAME']
    self.jira_cmr           = os.environ['JIRA_CMR']
    self.job                = os.environ['Job']

  def get_deploy_url(self):
    return self.deploy_url

  def get_cmr_number(self):
    return self.jira_cmr

  def output(self):
    print("build display name: ", format(self.build_display_name))
    print("build number: ", format(self.build_number))
    print("run display url: ", format(self.run_display_url))
    print("job name: ", format(self.job_name))
    print("jira_cmr: ", format(self.jira_cmr))
