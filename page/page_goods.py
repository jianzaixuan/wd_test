"""
============================
Author:丁琴
Time: 12:26
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""

from selenium.webdriver import Chrome

from common.basepage import BasePage
from locator.goods_locator import GoodsLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
class AddGoods(BasePage):

    def choose_goodstype(self):
        # 点击物品类型
        time.sleep(1)

        self.click_element(loc.goods_type_btn,"物品详情页面_点击物品类型")
        # 选择一个物品类型
        self.click_element(loc.choose_goodstype,"物品详情页面_选择物品类型")
    def input_goodsname(self,goodsname):
        # 输入物品名称
        self.input_text(loc.goods_name,goodsname,"物品详情页面_输入物品名称")
    def choose_unit(self):
#         点击单位
        time.sleep(1)
        self.click_element(loc.unit_btn,"物品详情页面_点击单位")
#     选择单位
        self.click_element(loc.choose_unit,"物品详情页面_选择单位")
    def input_clor(self,color):
# #         输入颜色内容
        self.input_text(loc.input_clor,color,"物品详情页面_输入颜色内容")

    def input_size(self,size):
#         点击尺码元素
#         time.sleep(1)
        self.click_element(loc.click_btn,"物品详情页面_点击尺码元素")
#         输入尺码
#         time.sleep(2)
        self.input_text(loc.size_btn,size,"物品详情页面_输入尺码内容")
    def save(self):
#     保存
        time.sleep(1)
        self.click_element(loc.save,"物品详情页面_点击保存")
    def good_type_errorinfo(self):
        # 物品类型为空提示信息
        time.sleep(1)
        # ele=self.wait_element_visibility(loc.good_type_errorinfo,"物品详情页面_没有选择物品类型错误提示")
        # return ele.text
        text=self.get_element_text(loc.good_type_errorinfo,"物品详情页面_没有选择物品类型错误提示")
        return text

    def good_errorinfo(self):
        # 添加物品失败错误提示信息
        # time.sleep(1)
        text=self.get_element_text(loc.good_errorinfo,"物品详情页面_添加物品失败错误提示信息")
        return text
    # def goods_errorinfo(self):
    #     # 规格有一个内容没填错误提示信息
    #     # time.sleep(1)
    #     text=self.get_element_text(loc.goodstype_errorinfo,"物品详情页面_尺码规格没有输入内容")
    #     return text
    #
    # def save_success(self):
    #     # 保存成功提示信息
    #     time.sleep(1)
    #     text=self.get_element_text(loc.save_success,"物品详情页面_保存成功提示信息")
    #     return text

    def delete(self):
#         点击状态选择作废然后点击保存，弹框确认
        time.sleep(1)
        self.click_element(loc.normal_status,"物品详情页面_点击状态")
        self.click_element(loc.delete_status,"物品详情页面_选择作废状态")
        # 直接调用保存的方法
        self.save()
        ele=self.wait_element_clickable(loc.goods_delete_confirm,"物品详情页面_选择作废状态点击确认按钮")
        ele.click()
        # self.click_element(loc.goods_delete_confirm,"物品详情页面_选择作废状态点击确认按钮")
    #     作废成功点击物品返回到列表界面
        self.black_goodslist()
    def black_goodslist(self):
#         点击物品返回到物品列表
        time.sleep(2)
        self.click_element(loc.click_goods,"物品详情页面_点击物品返回到物品列表")
    def refresh(self):
#         刷新页面
        self.driver.refresh()

    def use_delete(self):
#         点击状态选择作废然后点击保存，弹框确认
        time.sleep(1)
        self.click_element(loc.use_normal_status,"物品详情页面_点击状态")
        self.click_element(loc.delete_status,"物品详情页面_选择作废状态")
        # 直接调用保存的方法
        self.save()


