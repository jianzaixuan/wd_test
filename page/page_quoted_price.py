"""
============================
Author:丁琴
Time: 9:32
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from common.basepage import BasePage
from locator.quoted_price_locator import QuotedprinceLocator as loc
from locator.index_locator import IndexLocator as indexloc
from locator.business_locator import AddBusinesslocator as busloc
import time
class QuotedPrice(BasePage):
    def click_add(self):
        time.sleep(2)
        ele=self.wait_element_visibility(indexloc.add_btn,"首页_报价模块点击添加按钮")
        ele.click()
    def type_goodsno(self,goodno):
        self.input_text(busloc.search_goodsno,goodno,"选择物品弹框页面_输入物料号")
    def click_search(self):
        self.click_element(loc.search_btn,"选择物品弹框页面_输入物料号点击搜索按钮")
    def click_checkbox(self):
        self.click_element(busloc.choose_checkbox,"选择物品弹框页面_输入物料号点击搜索按钮后选择物品")
    def click_confirm(self):
        # ele=self.wait_element_presence(busloc.goods_confirm_btn,"选择物品弹框页面_输入物料号点击搜索按钮后选择物品点击确定按钮")
        # ele.click()
        self.click_element(loc.confirm,"选择物品弹框页面_输入物料号点击搜索按钮后选择物品点击确定按钮")
    def type_contact_unit(self,contact_unit):
        ele=self.click_element(loc.contact_unit,"报价详情页面_点击往来单位输入往来单位")
        ele.send_keys(contact_unit)
    def choose_contact_unit(self):
        self.click_element(loc.choose_contact,"报价详情页面_点击往来单位输入往来单位后选择")
    def click_contact_no(self):
        ele=self.wait_element_visibility(loc.contact_no,"报价详情页面_点击往来物料号")
        ele.click()
    def type_contact_no(self,contact_no):
        self.input_text(loc.input_contact_no,contact_no,"报价详情页面_点击往来物料号输入往来物料号")
    def contact_no_confirm(self):
        self.click_element(loc.click_confirm,"报价详情页面_点击往来物料号输入往来物料号点击确定")
    def click_save(self):
        self.click_element(busloc.save,"报价详情页面_点击保存按钮")
    def get_create_price_toast(self):
        text=self.get_element_text(loc.create_price_toast,"报价详情页面_创建成功弹出的提示")
        return text
    def get_save_toast(self):
        text=self.get_element_text(loc.save_toast,"报价详情页面_保存成功弹出的提示")
        return text
    def get_goodsno_error(self):
        text=self.get_element_text(loc.choose_goods_toast,"报价详情页面_没有输入物料号点击确定")
        return text
