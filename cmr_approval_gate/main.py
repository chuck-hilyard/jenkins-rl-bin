#!/usr/bin/env python3

import cmr_approval_gate
import jira_handler
import credentials_handler
import vault
import consul


class Main():

  def __init__(self):
    print("Main()")
    cmr = cmr_approval_gate.CmrApprovalGate()
    cmr_number = cmr.get_cmr_number()
    Job = cmr.job
    BUILD_NUMBER = cmr.build_number
    cmr.output()
    deploy_url = cmr.get_deploy_url()

    cnsl = consul.Consul()
    role_id = cnsl.get_role_id()

    vlt = vault.Vault(role_id)
    username = vlt.username
    password = vlt.password

    jira = jira_handler.JiraHandler()
    jira_conn = jira.create_connection(username, password)
    jira.find_approved_cmr(jira_conn, cmr_number)
    jira.match_build_string_from_cmr(jira_conn, cmr_number, Job, BUILD_NUMBER)
    #jira.add_comment_to_approved_cmr(jira_conn, cmr_number, deploy_url)


if __name__ == '__main__':
  main = Main()
