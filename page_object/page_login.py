from selenium.webdriver.common.by import By
from log.logger import Log
from base.base import Base
import time

log = Log().get_log()


class PageLogin(Base):
    url = 'http://oa.wdrjtz.com/loginAction.do?login'
    usr_loc = (By.XPATH, '//input[@placeholder="请输入用户名"]')
    pwd_loc = (By.XPATH, '//input[@placeholder="请输入密码"]')
    login_btn_loc = (By.XPATH, '//div[text()="登录"]')
    login_err = (By.XPATH, '//div[@class="layui-layer-content"]')
    # login_success_assert_loc = (By.ID, 'locationName')
    login_success_assert_loc = (By.XPATH, '//a[@title="登陆用户"]/b')

    # 打开登录页面
    def page_open(self):
        self.base_visit(self.url)

    # 输入用户名
    def page_input_usr(self, usr):
        self.base_send_keys(self.usr_loc, usr)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_send_keys(self.pwd_loc, pwd)

    # 点击登录
    def page_click_login(self):
        self.base_click_element(self.login_btn_loc)

    # 登录成功
    def page_login_success(self, usr, pwd):
        log.info("正在执行登录操作, 用户名：{} 密码：{}".format(usr, pwd))
        self.page_open()
        # 输入用户名
        self.page_input_usr(usr)
        # 输入密码
        self.page_input_pwd(pwd)
        # 点击登录
        self.page_click_login()
        # 登录成功断言
        return self.base_get_text(self.login_success_assert_loc)

    # 登录失败
    def page_login_fail(self, usr, pwd):
        log.info("正在执行登录操作, 用户名：{} 密码：{}".format(usr, pwd))
        self.page_open()
        # 输入用户名
        self.page_input_usr(usr)
        # 输入密码
        self.page_input_pwd(pwd)
        # 点击登录
        self.page_click_login()
        time.sleep(1.5)
        # 登录错误弹窗断言
        return self.base_get_text(self.login_err)
