from selenium.webdriver.common.by import By
from log.logger import Log
from base.base import Base

log = Log().get_log()


class PageIndex(Base):
    url = 'http://oa.wdrjtz.com/loginAction.do?symain'
    exit_loc = (By.XPATH, '//b[text()="退出"]')
    confirm_loc = (By.XPATH, '//input[@value="确定"]')
    exit_assert_loc = (By.XPATH, '//label[text()="OA系统"]')

    # 打开登录页面
    def page_open(self):
        self.base_visit(self.url)

    # 退出登录
    def page_exit(self):
        self.base_click_element(self.exit_loc)
        self.base_click_element(self.confirm_loc)

    # 断言退出登录文本
    def page_assert_text(self):
        return self.base_get_text(self.exit_assert_loc)
