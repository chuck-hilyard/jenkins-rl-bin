#!/bin/bash -x

PROJECT="$(echo ${Job} |sed 's/\-build//g')"
ENV_PLAT="$(echo ${JOB_NAME} |sed 's/'${PROJECT}'\-deploy\-//g')"
ENV_DOT_PLAT="$(echo ${ENV_PLAT} |sed 's/\-/\./g')"

VARS_FILE="${WORKSPACE}/source_build_vars.txt"

while read line in 
  do 
    key=$(echo ${line} |cut -f1 -d=)
    value=$(echo ${line} |cut -f2 -d=)
    $(curl -s https://consul-jenkins.${ENV_DOT_PLAT}.media.reachlocalservices.com/v1/kv/${PROJECT}/configs/${key} --data "$(echo $value)")
  done <$(echo ${VARS_FILE})

