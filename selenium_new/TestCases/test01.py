import unittest
from selenium import webdriver
import time
from Common.log import FrameLog


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       cls.log = FrameLog()
       cls.logger = cls.log.get_log()

    @classmethod
    def tearDownClass(cls):
       cls.log.close_handle()

    def setUp(self):
        self.logger.info("--start test --")
        base_url = 'https://www.baidu.com'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.logger.info("--test end--")

    def test_baidunews(self):
        u"""百度新闻"""
        driver = self.driver
        driver.find_element_by_link_text('新闻').click()
        time.sleep(2)
        self.assertIn(driver.title, u'百度新闻——海量中文资讯平台')


if __name__ == '__main__':
   unittest.main()