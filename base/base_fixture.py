import os
import unittest
from page_object.page_contract import PageContract
from page_object.page_entry import PageEntry
from page_object.page_index import PageIndex
from page_object.page_login import PageLogin
from log.logger import Log
from selenium import webdriver

log = Log().get_log()


class BaseFixture(unittest.TestCase):
    driver = None

    # 断言失败后自动调用固定save_img方法名截图
    def save_img(self, img_name):
        img_path = os.path.dirname(__file__).split('base')[0]+"img"
        log.info("正在将断言截图{}.png,存储至{}".format(img_name, img_path))
        try:
            self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))
        except Exception:
            log.error("断言截图失败!")
            raise

    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.pl = PageLogin(cls.driver)
            cls.pi = PageIndex(cls.driver)
            cls.pc = PageContract(cls.driver)
            cls.pe = PageEntry(cls.driver)
        except Exception as e:
            log.error("错误信息：{}".format(e))

    def setUp(self) -> None:
        log.info("-" * 35 + '用例开始执行' + "-" * 35)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        log.info("正在执行关闭driver对象操作")
        cls.driver.quit()
