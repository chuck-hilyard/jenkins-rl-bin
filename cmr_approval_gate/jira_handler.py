
from jira import JIRA

class JiraHandler():

  def __init__(self):
    print("in JiraHandler()")

  def create_connection_handler(self, username, password):
    print("connecting to https://tickets.reachlocal.com" as {0}.format(username))
    options = { 'server': 'https://tickets.reachlocal.com'}
    try:
      jira_conn_authd = JIRA(options, basic_auth=(username, password))
    return jira_conn_authd

  def find_approved_cmr(self, jira_conn, cmr_number):
    JQL = "project = CMR AND status = CAB-APPROVED AND key = {0} AND component = Media".format(cmr_number)
    issue = jira_conn.search_issues(JQL)
    print("issue: ", issue)

  # requires credentials
  def match_build_string_from_cmr(self, jira_conn, build_string):
    print("matching build string from CMR to Jenkins deploy")

  # requires credentials
  def add_comment_to_approved_cmr(self, jira_conn, cmr_number, build_url):
    print("adding comment to {0}".format(cmr_number))
    jira_conn.add_comment('CMR-2926', build_url)

