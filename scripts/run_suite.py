# 导包
import unittest
from tool.HTMLTestReportCN import HTMLTestRunner
# 定义测试套件
suite = unittest.defaultTestLoader.discover("./")
# 获取报告存储文件流，并实例化HTMLTestRunner 调用run方法执行suite
with open("../report/report.html","wb")as f:
    HTMLTestRunner(stream=f).run(suite)