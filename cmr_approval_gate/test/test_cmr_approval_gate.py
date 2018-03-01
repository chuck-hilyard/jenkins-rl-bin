
import unittest
from ..cmr_approval_gate import cmr_approval_gate
import os

class TestCmrApprovalGate(unittest.TestCase):

  def setUp(self):
    self.cmr = cmr_approval_gate.CmrApprovalGate()
    os.putenv('BUILD_NUMBER', '62')
    os.putenv('BUILD_ID', '62')
    os.putenv('BUILD_URL', 'http://10.233.72.125:8080/job/madmin-client-deploy-dev-usa/62/')
    os.putenv('JOB_NAME', 'madmin-client-deploy-dev-usa')
    os.putenv('JOB_BASE_NAME', 'madmin-client-deploy-dev-usa')
    os.putenv('GIT_COMMIT', '7010456bb538fe4dc872126fe9e545c331fd139a')

  def test_get_build_number(self):
    self.assertEqual(cmr.get_build_number(), '62')


if __name__ == '__main__':
  unittest.main()
