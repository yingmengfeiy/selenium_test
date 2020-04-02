from Base.base import Base
from selenium.webdriver.common.by import By
import time

class BookPage(Base):
    # 预订车票
    def book(self):
        return self.findele(By.XPATH, "//*[@id='searchlsit']/div[1]/div[1]/div[6]/div[1]/a")

    # 动车
    def book_typeD(self):
        return self.findele(By.CSS_SELECTOR, "#resultFilters01 > dl:nth-child(1) > dd:nth-child(4) > label > span")

    # # 关闭浮层
    # def book_close(self):
    #     return self.findele(By.CSS_SELECTOR, "appd_wrap_close")

    def book_btn(self):
        try:
            time.sleep(2)
            self.book().click()
            time.sleep(2)
        except:
            self.log.error("车次查询失败")
            None
        return self.url()