"""
============================
Author:丁琴
Time: 16:27
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import os
from webbrowser import Chrome

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from common.handle_logging import my_log
from common.handle_path import ERROR_IMG
from selenium.webdriver import Chrome, ActionChains


class BasePage:
    # 封装一些页面常用的操作动作
    def __init__(self,driver:Chrome):
        self.driver=driver

    def wait_element_visibility(self,locator,img_info,timeout=20,poll_frequency=0.5):
        """等待元素可见"""
        # 等待之前获取一下当前时间
        start_time=time.time()
        try:
            ele=WebDriverWait(self.driver,timeout,poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            my_log.error("等待元素--{}--失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("等待元素--{}--成功".format(locator))
            return ele
    def wait_element_clickable(self,locator,img_info,timeout=20,poll_frequency=0.5):
        """
        等待元素可点击
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :param timeout: 等待超时时间
        :param poll_frequency: 等待轮询时间
        :return:
        """
        # 等待元素之前获取当前时间
        start_time=time.time()
        try:
            ele=WebDriverWait(self.driver,timeout,poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as e:
            # 输出日志
            my_log.error("元素--{}--等待超时".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            # 元素等待出现后获取实际时间
            end_time=time.time()
            my_log.info("元素等待成功，等待时间{}".format(end_time-start_time))
            return ele
    def wait_element_presence(self,locator,img_info,timeout=20,poll_frequency=0.5):
        """
        等待元素可见
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :param timeout: 等待超时时间
        :param poll_frequency: 等待轮询时间
        :return:
        """
        # 等待元素之前获取当前时间
        start_time=time.time()
        try:
            ele=WebDriverWait(self.driver,timeout,poll_frequency).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            # 输出日志
            my_log.error("元素--{}--等待超时".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            # 元素等待出现后获取实际时间
            end_time=time.time()
            my_log.info("元素等待成功，等待时间{}".format(end_time-start_time))
            return ele
    def get_element_text(self,locator,img_info):
        """
        获取文本内容
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :param timeout: 等待超时时间
        :param poll_frequency: 等待轮询时间
        :return:
        """
        try:
            text=self.driver.find_element(*locator).text
        except Exception as e:
            # 输出日志
            my_log.error("元素--{}--获取文本失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("元素--{}--获取文本成功".format(locator))
            return text
    def get_element_attr(self,locator,attr_name,img_info):
        """
        获取元素属性值
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :param timeout: 等待超时时间
        :param poll_frequency: 等待轮询时间
        :return:
        """
        try:
            ele=self.driver.find_element(*locator)
            attr_value=ele.get_attribute(attr_name)
        except Exception as e:
            # 输出日志
            my_log.error("元素--{}--获取属性失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("元素--{}--获取属性成功".format(locator))
            return attr_value
    def click_element(self,locator,img_info):
        """
        元素点击
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :param timeout: 等待超时时间
        :param poll_frequency: 等待轮询时间
        :return:
        """
        try:
            self.driver.find_element(*locator).click()
        except Exception as e:
            # 输出日志
            my_log.error("点击元素--{}--失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("点击元素--{}--成功".format(locator))
    def input_text(self,locator,text_value,img_info):
        """
        输入内容
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :return:
        """
        try:
            self.driver.find_element(*locator).send_keys(text_value)
        except Exception as e:
            # 输出日志
            my_log.error("输入文本--{}--失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("输入文本--{}--成功".format(locator))
    def get_element(self,locator,img_info):
        """
        获取元素
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :return:
        """
        try:
            ele=self.driver.find_element(*locator)
        except Exception as e:
            # 输出日志
            my_log.error("获取元素--{}--失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("获取元素--{}--成功".format(locator))
            return ele
    def clear_input(self,locator,img_info):
        """
        清空输入框内容
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :return:
        """
        try:
            self.driver.find_element(*locator).clear()
        except Exception as e:
            # 输出日志
            my_log.error("清空内容--{}--失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("清空内容--{}--成功".format(locator))
    def move_to_element(self,locator,img_info):
        """
        鼠标移动到某个元素
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :return:
        """
        try:
            ele=self.driver.find_element(*locator)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            # 输出日志
            my_log.error("移动元素--{}--失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("移动元素--{}--成功".format(locator))
    def double_click_element(self,locator,img_info):
        """
        双击某个元素
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :return:
        """
        try:
            ele=self.driver.find_element(*locator)
            ActionChains(self.driver).double_click(ele).perform()
        except Exception as e:
            # 输出日志
            my_log.error("双击元素--{}--失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
        else:
            my_log.info("双击元素--{}--成功".format(locator))

    def get_page_str(self,name,img_info):
        """
        # 查找页面的字符串个数
        :param pagesource: 页面源代码
        :param img_info: 错误信息
        :return:
        """
        try:
            pagesource = self.driver.page_source
            str_count=pagesource.count(name)
            return str_count
        except  Exception as e:
            my_log.error("字符串---{}--获取失败".format(name))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e

    def get_page_str_isnot(self, name, img_info):
        """
        # 查找页面的字符串个数是否大于2
        :param pagesource: 页面源代码
        :param img_info: 错误信息
        :return:
        """
        try:
            pagesource = self.driver.page_source
            str_count = pagesource.count(name)
            if str_count >= 2:
                return "搜索数据成功"
            elif str_count==1:
                return "搜索数据失败"
        except  Exception as e:
            my_log.error("字符串---{}--获取失败".format(name))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
    def get_maxpage_str(self,name,img_info):
        """
        # 查找页面字符串是否存在
        :param pagesource: 页面源代码
        :param img_info: 错误信息
        :return:
        """
        try:
            # time.sleep(10)
            # js = """
            # window.scrollBy(0,document.body.scrollHeight);
            # """
            # self.driver.execute_script(js)
            # time.sleep(10)
            pagesource = self.driver.page_source
            if pagesource.find(name)!=-1:
                return name
        except  Exception as e:
            my_log.error("字符串---{}--获取失败".format(name))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
    def refresh(self):
        self.driver.refresh()
    #     获取新窗口在新窗口操作
    def get_windows(self,locator,img_info):
        # 打开新窗口之前获取所有窗口
        start_win = self.driver.window_handles
        try:
            # 点击搜索的数据打开新窗口
            ele=self.wait_element_clickable(locator,img_info)
            ele.click()
        # 等待新窗口是否打开
            time.sleep(2)
            WebDriverWait(self.driver, 30, 0.5).until(
                EC.new_window_is_opened(start_win)
                )
    # 打开新窗口后获取所有窗口句柄, 然后下标取值切换到新窗口，就可以定位新窗口的元素
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except Exception as e:
            raise e
        finally:
            pass
    def get_time_str(self,starttime,endtime,img_info):
        """
        # 搜索时间查找页面这两个时间以外的时间字符串个数，如果都是0搜索成功
        :param pagesource: 页面源代码
        :param img_info: 错误信息
        :return:
        """
        try:
            pagesource = self.driver.page_source
            if pagesource.count(starttime)==0 and pagesource.count(endtime)==0:
                return 0
        except  Exception as e:
            my_log.error("时间字符串---{}--{}存在--搜索结果不正确".format(starttime,endtime))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e
    def find_province_city(self,name,locator,img_info):
    #     选择省需要点击选择框，鼠标滑动页面出现那个省市的字符才能去点击那个元素
        old = ""
        new = self.driver.page_source
        try:
            while old != new:  # 没有划到页面底部之前：更新前和更新后的页面内容是否一致
                # 找一次，找文本  # 当此元素可见时，停止循环
                if new.find(name) != -1:
                    # 找到这个名字
                    print("找到   元素了！！")
                    break
                # 鼠标滑动，会导致页面的内容更新。

                old = new
                new = self.driver.page_source  # 重新赋值。
                self.click_element(locator, img_info)
        except  Exception as e:
            my_log.error("元素---{}--定位失败".format(locator))
            my_log.exception(e)
            # 捕获出错的当前页面截屏
            self.save_scree_image(img_info)
            raise e

    def save_scree_image(self,img_info):
        """
        对当前页面进行截图
        :param img_info: 错误截图信息
        :return:
        """
        start_time = time.time()
        filename = '{}_{}.png'.format(img_info, start_time)
        file_path = os.path.join(ERROR_IMG, filename)
        self.driver.save_screenshot(file_path)
        my_log.info("错误页面截图成功，图片保存的路径:{}".format(file_path))
