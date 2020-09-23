"""
============================
Author:丁琴
Time: 16:55
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.basepage import BasePage
from locator.index_locator import IndexLocator as loc
# 下面是搜索按钮和搜索界面字段的定位文件
from locator.search_locator import Search_Locator as sloc
from selenium.webdriver import Chrome
import time
class Index_Page(BasePage):
    def get_info(self):
        try:
            time.sleep(4)
            self.wait_element_visibility(loc.comp_ele,"首页_获取登录成功标识")
        except:
            return "登录失败"
        else:
            return "登录成功"
    def exit(self):
        # 退出
        self.click_element(loc.exit,"首页_点击退出")
    def click_goods(self):
        # 点击物品模块
        time.sleep(4)
        ele=self.wait_element_clickable(loc.goods_btn,"首页_点击物品模块")
        ele.click()
        # self.click_element(loc.goods_btn,"首页_点击物品模块")
    def click_addgoods(self):
    #     点击添加物品按钮
        time.sleep(3)
        self.click_element(loc.add_btn,"首页物品模块_点击添加物品按钮")

    def search_btn(self):
#         搜索按钮
        time.sleep(3)
        ele=self.wait_element_clickable(sloc.search_goods_btn,"首页_点击搜索按钮")
        ele.click()
        # self.click_element(sloc.search_goods_btn,"首页_点击搜索按钮")

    def input_goodsno(self,goodsno):
        # 在搜索框输入物料号
        time.sleep(1)
        self.input_text(sloc.goods_no,goodsno,"搜索页面_物料号输入框输入物料号")
    def search_confim_btn(self):
        # 搜索页面点击确定按钮
        self.click_element(sloc.search_confim_btn,"搜索页面_点击确定按钮")
    def confirm_goodsno_exist(self):
        text=self.get_element_text(loc.confirm_goodsno_exist,"搜索成功列表_获取物料号是否跟预期一致")
        return text
    # def click_goodsno_exist(self):
    #     self.click_element(loc.confirm_goodsno_exist,"搜索成功列表_点击这条数据进入详情")
    def get_window(self):
        # 搜索物品点击物品进入新的页面获取
        self.get_windows(loc.confirm_goodsno_exist,"搜索成功列表_点击这条数据进入详情")

    def clear_input_goodno(self):
        time.sleep(1)
        self.clear_input(sloc.goods_no,"搜索页面_清空输入框")

    # 新建待交易选择新建需求
    def move_to_add_element(self):
        # 移动到添加元素上
        time.sleep(2)
        self.move_to_element(loc.add_btn,"待交易页面_移动元素到添加按钮上面")
        # ele=self.wait_element_visibility(loc.addgoods_btn,"待交易页面_移动元素到添加按钮上面")

    def click_new_business(self):
        # 点击新建需求
        # self.click_element(loc.new_business,"待交易页面_移动元素到添加按钮上面点击新建需求")
        time.sleep(2)
        ele=self.wait_element_visibility(loc.new_business,"待交易页面_移动元素到添加按钮上面点击新建需求")
        ele.click()

    # 从订单生成需求
    def purchase_from_order(self):
        time.sleep(1)
        self.click_element(loc.purchase_from_order,"待交易页面_移动元素到添加按钮上面点击订单生成")
    # 从报价生成需求
    def purchase_from_price(self):
        self.click_element(loc.purchase_from_price,"待交易页面_移动元素到添加按钮上面点击报价生成")
    # 进入首页点击订单模块
    def click_order(self):
        time.sleep(3)
        ele=self.wait_element_clickable(loc.order,"首页_点击订单模块")
        ele.click()

#     首页点击仓库管理模块
    def click_warehouse(self):
        time.sleep(2)
        ele=self.wait_element_visibility(loc.warehouse_manage,"首页_点击仓库管理模块")
        ele.click()
# 点击报价模块
    def click_quotedprice(self):
        ele=self.wait_element_visibility(loc.quoted_price,"首页_点击报价模块")
        ele.click()

