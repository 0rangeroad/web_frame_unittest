from selenium.webdriver.common.by import By
from log.logger import Log
from base.base import Base

log = Log().get_log()


class PageContract(Base):
    url = 'http://oa.wdrjtz.com/loginAction.do?login&functionid=8a8634885af39a5a015af39c95580001'
    entry_btn_loc = (By.XPATH, '//span[text()="录入"]')
    contract_success_assert_loc = (By.ID, 'locationName1')
    entry_assert_loc = (By.XPATH, '//*[@id="tab2"]/div/table/thead/tr/th')

    def page_open(self):
        self.base_visit(self.url)

    def page_click_entry(self):
        self.base_click_element(self.entry_btn_loc)

    def page_open_entry(self):
        self.page_click_entry()

    # 断言合同管理页面文本
    def get_contract_assert_text(self):
        return self.base_get_text(self.contract_success_assert_loc)

    # 断言录入弹窗文本
    def get_open_entry_assert_text(self):
        self.base_switch_iframe(0)
        text = self.base_get_text(self.entry_assert_loc)
        self.base_default_content()
        return text
