#!/usr/bin/env python3


import consul_kv


def main():
  TESTJSON = [{"LockIndex":0,"Key":"prometheus-alertmanager/config/AWS_ACCOUNT_NUMBER","Flags":0,"Value":"NzYyODU4MzM2Njk4","CreateIndex":2301,"ModifyIndex":9948},{"LockIndex":0,"Key":"prometheus-alertmanager/config/ENVIRONMENT","Flags":0,"Value":"ZGV2","CreateIndex":2303,"ModifyIndex":9954},{"LockIndex":0,"Key":"prometheus-alertmanager/config/FQDN","Flags":0,"Value":"Y2hpbHlhcmQuZGV2LnVzYS5tZWRpYS5yZWFjaGxvY2Fsc2VydmljZXMuY29t","CreateIndex":2297,"ModifyIndex":9953},{"LockIndex":0,"Key":"prometheus-alertmanager/config/PLATFORM","Flags":0,"Value":"dXNh","CreateIndex":2300,"ModifyIndex":9950},{"LockIndex":0,"Key":"prometheus-alertmanager/config/REGION","Flags":0,"Value":"dXMtd2VzdC0y","CreateIndex":2305,"ModifyIndex":9949},{"LockIndex":0,"Key":"prometheus-alertmanager/config/branch","Flags":0,"Value":"bWFzdGVy","CreateIndex":2299,"ModifyIndex":9952},{"LockIndex":0,"Key":"prometheus-alertmanager/config/ecr_image_digest","Flags":0,"Value":"c2hhMjU2Ojc1MWE5MmFiNWJiYmU5NTMzMmRkNTg2MGFlYzE2MzEzZjI1MmRkYTFhZjljOTRhMTcyMjQzZmIyYjk0ZGYzNjg=","CreateIndex":10016,"ModifyIndex":10016},{"LockIndex":0,"Key":"prometheus-alertmanager/config/ecr_repo","Flags":0,"Value":"cHJvbWV0aGV1cy1hbGVydG1hbmFnZXItY2hpbHlhcmQtZGV2LXVzYS1tZWRpYS1yZWFjaGxvY2Fsc2VydmljZXMtY29t","CreateIndex":2304,"ModifyIndex":9951},{"LockIndex":0,"Key":"prometheus-alertmanager/config/ecs_cluster","Flags":0,"Value":"YXJuOmF3czplY3M6dXMtd2VzdC0yOjc2Mjg1ODMzNjY5ODpjbHVzdGVyL2FwcC1jbHVzdGVyLTAwLWNoaWx5YXJkLWRldi11c2EtbWVkaWEtcmVhY2hsb2NhbHNlcnZpY2VzLWNvbQ==","CreateIndex":2302,"ModifyIndex":9957},{"LockIndex":0,"Key":"prometheus-alertmanager/config/environment","Flags":0,"Value":"ZGV2","CreateIndex":2306,"ModifyIndex":9955},{"LockIndex":0,"Key":"prometheus-alertmanager/config/github_repo","Flags":0,"Value":"Z2l0QGdpdGh1Yi5jb206Y2h1Y2staGlseWFyZC9kb2NrZXItcHJvbWV0aGV1cy1hbGVydG1hbmFnZXIuZ2l0","CreateIndex":2298,"ModifyIndex":9956}]
  return TESTJSON

if __name__ == '__main__':
  TEST = main()
  print(TEST)
