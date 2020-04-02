import unittest
from Common.function import config_url
from selenium import webdriver


# 抽离单元测试中的setUp和tearDown
class UnitBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
