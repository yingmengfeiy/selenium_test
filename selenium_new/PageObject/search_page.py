from Base.base import Base
from selenium.webdriver.common.by import By
import time


class SearchPage(Base):
    def search_leave(self):
        return self.findele(By.ID,"notice01")

    # 八大定位
    def search_arrive(self):
        return self.findele(By.ID,"notice08")

    def search_date(self):
        return  self.findele(By.ID,"dateObj")

    def search_btn(self):
        return self.findele(By.ID,"searchbtn")

    def search_current(self):
        return self.findele(By.CSS_SELECTOR, "#searchtype > li.current")

    def search_js(self,value):
        jsvalue = "document.getElementById('dateObj').value='%s'" %(value)
        self.js(jsvalue)

    def search_train(self, leave, arrive, leave_date):
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        time.sleep(2)
        self.search_js(leave_date)
        self.search_current().click()
        self.search_btn().click()
        time.sleep(3)
        return self.url()