#!/usr/bin/env python3

import cmr_approval_gate
import jira_handler


class Main():

  def __init__(self):
    print("in Main()")
    cmr = cmr_approval_gate.CmrApprovalGate()
    cmr_number = cmr.get_cmr_number()
    build_url = cmr.get_build_url()

    jira = jira_handler.JiraHandler()
    jira_conn = jira.create_connection_handler()
    jira.find_approved_cmr(jira_conn, cmr_number)
    jira.add_comment_to_approved_cmr(build_url)


if __name__ == '__main__':
  main = Main()
