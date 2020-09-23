"""
============================
Author:丁琴
Time: 15:58
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By

from common.basepage import BasePage
from common.handle_confing import conf
from locator.login_locator import LoginLocator as loc
from selenium.webdriver import Chrome
import time
class Login_Page(BasePage):
    # 首页地址
    url=conf.get("env","base_url")+conf.get("url","login_url")
    def __init__(self,driver:Chrome):
        super().__init__(driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
    def login(self,user,pwd):
#         输入账号密码登录
        self.input_text(loc.mobile,user,"登录页面_输入账号")
        self.input_text(loc.pwd,pwd,"登录页面_输入密码")
        self.click_element(loc.login_btn,"登录页面_点击登录")
    def login_error_info(self):
        # 登录失败获取错误提示
        time.sleep(1)
        text=self.get_element_text(loc.login_error_info,"登录页面_登录失败错误提示信息")
        return text
    def refresh(self):
        # 刷新页面
        self.driver.refresh()