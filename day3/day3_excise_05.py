import unittest
import requests
from test_login2 import TestLogin2,TestReg2

#
# suite = unittest.TestSuite()
# suite.addTest(TestLogin2("test_login"))
# suite.addTest(TestLogin2("test_reg"))

suite = unittest.defaultTestLoader.discover("./")
runner = unittest.TextTestRunner().run(suite)

