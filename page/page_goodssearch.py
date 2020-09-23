"""
============================
Author:丁琴
Time: 10:48
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""


from common.basepage import BasePage
from locator.search_locator import Search_Locator as loc
import time
class Good_Search(BasePage):
    # # 进入物品模块点击搜索按钮
    # def click_search_button(self):
    #     ele=self.wait_element_clickable(loc.search_goods_btn,"物品_点搜索按钮")
    #     ele.click()

#     def goodtype_search(self):
# #         物品类型搜索
#         ele=self.wait_element_clickable(loc.goods_type,"搜索页面_点击物品类型搜索选择框")
#         ele.click()
#     def choose_clothing_type(self):
# #         选择服装类型
#         ele=self.wait_element_clickable(loc.clothing_type,"搜索页面_点击物品类型搜索选择框后选择服装类型")
#         ele.click()
    def product_name_search(self,product_name):
        # 输入品名搜索
        self.clear_input(loc.product_name,"搜索页面_清空品名输入框")
        self.input_text(loc.product_name,product_name,"搜索页面_输入品名")

    def goods_no_search(self,goods_no):
        # 输入物料号搜索
        self.clear_input(loc.goods_no,"搜索页面_清空物料号输入框")
        self.input_text(loc.goods_no,goods_no,"搜索页面_输入物料号")

    def transaction_no(self,transaction_no):
        # 输入往来物料号搜索
        self.clear_input(loc.transaction_no,"搜索页面_清空往来物料号输入框")
        self.input_text(loc.transaction_no,transaction_no,"搜索页面_输入往来物料号")
    def creater(self,creater):
        # 输入创建人搜索
        self.clear_input(loc.creater,"搜索页面_清空创建人输入框")
        self.input_text(loc.creater,creater,"搜索页面_输入创建人")
    def contact_unit(self,contact_unit):
        # 输入往来单位搜索
        self.clear_input(loc.contact_unit,"搜索页面_清空往来单位输入框")
        self.input_text(loc.contact_unit,contact_unit,"搜索页面_输入往来单位")
    def remarks(self,remarks):
        # 输入往来单位搜索
        self.clear_input(loc.remarks,"搜索页面_清空备注输入框")
        self.input_text(loc.remarks,remarks,"搜索页面_输入备注")
    def label(self,label):
        # 输入往来单位搜索
        self.clear_input(loc.label,"搜索页面_清空标签输入框")
        self.input_text(loc.label,label,"搜索页面_输入标签")
    def start_end_time(self):

        start_time=self.wait_element_visibility(loc.start_time,"搜索页面_等待开始时间元素可见")
        end_time=self.wait_element_visibility(loc.end_time,"搜索页面_等待结束时间元素可见")
        js="""
        var data0=arguments[0];
        var data1=arguments[1];
        data0.readonly=false;
        data0.value='2020-08-02'
        data1.readonly=false;
        data1.value='2020-08-14'
        """
        self.driver.execute_script(js,start_time,end_time)

    def click_confim(self):
#         输入选择添加后点击确定按钮
        self.click_element(loc.search_confim_btn,"搜索页面_点击确定")
    def refresh_page(self):
        time.sleep(5)
        self.refresh()
    def get_pagesource_str(self,name):
    # 获取页面出现的字符串个数
    # 先获取页面源代码
        time.sleep(5)
        count_str=self.get_page_str(name,"搜索出现的页面_获取字符串个数")
        return count_str
    def get_maxpagesource_strs(self,name):
#         页面滑动到最大高度查找搜索的字符串，找到说明搜索成功
        name=self.get_maxpage_str(name,"搜索出现的页面_页面滑动到最大高度获取字符串存在")
        return name

#     点击一条物品记录获取新窗口，进入新窗口点击报价记录获取相关的往来单位字样
    def get_contact_unit_info(self):
# 先获取第一个出现的窗口句柄
        window1=self.driver.current_window_handle
#         等待元素出现点击切换窗口
        self.get_windows(loc.unit_googsno,"物品搜索列表_点击搜索的物品")
        # time.sleep(5)
        # ele=self.wait_element_visibility(loc.price_record,"物品详情页面_点击报价记录")
        # ele.click()
        ele=self.wait_element_clickable(loc.price_record,"物品详情页面_点击报价记录")
        ele.click()
        text=self.get_element_text(loc.contact_unit_confim,"物品详情页面_获取企业名称")
        # 关闭窗口，切换到之前的窗口
        self.driver.close()
        self.driver.switch_to_window(window1)
        return text
    def get_remark_info(self):
        # 先获取第一个出现的窗口句柄
        window1 = self.driver.current_window_handle
        # 进入物品详情确认备注信息是否存在
        self.get_windows(loc.unit_googsno,"物品搜索列表_点击搜索的物品")
        ele=self.wait_element_clickable(loc.remarks_tab,"物品详情页面_点击备注")
        ele.click()
        text=self.get_element_attr(loc.remarks_confim,"value","物品详情页面_备注存在")
        # 关闭窗口，切换到之前的窗口
        self.driver.close()
        self.driver.switch_to_window(window1)
        return text
    def get_label_info(self):
# 先获取第一个出现的窗口句柄
        window1=self.driver.current_window_handle
#         搜索的物品进入详情确认标签是否存在
        self.get_windows(loc.label_goodno,"物品列表页面——点击物品")
        text=self.get_element_attr(loc.label_confim,"value","物品详情页面_标签是否存在")
        # 关闭窗口，切换到之前的窗口
        self.driver.close()
        self.driver.switch_to_window(window1)
        return text
    def get_pagetime_str(self,starttime,endtime):
        count=self.get_time_str(starttime,endtime,"物品搜索列表_搜索的时间数据显示")
        return count

    def get_exsit_product_name(self,name):
        count=self.get_page_str(name,"物品搜索页面_搜索列表品名不存在")
        return count

    def click_search_input(self):
        # 进入搜索页面先点击类型框
        ele=self.wait_element_clickable(loc.goods_type,"物品搜索页面_点击物品类型搜索框")
        ele.click()
    def click_clothing_type(self):
        # 点击类型框
        self.click_search_input()
#         选择服装类型
        ele=self.wait_element_clickable(loc.clothing_type,"物品搜索页面_点击物品服装类型")
        ele.click()
    def get_lowpage_clothingtype(self):
        text=self.get_element_text(loc.low_clothing_type,"物品列表页面_获取页面最底部的服装类型文本")
        return text
    def click_fabric_type(self):
        # 点击类型框
        self.click_search_input()
        #         选择面料类型
        ele = self.wait_element_clickable(loc.fabric_type, "物品搜索页面_点击物品面料类型")
        ele.click()
    def get_lowpage_fabrictype(self):
        text=self.get_element_text(loc.low_fabric_type,"物品列表页面_获取页面最底部的面料类型文本")
        return text
    def click_lining_type(self):
        # 点击类型框
        self.click_search_input()
        #         选择里料类型
        ele = self.wait_element_clickable(loc.lining_type, "物品搜索页面_点击物品里料类型")
        ele.click()
    def get_lowpage_liningtype(self):
        text=self.get_element_text(loc.low_lining_type,"物品列表页面_获取页面最底部的面料类型文本")
        return text




