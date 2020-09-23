"""
============================
Author:丁琴
Time: 13:47
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import time

from selenium.webdriver import Chrome
from common.basepage import BasePage
from locator.business_locator import AddBusinesslocator as loc
class AddBusiness(BasePage):

    def choose_bustype(self):
        # 选择交易类型
        time.sleep(1)
        self.click_element(loc.click_business_type,"新建需求界面_点击类型")
        self.click_element(loc.buy_type,"新建需求界面_选择采购类型")
    def click_goods_btn(self):
        # 选择物品
        self.click_element(loc.choose_goods,"新建需求界面_点击品名进入选择物品界面去")
    def choose_goods(self,goodsno):

        time.sleep(1)
        self.input_text(loc.search_goodsno,goodsno,"选择物品界面_输入物料号")
        self.click_element(loc.search_btn,"选择物品界面_点击搜索")
        time.sleep(3)
        self.click_element(loc.choose_checkbox,"选择物品界面_勾选物品的选择框")
        self.click_element(loc.goods_confirm_btn,"选择物品界面_点击确定")
    def save(self):
        time.sleep(2)
        self.click_element(loc.save,"需求详情页面_保存")
    def toast_info(self):
        ele=self.wait_element_presence(loc.toast_info,"需求详情页面_toast提示信息")
        res=ele.text
        return res
    def input_number(self,input_number1,input_number2,input_number3,input_number4):
        # 输入数量
        self.input_text(loc.input_number1,input_number1,"需求详情页面_输入数量1")
        self.input_text(loc.input_number2, input_number2,"需求详情页面_输入数量2")
        self.input_text(loc.input_number3, input_number3,"需求详情页面_输入数量3")
        self.input_text(loc.input_number4, input_number4,"需求详情页面_输入数量4")
    def input_price(self,price):
        # 点击价格条款输入价格
        self.click_element(loc.price_btn,"需求详情页面_点击价格条款")
        self.input_text(loc.input_price,price,"需求详情页面_输入单价")

    def click_material(self):
#         点击材料单
        # self.click_element(loc.click_material,"需求详情页面材料单页面_点击材料单")
        ele=self.wait_element_clickable(loc.click_material,"需求详情页面材料单页面_点击材料单")
        ele.click()
        self.click_element(loc.click_add_btn,"需求详情页面材料单页面_点击添加按钮")

    def click_material_color(self):
        self.click_element(loc.material_btn,"需求详情页面材料单页面_点击配色配码按钮")
        self.click_element(loc.material_color1,"需求详情页面材料单页面_点击配色配码1")
        self.click_element(loc.choose_color1,"需求详情页面材料单页面_点击配色配码选择颜色1")
        self.click_element(loc.material_color2,"需求详情页面材料单页面_点击配色配码2")
        time.sleep(1)
        self.click_element(loc.choose_color2,"需求详情页面材料单页面_点击配色配码选择颜色2")
        self.click_element(loc.material_confirm,"需求详情页面材料单页面_点击配色配码选择颜色后确定")
    def input_consumption(self,Unit_consumption,loss):
#         输入单耗损耗
        self.input_text(loc.Unit_consumption,Unit_consumption,"需求详情页面材料单页面_输入单耗")
        self.input_text(loc.loss,loss,"需求详情页面材料单页面_输入损耗")

    def click_purchase(self):
#         点击采购
#         self.click_element(loc.purchase_btn,"需求详情页面材料单页面_点击采购")
        ele=self.wait_element_clickable(loc.purchase_btn,"需求详情页面材料单页面_点击采购")
        ele.click()

        # 点击待采购tab
        self.click_element(loc.click_purchase,"需求详情页面材料单页面_点击待采购")
    def get_text_info(self):
#         获取待采购是否有该物料号文本信息
        text=self.get_element_text(loc.purchase_no,"需求详情页面待采购页面_获取物料号文本信息")
        return text


    def delete_data(self):
#         删除待采购数据已经子数据
        time.sleep(3)
        self.click_element(loc.delete_btn,"需求详情页面_删除")

        # ele=self.wait_element_clickable(loc.delete_btn,"需求详情页面_删除")
        # ele.click()
        # self.click_element(loc.confirm_btn,"需求详情页面_确认删除")
        ele=self.wait_element_clickable(loc.confirm_btn,"需求详情页面_确认删除")
        ele.click()

    def click_purchase_data(self):
#         回到列表点击第一条数据进入详情删除
#         self.click_element(loc.purchase_data,"需求列表页面_点击需求")
#         time.sleep(3)
        ele=self.wait_element_clickable(loc.purchase_data,"需求列表页面_点击需求")
        ele.click()


    def choose_goods_order(self, orderno):
        # 从订单选择弹框中搜索物料号
        time.sleep(1)
        # self.input_text(loc.search_goodsno_order, goodsno, "选择物品界面_输入物料号")
        ele=self.wait_element_clickable(loc.search__order_no, "选择物品界面_输入物料号")
        ele.send_keys(orderno)
        self.click_element(loc.search_btn, "选择物品界面_点击搜索")
        time.sleep(3)
        self.click_element(loc.choose_checkbox, "选择物品界面_勾选物品的选择框")
        self.click_element(loc.goods_confirm_btn, "选择物品界面_点击确定")
    def choose_goods_price(self, cometogoodsno):
        # 从报价选择弹框中搜索物料号
        time.sleep(1)
        # self.input_text(loc.search_goodsno_order, goodsno, "选择物品界面_输入物料号")
        ele=self.wait_element_clickable(loc.search_price_no, "选择物品界面_输入物料号")
        ele.send_keys(cometogoodsno)
        time.sleep(3)
        self.click_element(loc.search_btn_price, "选择物品界面_点击搜索")
        time.sleep(3)
        self.click_element(loc.choose_checkbox, "选择物品界面_勾选物品的选择框")
        self.click_element(loc.goods_confirm_price_btn, "选择物品界面_点击确定")