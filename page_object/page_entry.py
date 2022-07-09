from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
from log.logger import Log
from base.base import Base

log = Log().get_log()


class PageEntry(Base):
    # max_loc = (By.XPATH, '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/div[2]/a[2]')
    frame_loc = (By.XPATH, '//iframe[@name="JDG16554342953581"]')
    tel_loc = (By.XPATH, '//input[@nullmsg="请填写联系电话"]')
    contract_name_loc = (By.XPATH, '//input[@nullmsg="请填写合同名称"]')
    date_loc = (By.XPATH, '//input[@nullmsg="请选择制定时间"]')
    amount_loc = (By.XPATH, '//input[@nullmsg="请填写合同金额"]')
    del_btn_loc = (By.XPATH, '//*[@id="tTable"]/tbody/tr[3]/td[5]/a')
    contract_big_loc = (By.NAME, 'fshtlx1')
    xdrmc_loc = (By.XPATH, '//input[@nullmsg="请填写相对人名称"]')
    identity_loc = (By.XPATH, '//input[@nullmsg="请填写营业执照/身份证"]')
    describe_loc = (By.XPATH, '//textarea[@nullmsg="请填写事项描述"]')
    submit_btn = (By.XPATH, '//a[@onclick="doSubmit()"]')

    def page_entry(self, **entry):
        # 进入第一个iframe框架
        self.base_switch_iframe(0)
        # 滑动至底部
        self.base_scroll_end()
        # 提交录入合同
        # self.base_click_element(self.submit_bt)
        # 联系电话
        self.base_send_keys(self.tel_loc, entry['tel'])
        # # 合同名称
        self.base_send_keys(self.contract_name_loc, entry['contract_name'])
        # 移除日期readonly属性
        self.base_remove_attribute(self.date_loc, entry['attr'])
        # # 输入日期
        self.base_send_keys(self.date_loc, entry['date'])
        # # 合同金额
        self.base_send_keys(self.amount_loc, entry['amount'])
        # # 点击删除
        self.base_click_element(self.del_btn_loc)
        # # 选择合同大类
        sel = Select(self.base_find_element(self.contract_big_loc))
        sel.select_by_value(entry['value'])
        # # 相对人名称
        self.base_send_keys(self.xdrmc_loc, entry['xdrmc'])
        # # 身份证
        self.base_send_keys(self.identity_loc, entry['identity'])
        # 事项描述
        self.base_send_keys(self.describe_loc, entry['describe'])
        # 返回原目录
        self.base_default_content()

