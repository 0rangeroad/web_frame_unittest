import os
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from log.logger import Log
import time

log = Log().get_log()


class Base:
    # 构造driver对象
    def __init__(self, driver):
        log.info("正在获取初始化driver对象:{}".format(driver))
        self.driver = driver

    def base_visit(self, url):
        log.info("正在打开页面：{}".format(url))
        self.driver.get(url)

    def base_find_element(self, loc, timeout=20):
        try:
            # 使用显示等待获取元素
            ele = WebDriverWait(self.driver, timeout=timeout).until(lambda x: x.find_element(*loc))
            log.info("元素定位成功")
            return ele
        except Exception:
            log.error("元素定位失败，元素：{}".format(loc))
            raise

    # 获取元素值的方法
    def base_get_text(self, loc):
        log.info("正在获取:{} 元素文本值".format(loc))
        try:
            text = self.base_find_element(loc).text
            log.info("正在获取元素文本值:{}".format(text))
            return text
        except Exception:
            log.error("获取元素值失败！")
            raise

    def base_send_keys(self, loc, txt):
        log.info("正在给元素{} 输入内容：{}".format(loc, txt))
        ele = self.base_find_element(loc)
        log.info("正在给元素:{}清空".format(loc))
        ele.clear()
        log.info("正在给元素:{}输入内容".format(loc))
        try:
            ele.send_keys(txt)
        except Exception:
            log.error("元素输入文本{}失败！".format(txt))
            raise

    def base_click_element(self, loc):
        log.info("正在点击元素:{}".format(loc))
        try:
            self.base_find_element(loc).click()
        except Exception:
            log.error("点击元素失败，元素：".format(loc))
            raise

    # 判断元素是否存在
    def base_element_exits(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info("判断元素:{}存在！".format(loc))
            return True
        except Exception as e:
            log.error("判断元素不存在！".format(e))
            return False

    # 切换frame表单的方法
    def base_switch_iframe(self, frame_reference):
        log.info("正在进入:{}框架！".format(frame_reference))
        try:
            self.driver.switch_to.frame(frame_reference)
        except Exception:
            log.error("iframe切换失败！")
            raise

    # 回到默认目录的方法
    def base_default_content(self):
        log.info("正在回到默认框架！")
        try:
            self.driver.switch_to.default_content()
        except Exception:
            log.error("切回默认目录失败！")
            raise

    # 切换窗口的方法
    def base_switch_to_window(self, title):
        log.info("正在切换到:{}窗口！".format(title))
        self.driver.switch_to.window(self.base_get_title_handle(title))

    # 获取指定title页面的handle方法
    def base_get_title_handle(self, title):
        # 获取当前页面所有的handles
        for handle in self.driver.window_handles:
            log.info("正在遍历handles：{}-->{}".format(handle, self.driver.window_handles))
            # 切换 handle
            self.driver.switch_to.window(handle)
            log.info("切换至:{} 窗口".format(handle))
            # 获取当前页面title并判断是否等于指定参数title
            log.info("判断当前页面title:{} 是否等于指定的title:{}".format(self.driver.title, title))
            if self.driver.title == title:
                log.info("条件成立！ 返回当前handle{}".format(handle))
                return handle

    # 截图方法
    def base_save_img(self):
        log.info("断言出错，调用截图")
        now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        try:
            self.driver.get_screenshot_as_file(os.path.dirname(__file__).split('base')[0]+"img/{}.png".format(now_time))
        except Exception:
            log.error("调用截图失败！")
            raise

    def base_script(self, js):
        log.info("正在加载js脚本:{}".format(js))
        try:
            self.driver.execute_script(js)
        except Exception:
            log.error("脚本{}加载失败！".format(js))
            raise

    def base_script_ele(self, loc, js):
        """定位某一元素执行js脚本"""
        args = self.base_find_element(loc)
        log.info("正在传入脚本元素定位:{}".format(args))
        self.driver.execute_script(js, args)
        log.info("正在加载js脚本:{}".format(js))

    def base_scroll_ele(self, loc):
        """将指定元素滚动显示到页面"""
        js = "arguments[0].scrollIntoView()"
        self.driver.execute_script(js, self.base_find_element(loc))

    def base_scroll_end(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        log.info("正在滑动到页面底部:{}".format(js))
        self.driver.execute_script(js)

    def base_remove_attribute(self, loc, attr):
        """移除某一元素的属性"""
        js = "arguments[0].removeAttribute(arguments[1])"
        log.info("正在定位元素:{}".format(loc))
        args = self.base_find_element(loc)
        self.driver.execute_script(js, args, attr)
        log.info("正在移除元素属性:{}".format(attr))

    @classmethod
    def base_get_position(cls):
        """获取鼠标当前坐标"""
        last_pos = pyautogui.position()
        try:
            while True:
                new_pos = pyautogui.position()
                if new_pos == (0, 0):
                    print("定位完成")
                    break
                if new_pos != last_pos:
                    time.sleep(1)
                    last_pos = new_pos
            return last_pos
        except KeyboardInterrupt:
            print('结束')
