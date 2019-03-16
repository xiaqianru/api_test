import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

# 使用unittest默认的加载器，便利发现所有test开头py文件中所有Test类中的test开头方法
# 返回一个包含所有用例的测试集合
suite = unittest.defaultTestLoader.discover("./",pattern="test_*")
# 新建一个执行器 verbosity显示级别为最高级2
# runner = unittest.TextTestRunner(verbosity=2)
# 使用执行器执行测试集合
# runner.run(suite)

f = open("report.html","wb")
runner = HTMLTestRunner(stream=f,title="我的接口测试报告",description="这是课堂练习",verbosity=2)

runner.run(suite)
f.close()