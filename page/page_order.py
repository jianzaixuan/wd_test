"""
============================
Author:丁琴
Time: 11:42
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from common.basepage import BasePage
from locator.order_locator import Order_locator as loc
from locator.index_locator import IndexLocator as loc_index
import time
class Order_Page(BasePage):

    # 鼠标移动到加号
    def move_to_add(self):
        self.move_to_element(loc_index.add_btn,"首页_鼠标移动到订单添加按钮上面")
#     需求生成订单
    def order_from_requirement(self,requirement_no):
        time.sleep(3)
        self.move_to_add()
        ele=self.wait_element_visibility(loc_index.purchase_from_business,"首页_新建订单选择从需求生成")
        ele.click()
        self.input_requirement_no(requirement_no)
        self.search_requirement_btn()
        self.choose_requirement_box()
        self.confirm_requirement_btn()
    #     需求生成订单，没有选择需求确定
    def order_from_requirementerror(self, requirement_no):
        time.sleep(3)
        self.move_to_add()
        ele = self.wait_element_visibility(loc_index.purchase_from_business, "首页_新建订单选择从需求生成")
        ele.click()
        self.input_requirement_no(requirement_no)
        self.search_requirement_btn()
        self.confirm_requirement_btn()
    #     下面是共同的操作方法
    def input_requirement_no(self,requirement_no):
        self.clear_input(loc.requirement_number,"弹出需求选择页面_情空输入框")
        self.input_text(loc.requirement_number,requirement_no,"弹出需求选择页面_输入需求编号")
    def search_requirement_btn(self):
        ele=self.wait_element_clickable(loc.search_btn_requirement,"弹出需求选择页面_点击搜索按钮")
        ele.click()
    def choose_requirement_box(self):
        time.sleep(2)
        ele=self.wait_element_clickable(loc.choose_checkbox,"弹出需求选择页面_点击选择框")
        ele.click()
    def confirm_requirement_btn(self):
        self.click_element(loc.confirm_requirement_btn,"弹出需求选择页面_点击确定按钮")
    def close_requirement_btn(self):
        self.click_element(loc.close_alert_requirement,"弹出需求选择页面_点击关闭按钮")
#     报价生成订单
    def order_from_price(self,transaction_no):
        time.sleep(3)
        self.move_to_add()
        ele=self.wait_element_visibility(loc_index.purchase_from_price,"首页_新建订单选择从报价生成")
        ele.click()
        self.input_transaction_no(transaction_no)
        self.search_transaction_btn()
        time.sleep(2)
        self.choose_transaction_box()
        self.confirm_transaction_btn()
    #     报价生成订单,没有选择报价点击确定
    def order_from_priceerror(self, transaction_no):
        time.sleep(1)
        self.move_to_add()
        ele = self.wait_element_visibility(loc_index.purchase_from_price, "首页_新建订单选择从报价生成")
        ele.click()
        self.input_transaction_no(transaction_no)
        self.search_transaction_btn()
        time.sleep(1)
        self.confirm_transaction_btn()
    #     下面是共同的操作方法
    def input_transaction_no(self,transaction_no):
        self.clear_input(loc.transaction_no,"弹出报价选择页面_清空往来物料号输入框")
        self.input_text(loc.transaction_no,transaction_no,"弹出报价选择页面_输入往来物料号")
    def search_transaction_btn(self):
        ele=self.wait_element_clickable(loc.search_btn_transaction,"弹出报价选择页面_点击搜索按钮")
        ele.click()
    def choose_transaction_box(self):
        self.click_element(loc.contract_choose_checkbox,"弹出报价选择页面_点击选择框")
    def confirm_transaction_btn(self):
        self.click_element(loc.confirm_price_btn,"弹出报价选择页面_点击确定按钮")
    def close_price_btn(self):
        self.click_element(loc.close_alert_price,"弹出报价选择页面_点击关闭按钮")


#     从合同生成订单
    def order_from_contract(self,contract_no):
        time.sleep(3)
        self.move_to_add()
        ele = self.wait_element_visibility(loc_index.purchase_from_contract, "首页_新建订单选择从合同生成")
        ele.click()
        self.input_contract_no(contract_no)
        self.search_contract_btn()
        self.choose_contract_box()
        self.confirm_contract_btn()
    #     从合同生成订单，没有选择合同确定
    def order_from_contracterror(self, contract_no):
        self.driver.refresh()
        time.sleep(3)
        self.move_to_add()
        ele = self.wait_element_visibility(loc_index.purchase_from_contract, "首页_新建订单选择从合同生成")
        ele.click()
        self.input_contract_no(contract_no)
        self.search_contract_btn()
        time.sleep(1)
        self.confirm_contract_btn()
        # time.sleep(2)
        # self.close_contract_btn()
    #     下面是共同的操作方法
    def input_contract_no(self, contract_no):
        time.sleep(2)
        self.clear_input(loc.contract_no, "弹出合同选择页面_清空合同号输入框")
        self.input_text(loc.contract_no, contract_no, "弹出合同选择页面_输入合同号")
    def search_contract_btn(self):
        ele = self.wait_element_clickable(loc.search_btn_contract, "弹出合同选择页面_点击搜索按钮")
        ele.click()
    def choose_contract_box(self):
        time.sleep(2)
        # ele = self.wait_element_clickable(loc.contract_choose_checkbox, "弹出合同选择页面_点击选择框")
        # ele.click()
        self.click_element(loc.contract_choose_checkbox, "弹出合同选择页面_点击选择框")
    def confirm_contract_btn(self):
        self.click_element(loc.confirm_contract_btn, "弹出合同选择页面_点击确定按钮")
    def close_contract_btn(self):
        ele=self.wait_element_presence(loc.close_alert_contract,"弹出合同选择页面_点击关闭按钮")
        ele.click()
    # 添加订单成功提示信息
    def success_toast(self):
        text=self.get_element_text(loc.success_toast,"首页_新建订单成功弹出提示信息")
        return text
#     从需求拉取订单，没有选择需求确定错误提示
    def get_error_requirement(self):
        ele=self.wait_element_presence(loc.error_requirement,"新建订单选择需求页面_没有选择需求点击确定")
        text=ele.text
        return text

    #     从报价拉取订单，没有选择报价确定错误提示
    def get_error_price(self):
        text=self.get_element_text(loc.error_price,"新建订单选择报价页面_获取错误信息的元素的文本")
        return text

    #     从合同拉取订单，没有选择合同确定错误提示
    def get_error_contract(self):
        text=self.get_element_text(loc.error_contract, "新建订单选择合同求页面_没有选择合同点击确定")
        return text
    # 删除订单
    def delete_order(self):
        time.sleep(2)
        ele=self.wait_element_clickable(loc.first_order,"订单列表界面_点击第一条订单进入详情")
        ele.click()
        time.sleep(1)
        self.click_element(loc_index.common_delete_btn,"订单详情页面_点击删除")
        self.click_element(loc.delete_order_confim,"订单详情页面_点击删除后确认")
    def toast_text(self):
        text=self.get_element_text(loc.toast_info,"订单详情页面_点击删除或者保存成功后提示信息")
        return text

#     编辑订单
    def edit_order(self,num,price):
        time.sleep(2)
#         点击一条订单进入详情
        ele=self.wait_element_visibility(loc.first_order,"订单列表界面_点击一条订单进入详情")
        ele.click()
        self.input_ordernum(num)
        self.click_element(loc.price_tab,"订单详情页面_点击价格条款")
        self.input_price(price)
        self.click_element(loc_index.common_save,"订单详情页面_点击保存按钮")

#     输入数量和价格
    def input_ordernum(self,num):
        time.sleep(1)
        self.double_click_element(loc.input_ordernum, "订单列表界面_双击输入框")
        self.input_text(loc.input_ordernum,num,"订单列表界面_输入数量")
    def input_price(self,price):
        time.sleep(1)
        self.double_click_element(loc.input_orderprice, "订单列表价格条款界面_输入价格")
        self.input_text(loc.input_orderprice, price, "订单列表价格条款界面_输入价格")


