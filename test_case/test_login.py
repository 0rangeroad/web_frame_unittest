from ddt import ddt, data, unpack, file_data
from BeautifulReport import BeautifulReport
from base.base_fixture import BaseFixture
from common.data_load import read_excel_dic, write_excel
from log.logger import Log
log = Log().get_log()


@ddt
class TestLogin(BaseFixture):

    @BeautifulReport.add_test_img("test_01_login")
    @data(*read_excel_dic())
    def test_01_login(self, login):
        # 设置用例描述
        print(login)
        detail = login.get('detail', login['title'])
        self._testMethodDoc = detail
        params = eval(login['data'])
        if login['id'] == 1:
            res = self.pl.page_login_success(params['username'], params['password'])
        else:
            res = self.pl.page_login_fail(params['username'], params['password'])
        log.info('实际结果：{}，预期结果：{}'.format(res, login['expected']))
        try:
            self.assertEqual(res, login['expected'])
            log.info("登录断言成功！")
            write_excel(login['id'] + 1, 5, '通过')
        except AssertionError:
            log.error("登录断言失败！")
            write_excel(login['id'] + 1, 5, '未通过')
            raise
    #
    # @unittest.skip("不退出登录")
    # @BeautifulReport.add_test_img("test_02_click_exit")
    # @file_data("../data/entry.yaml")
    # def test_02_click_exit(self, **entry):
    #     detail = entry.get('detail', '退出登录')
    #     self._testMethodDoc = detail
    #     self.pi.page_exit()
    #     res = self.pi.page_assert_text()
    #     log.info('实际结果：{}，预期结果：{}'.format(res, entry['exit_expect_result']))
    #     try:
    #         self.assertEqual(entry['exit_expect_result'], res)
    #         log.info("退出登录断言成功！")
    #     except AssertionError:
    #         log.error("退出登录断言失败！")
    #         raise
