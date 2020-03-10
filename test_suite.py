# 测试套件

# 1.导包
import time
import unittest
from script.test_login import TestLogin


# 2.创建测试套件
from tools.HTMLTestRunner import HTMLTestRunner

test_suite = unittest.TestSuite()

# 3.添加测试用例
test_suite.addTest(unittest.makeSuite(TestLogin))

# 4.指定报告路径
report_path = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 5.打开文件流
with open(report_path, "wb") as f:
    # 5.1 创建运行器
    runner = HTMLTestRunner(f, title="test report", description="hahaha")
    # 5.2 执行测试套件
    runner.run(test_suite)
