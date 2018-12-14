

import re
from jira import JIRA

class JiraHandler():

  def __init__(self):
    print("JiraHandler()")

  def create_connection(self, username, password):
    print("connecting to https://tickets.reachlocal.com")
    options = { 'server': 'https://tickets.reachlocal.com'}
    try:
      #if we decide to add comments to the tickets we'll need to auth
      jira_conn_authd = JIRA(options, basic_auth=(username, password))
      #jira_conn_authd = JIRA(options)
      return jira_conn_authd
    except:
      print("unexpected error, connection to jira failed")

  def find_approved_cmr(self, jira_conn, cmr_number):
    print("searching JIRA for {0}...".format(cmr_number))
    JQL = "project = CMR AND status = \"In Progress\" OR status = CAB-APPROVED  AND key = {0} AND component = Media".format(cmr_number)
    issue = jira_conn.search_issues(JQL)
    if len(issue) > 0:
      print("found CMR")
      return issue
    else:
      print("matching CMR not found, exiting")
      exit(1)

  def match_build_string_from_cmr(self, jira_conn, cmr_number, Job, BUILD_NUMBER):
    print("matching CMR to Jenkins BUILD")
    issue = jira_conn.issue(cmr_number)
    description = issue.fields.description
    #search_string = r"^BUILD:\shttps:\/\/\S*\/view\/\S*\/job\/{0}\/{1}".format(Job, BUILD_NUMBER)
    search_string = r"{0}.*{1}".format(Job, BUILD_NUMBER)
    match = re.search(search_string, description)
    if match is None:
      print("no matching BUILD: string found in {0}".format(cmr_number))
      print("quitting...")
      exit(1)

  def add_comment_to_approved_cmr(self, jira_conn, cmr_number, deploy_url):
    modified_deploy_url = re.sub('^http:\/\/[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\:8080', 'https://jenkins.media.dev.usa.reachlocalservices.com', deploy_url)
    print("adding comment to {0}".format(cmr_number))
    jira_conn.add_comment('CMR-2926', "DEPLOY URL: {0}".format(modified_deploy_url))

