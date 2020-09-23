"""
============================
Author:丁琴
Time: 10:15
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from common.basepage import BasePage
from locator.goods_locator import GoodsLocator as loc
import time
class GoodsList(BasePage):

    def click_goodslist_data(self):
    #     点击第一条物品数据进入详情
        time.sleep(2)
        self.click_element(loc.list_goodsdata,"物品列表页面_点击一个物品")

