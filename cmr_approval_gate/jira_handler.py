
import re
from jira import JIRA

class JiraHandler():

  def __init__(self):
    print("in JiraHandler()")

  def create_connection(self, username, password):
    print("connecting to https://tickets.reachlocal.com as {0}".format(username))
    options = { 'server': 'https://tickets.reachlocal.com'}
    try:
      jira_conn_authd = JIRA(options, basic_auth=(username, password))
      return jira_conn_authd
    except JiraConnError:
      print("connection to jira failed")

  def find_approved_cmr(self, jira_conn, cmr_number):
    #JQL = "project = CMR AND status = CAB-APPROVED AND key = {0} AND component = Media".format(cmr_number)
    #testing
    JQL = "project = CMR AND status = RE-OPEN AND key = {0}".format(cmr_number)
    issue = jira_conn.search_issues(JQL)
    if len(issue) > 0:
      return issue
    else:
      exit(1)

  def match_build_string_from_cmr(self, jira_conn, build_string):
    # this is a matching build string
    # https://jenkins.media.dev.usa.reachlocalservices.com/view/madmin-client/job/madmin-client-build/68/
    # https://*/view/*/job/$Job/$BUILD_NUMBER
    # regex: ^https:\/\/\S*\/view\/\S*\/job\/%s\/%s % Job, BUILD_NUMBER
    print("matching CMR to Jenkins deploy")
    description = jira_conn.issue.fields.comment.comments
    print("test: ", description)


  def add_comment_to_approved_cmr(self, jira_conn, cmr_number, deploy_url):
    # modify deploy_url to reflect the jenkins VIP DNS name
    # modified_deploy_url = regex blah blah
    # switch this http://10.233.72.141:8080/job/madmin-client-deploy-dev-usa/62/
    # to
    # https://jenkins.media.dev.usa.reachlocalservices.com/view/madmin-client/job/madmin-client-deploy-dev-usa/62/
    # regex: ^http:\/\/[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\:8080
    modified_deploy_url = re.sub('^http:\/\/[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\:8080', 'https://jenkins.media.dev.usa.reachlocalservices.com', deploy_url)
    print("adding comment to {0}".format(cmr_number))
    jira_conn.add_comment('CMR-2926', "DEPLOY URL: {0}".format(modified_deploy_url))

