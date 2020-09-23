"""
============================
Author:丁琴
Time: 9:57
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from common.basepage import BasePage
from locator.warehouse_locator import WarehouseLocator as loc
from selenium.webdriver.common.by import By

import time
class WareHouse(BasePage):

    def build_warehouse(self,warehousename,contacts,contactnumber,address,marks):
        self.type_warehousename(warehousename)
        self.type_contacts(contacts)
        self.type_contact_number(contactnumber)
        self.choose_province_city()
        self.type_address(address)
        self.choose_warehouse_type()
        self.type_marks(marks)
        self.click_confim()
    def build_warehouse_fail(self,warehousename,contacts):
        self.type_warehousename(warehousename)
        self.type_contacts(contacts)
        self.click_confim()
    def type_warehousename(self,warehousename):
        self.input_text(loc.warehouse_name,warehousename,"添加仓库页面_输入仓库名称")
    def type_contacts(self,contacts):
        self.input_text(loc.contacts,contacts,"添加仓库页面_输入联系人")
    def type_contact_number(self,contactnumber):
        self.input_text(loc.contact_number,contactnumber,"添加仓库页面_输入联系人")
    def choose_province_city(self):
        # 选择省
        ele=self.wait_element_clickable(loc.choose_province,"添加仓库页面_选择省")
        ele.click()
        time.sleep(1)
        js = """
        window.scrollTo(0,100);
        """
        self.driver.execute_script(js)
        self.click_element(loc.province,"添加仓库页面_选择省")
        # 选择市
        ele=self.wait_element_visibility(loc.choose_city,"添加仓库页面_选择市")
        ele.click()
        js = """
        window.scrollTo(0,100);
        """
        self.driver.execute_script(js)
        self.click_element(loc.city,"添加仓库页面_选择市")
    def type_address(self,address):
        self.input_text(loc.input_addr,address,"添加仓库页面_填写地址")
    def choose_warehouse_type(self):
        self.click_element(loc.choose_warehousetype,"添加仓库页面_点击类型")
        self.click_element(loc.choose_innerwarehouse,"添加仓库页面_点击内部仓库")
    def type_marks(self,marks):
        self.input_text(loc.input_remarks,marks,"添加仓库页面_输入备注")
    def click_confim(self):
        self.click_element(loc.confirm_btn,"添加仓库页面_点击确定按钮")
    def click_cacel(self):
        self.click_element(loc.cacle_btn,"添加仓库页面_点击取消按钮")

    def get_success_info(self):
        # text=self.get_element_text(loc.success_toast,"添加仓库页面_保存成功提示")
        ele=self.wait_element_visibility(loc.success_toast,"添加仓库页面_保存成功提示")
        text=ele.text
        return text
    def get_fail_toast(self):
        text=self.get_element_text(loc.fail_tosat,"添加仓库页面_保存失败提示")
        return text

    def get_warehousename_str(self,warehousename):
        str_count=self.get_page_str(warehousename,"添加仓库页面_保存成功后页面存在该仓库名称")
        return str_count


