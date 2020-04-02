import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from Common.function import project_path

if __name__ == '__main__':
    test_dir = project_path()+"Testcases"
    tests=unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    filepath = project_path()+"/Report/"+now+'.html'
    fp = open(filepath, 'wb')
    # 定义测试报告的标题和描述
    runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试报告')
    runner.run(tests)
    fp.close()

