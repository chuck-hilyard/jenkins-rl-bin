#!/usr/bin/env python3

import application_properties_parser
import credentials_handler


class Main():

  def __init__(self):
    print("Main()")
    cmr = cmr_approval_gate.CmrApprovalGate()
    cmr_number = cmr.get_cmr_number()
    Job = cmr.job
    BUILD_NUMBER = cmr.build_number
    cmr.output()
    deploy_url = cmr.get_deploy_url()

    # future project (if we decide to add comments to the tickets)
    #credentials = credentials_handler.CredentialsHandler()
    #password = credentials.get_password()
    username = 'anonymous'
    password = 'anonymous'

    jira = jira_handler.JiraHandler()
    jira_conn = jira.create_connection(username, password)
    jira.find_approved_cmr(jira_conn, cmr_number)
    jira.match_build_string_from_cmr(jira_conn, cmr_number, Job, BUILD_NUMBER)
    #jira.add_comment_to_approved_cmr(jira_conn, cmr_number, deploy_url)


if __name__ == '__main__':
  main = Main()
