from ddt import ddt, data, unpack, file_data
from BeautifulReport import BeautifulReport
from base.base_fixture import BaseFixture
from log.logger import Log
import unittest

log = Log().get_log()


@ddt
class TestCase(BaseFixture):

    @BeautifulReport.add_test_img("test_01_login")
    @file_data("../data/entry.yaml")
    def test_01_login(self, **entry):
        # 设置用例描述
        detail = entry.get('detail', '登录admin')
        self._testMethodDoc = detail
        self.pl.page_login()
        res = self.pl.get_assert_text()
        log.info('实际结果：{}，预期结果：{}'.format(res, entry['login_expect_result']))
        try:
            self.assertEqual(res, entry['login_expect_result'])
            log.info("登录断言成功！")
        except AssertionError:
            log.error("登录断言失败！")
            raise

    @BeautifulReport.add_test_img("test_03_open_contract")
    @file_data("../data/entry.yaml")
    def test_03_open_contract(self, **entry):
        detail = entry.get('detail', '打开合同管理页面')
        self._testMethodDoc = detail
        self.pc.page_open()
        res = self.pc.get_contract_assert_text()
        log.info('实际结果：{}，预期结果：{}'.format(res, entry['contract_expect_result']))
        try:
            self.assertIn(entry['contract_expect_result'], res)
            log.info("进入合同管理断言成功！")
        except AssertionError:
            log.error("进入合同管理断言失败！")
            raise

    @BeautifulReport.add_test_img("test_04_open_entry")
    @file_data("../data/entry.yaml")
    def test_04_open_entry(self, **entry):
        detail = entry.get('detail', '点击合同录入')
        self._testMethodDoc = detail
        self.pc.page_open_entry()
        res = self.pc.get_open_entry_assert_text()
        log.info('实际结果：{}，预期结果：{}'.format(res, entry['open_entry_expect_result']))
        try:
            self.assertEqual(entry['open_entry_expect_result'], res)
            log.info("点击合同录入断言成功！")
        except AssertionError:
            log.error("点击合同录入断言失败！")
            raise

    @BeautifulReport.add_test_img("test_05_entry")
    @file_data("../data/entry.yaml")
    def test_05_entry(self, **entry):
        detail = entry.get('detail', '提交合同录入信息')
        self._testMethodDoc = detail
        self.pe.page_entry(**entry)
        self.assertEqual(1, 3)
