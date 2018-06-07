import os,sys
sys.path.append(os.getcwd())
from page.display_page import NetworkPage
from base.base_driver import init_driver
class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.dis = NetworkPage(self.driver)
    def test_display(self):
        self.dis.click_more顶顶顶顶顶顶()
        self.dis.click_rearch()
        self.dis.input_search("admin")





