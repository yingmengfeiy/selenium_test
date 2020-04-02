from Base.base import Base
from selenium.webdriver.common.by import By
import time


class OrderPage(Base):
    # 预订车票
    def detail_name(self):
        return self.findele(By.CSS_SELECTOR, "#pasglistdiv > div > ul > li:nth-child(2) > input")

    def user_info(self, name):
        time.sleep(3)
        self.detail_name().send_keys(name)
        return self.url()
