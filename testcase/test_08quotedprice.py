"""
============================
Author:丁琴
Time: 17:22
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import pytest
from common.handle_logging import my_log
from data.quotedprice_data import QuotedpriceCase
class Test_Quotedprice:
    @pytest.mark.parametrize("case",QuotedpriceCase.type_goodsno_data)
    def test_goodsno_data(self,case,quotedprice_fixture):
        global text
        business_page, quotedprice_page=quotedprice_fixture[1],quotedprice_fixture[2]

        if case["title"]=="物料号为空":
            # 首页点击添加按钮
            quotedprice_page.click_add()
            # 点击确定
            quotedprice_page.click_confirm()
            text=quotedprice_page.get_goodsno_error()
        if case["title"]=="选择物品创建报价成功":
            quotedprice_page.type_goodsno(case["goods_no"])
            quotedprice_page.click_search()
            quotedprice_page.click_checkbox()
            quotedprice_page.click_confirm()
            text=quotedprice_page.get_create_price_toast()
        # 断言
        try:
            assert case["excepted"] == text
        except  AssertionError as e:
            my_log.error("用例--{}--不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例--{}--通过".format(case["title"]))