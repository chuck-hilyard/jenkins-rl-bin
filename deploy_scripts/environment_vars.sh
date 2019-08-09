#!/bin/bash -x

PROJECT="$(echo ${Job} |sed 's/\-build//g')"
ENV_PLAT="$(echo ${JOB_NAME} |sed 's/'${PROJECT}'\-deploy\-//g')"
ENV_DOT_PLAT="$(echo ${ENV_PLAT} |sed 's/\-/\./g')"

keys=$(curl -s https://consul-jenkins.${ENV_DOT_PLAT}.media.reachlocalservices.com/v1/kv/${PROJECT}/config?recurse |jq '.[] | {key: .Key} | .[]'| sed 's/"//g')

VARS_FILE="${WORKSPACE}/deploy_environment_vars.txt"

echo "PROJECT=${PROJECT}" >> $VARS_FILE
for key in $keys
  do
    value=$(curl -s http://consul.${ENV_DOT_PLAT}.media.reachlocalservices.com:8500/v1/kv/${key}?raw)
    raw_key=$(echo ${key} |sed 's/'$PROJECT'\/config\///g')
    kv="${raw_key}=${value}"
    echo ${kv} >> $VARS_FILE
    ls -ld ${VARS_FILE}
  done

