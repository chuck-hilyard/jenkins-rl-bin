
from jira import JIRA

class JiraHandler():

  def __init__(self):
    print("in JiraHandler()")

  def create_connection_handler(self):
    print("connecting to https://tickets.reachlocal.com")
    options = { 'server': 'https://tickets.reachlocal.com'}
    return JIRA(options)

  def find_approved_cmr(self, jira_conn, cmr_number):
    JQL = "project = CMR AND status = CAB-APPROVED AND key = {0} AND component = Media".format(cmr_number)
    issue = jira_conn.search_issues(JQL)
    print("issue: ", issue)

  def add_comment_to_approved_cmr(self, jira_conn, cmr_number, build_url):
    print("adding comment to {0}".format(cmr_number))
    jira_conn.add_comment(cmr_number, build_url)

