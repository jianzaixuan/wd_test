"""
============================
Author:丁琴
Time: 9:45
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By
# 登录页面所有元素定位
class LoginLocator:
    # 输入账号
    # mobile=(By.XPATH,"//input[@placeholder='输入账号']")

    mobile = (By.XPATH, "//input[@ng-model='username']")
    # 输入密码
    pwd=(By.XPATH, "//input[@placeholder='输入密码']")
    # 点击登录
    login_btn = (By.XPATH, "//button[text()='登录']")
    # 登录失败错误提示
    login_error_info=(By.XPATH, "//article[@class='alertify-log alertify-log-error alertify-log-show']")