"""
============================
Author:丁琴
Time: 11:16
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import time
from common.basepage import BasePage
from locator.search_locator import Search_Locator as loc
class Order_Search(BasePage):
    def refresh_page(self):
        time.sleep(5)
        self.refresh()
    def click_confim(self):

        #         输入选择添加后点击确定按钮
        self.click_element(loc.search_confim_btn, "搜索页面_点击确定")
    def order_no_search(self,order_no):
    #     输入订单号
        self.clear_input(loc.order_no,"搜索页面_清空订单号输入框")
        self.input_text(loc.order_no,order_no,"搜索页面_输入订单号")
    def get_orderno_info(self,order_no):
        #     搜索订单号获取页面订单号字符串个数
        count_str=self.get_page_str(order_no,"搜索列表页面_获取订单号字符串个数")
        return count_str
    def order_theme_search(self,order_theme):
    #     输入主题
        self.clear_input(loc.order_theme,"搜索页面_清空主题输入框")
        self.input_text(loc.order_theme,order_theme,"搜索页面_输入主题")
    def get_ordertheme_info(self,order_theme):
        #     搜索主题获取页面主题字符串个数
        count_str=self.get_page_str(order_theme,"搜索列表页面_获取主题字符串个数")
        return count_str
    def product_name_search(self,product_name):
        # 输入品名搜索
        self.clear_input(loc.product_name,"搜索页面_清空品名输入框")
        self.input_text(loc.product_name,product_name,"搜索页面_输入品名")
    def get_productname_info(self,product_name):
        #     搜索品名获取页面品名字符串个数
        count_str=self.get_page_str(product_name,"搜索列表页面_获取品名字符串个数")
        return count_str
    def goods_no_search(self,goods_no):
        # 输入物料号搜索
        self.clear_input(loc.goods_no,"搜索页面_清空物料号输入框")
        self.input_text(loc.goods_no,goods_no,"搜索页面_输入物料号")
    def get_goodsno_info(self,goods_no):
        #     搜索物料号获取页面物料号字符串个数
        result=self.get_page_str_isnot(goods_no,"搜索列表页面_获取物料号字符串个数")
        return result

    def transaction_no_search(self,transaction_no):
        # 输入往来物料号搜索
        self.clear_input(loc.transaction_no,"搜索页面_清空往来物料号输入框")
        self.input_text(loc.transaction_no,transaction_no,"搜索页面_输入往来物料号")
    def get_transactionno_info(self,transaction_no):
        #     搜索往来物料号获取页面往来物料号字符串个数
        result=self.get_page_str_isnot(transaction_no,"搜索列表页面_获取往来物料号字符串个数")
        return result
    def creater_search(self,creater):
        # 输入创建人搜索
        self.clear_input(loc.creater,"搜索页面_清空创建人输入框")
        self.input_text(loc.creater,creater,"搜索页面_输入创建人")
    def get_creater_info(self,creater):
        #     搜索往来物料号获取页面往来物料号字符串个数
        result=self.get_page_str_isnot(creater,"搜索列表页面_获取创建人字符串个数")
        return result
    def contact_unit_search(self,contact_unit):
        # 输入往来单位搜索
        self.clear_input(loc.contact_unit,"搜索页面_清空往来单位输入框")
        self.input_text(loc.contact_unit,contact_unit,"搜索页面_输入往来单位")
    def get_contactunit_info(self,contact_unit):
        #     搜索往来单位获取页面往来单位字符串个数
        result=self.get_page_str_isnot(contact_unit,"搜索列表页面_获取往来单位字符串个数")
        return result
    def label_search(self,label):
        # 输入往来单位搜索
        self.clear_input(loc.label,"搜索页面_清空标签输入框")
        self.input_text(loc.label,label,"搜索页面_输入标签")
    def click_order_get_labelinfo(self):
        # 点击订单进入详情再点击标签看标签名是否存在
        ele=self.wait_element_visibility(loc.first_order,"搜索订单列表界面_点击第一条订单进入详情")
        ele.click()
#         点击标签
        self.click_element(loc.label_tab,"订单详情_点击标签")
        #         搜索的订单进入详情确认标签是否存在
        text = self.get_element_attr(loc.label_input, "value", "物品详情页面_标签是否存在")
        return text
    def balck_refresh(self):
        self.driver.back()
        self.driver.refresh()

    #   选择物品类型
    def order_goodstype_search(self):
        ele=self.wait_element_clickable(loc.goods_type,"订单的搜索页面_点击物品类型选择框")
        ele.click()
    def choose_clothing_type(self):
        self.order_goodstype_search()
        ele=self.wait_element_clickable(loc.clothing_type,"订单的搜索页面_点击物品类型选择框选择服装类型")
        ele.click()
    def choose_fabric_type(self):
        self.order_goodstype_search()
        ele=self.wait_element_clickable(loc.fabric_type,"订单的搜索页面_点击物品类型选择框选择面料类型")
        ele.click()
    def choose_lining_type(self):
        self.order_goodstype_search()
        ele=self.wait_element_clickable(loc.lining_type,"订单的搜索页面_点击物品类型选择框选择里料类型")
        ele.click()
    def get_page_info(self,name):
        text=self.get_page_str_isnot(name,"订单搜索列表_获取页面字符存在")
        return text
    # 选择订单类型
    def order_type_search(self):
        ele=self.wait_element_visibility(loc.order_type,"订单的搜索页面_点击订单类型选择框")
        ele.click()
    def choose_order_purchase(self):
        self.order_type_search()
        ele=self.wait_element_clickable(loc.order_purchase,"订单的搜索页面_点击订单类型选择框选择采购类型")
        ele.click()
    def choose_order_sale(self):
        self.order_type_search()
        ele=self.wait_element_clickable(loc.order_sale,"订单的搜索页面_点击订单类型选择框选择销售类型")
        ele.click()
