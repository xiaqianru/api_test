import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./", pattern="test_*")
f = open("report.html", "wb")
runner = HTMLTestRunner(stream=f,title="加油卡测试报告",description="第三天作业",verbosity=2)
runner.run(suite)
f.close()
