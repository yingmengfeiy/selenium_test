import os, sys
import time, unittest
from HTMLTestRunner import HTMLTestRunner

from Common.log import FrameLog
from PageObject.book_page import BookPage
from PageObject.order_page import OrderPage
from PageObject.search_page import SearchPage
from Common.excel_data import read_excel
from Common.function import config_url
from selenium import webdriver
from Common.function import project_path
sys.path.append(os.path.split(os.getcwd())[0])


class logingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = read_excel(project_path()+'Data/testdata.xlsx',0)
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()
        cls.log = FrameLog()
        cls.logger = cls.log.get_log()

    def test_02(self):
        self.driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")
        search = SearchPage(self.driver)
        res = search.search_train(self.data.get(1)[0], self.data.get(1)[1], self.data.get(1)[2])
        # 本例断言是根据当前页面的URL来判断的
        try:
           self.assertIn('TrainBooking', res)
           self.logger.info("用例通过")
        except:
            self.logger.error("用例失败")

    def test_03(self):
        book = BookPage(self.driver)
        res = book.book_btn()
        # 断言当前页面的URL是否包含“InputPassengers”
        self.assertIn("InputPassengers", res)

    def test_04(self):
        order = OrderPage(self.driver)
        res = order.user_info("小王")
        self.assertIn("RealTimePay", res)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()


if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(logingTest("test_02"))
    suiteTest.addTest(logingTest("test_03"))
    suiteTest.addTest(logingTest("test_04"))
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    filepath = project_path()+'Reports\\'+now+'.html'
    fp = open(filepath, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试报告')
    runner.run(suiteTest)
    fp.close()