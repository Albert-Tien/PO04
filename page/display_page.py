import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_Action import BaseAction
class NetworkPage(BaseAction):
    button1 = By.XPATH, "//*[contains(@text,'更多')]"
    button2 = By.ID, "com.android.settings:id/search"
    button3 = By.XPATH,"//*[contains(@text,'搜索…')]"
    def click_more(self):
       self.click(self.button1)
    def click_rearch(self):
        self.click(self.button2)
    def input_search(self,text):
        self.input_rearch(self.button3,text)


