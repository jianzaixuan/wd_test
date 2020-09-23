"""
============================
Author:丁琴
Time: 11:12
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import pytest
from data.order_search_data import OrderSearchcase
from common.handle_logging import my_log
# import sys
# sys.setrecursionlimit(1000000)
class Test_OrderSearch:
    # 搜索品名
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case",OrderSearchcase.order_no_data)
    def test_order_no(self,case,order_fixture):
        index_page,order_search=order_fixture[0],order_fixture[2]
        # 点击搜索
        index_page.search_btn()
        order_search.order_no_search(case["order_no"])
        order_search.click_confim()
        # 获取页面的订单号字符串个数
        count=order_search.get_orderno_info(case["order_no"])
#         断言
        try:
            assert case["excepted"]==count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))

    # 搜索主题
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case",OrderSearchcase.order_theme_data)
    def test_order_theme(self,case,order_fixture):
        index_page,order_search=order_fixture[0],order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        order_search.order_theme_search(case["theme"])
        order_search.click_confim()
        # 获取页面的主题字符串个数
        count=order_search.get_ordertheme_info(case["theme"])
#         断言
        try:
            assert case["excepted"]==count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))

  # 搜索品名
  #   @pytest.mark.goodno
    @pytest.mark.parametrize("case",OrderSearchcase.product_name_data)
    def test_product_name(self,case,order_fixture):
        index_page,order_search=order_fixture[0],order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        order_search.product_name_search(case["product_name"])
        order_search.click_confim()
        # 获取页面的品名字符串个数
        count=order_search.get_productname_info(case["product_name"])
#         断言
        try:
            assert case["excepted"]==count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))

    # 搜索物料号
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderSearchcase.goods_no_data)
    def test_goods_no(self, case, order_fixture):
        index_page, order_search = order_fixture[0], order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        order_search.goods_no_search(case["goods_no"])
        order_search.click_confim()
        # 获取页面的物料号订单号字符串个数
        result = order_search.get_goodsno_info(case["goods_no"])
        #         断言
        try:
            assert case["excepted"] == result
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索往来物料号
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderSearchcase.transaction_no_data)
    def test_transaction_no(self, case, order_fixture):
        index_page, order_search = order_fixture[0], order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        order_search.transaction_no_search(case["transaction_no"])
        order_search.click_confim()
        # 获取页面的往来物料号字符串个数
        result = order_search.get_transactionno_info(case["transaction_no"])
        #         断言
        try:
            assert case["excepted"] == result
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索创建人
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderSearchcase.creater_data)
    def test_creater(self, case, order_fixture):
        index_page, order_search = order_fixture[0], order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        order_search.creater_search(case["creater"])
        order_search.click_confim()
        # 获取页面的创建人字符串个数
        result = order_search.get_creater_info(case["creater"])
        #         断言
        try:
            assert case["excepted"] == result
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索往来单位
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderSearchcase.contact_unit_data)
    def test_contactunit(self, case, order_fixture):
        index_page, order_search = order_fixture[0], order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        order_search.contact_unit_search(case["contact_unit"])
        order_search.click_confim()
        # 获取页面的创建人字符串个数
        result = order_search.get_contactunit_info(case["contact_unit"])
        #         断言
        try:
            assert case["excepted"] == result
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索物品类型
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderSearchcase.goods_type_data)
    def test_goods_type(self, case, order_fixture):
        global text
        index_page, order_search = order_fixture[0], order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        if case["title"]=="搜索服装类型":
            order_search.choose_clothing_type()
            order_search.click_confim()
            # 获取页面字符串是否存在
            text=order_search.get_page_info(case["clothing_type"])
        elif case["title"]=="搜索面料类型":
            order_search.choose_fabric_type()
            order_search.click_confim()
            # 获取页面字符串是否存在
            text=order_search.get_page_info(case["fabric_type"])
        elif case["title"]=="搜索里料类型":
            order_search.choose_lining_type()
            order_search.click_confim()
            # 获取页面字符串是否存在
            text=order_search.get_page_info(case["lining_type"])
        #         断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索订单类型
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderSearchcase.order_type_data)
    def test_order_type(self, case, order_fixture):
        global text
        index_page, order_search = order_fixture[0], order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        if case["title"]=="搜索采购类型":
            order_search.choose_order_purchase()
            order_search.click_confim()
            # 获取页面字符串是否存在
            text=order_search.get_page_info(case["purchase_type"])
        elif case["title"]=="搜索销售类型":
            order_search.choose_order_sale()
            order_search.click_confim()
            # 获取页面字符串是否存在
            text=order_search.get_page_info(case["sale_type"])
        #         断言
        try:
            case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索订单编号不存在
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderSearchcase.fail_search)
    def test_fail_search(self, case, order_fixture):
        index_page, order_search = order_fixture[0], order_fixture[2]
        # 刷新页面
        order_search.refresh_page()
        # 点击搜索
        index_page.search_btn()
        order_search.order_no_search(case["name"])
        order_search.click_confim()
        # 获取页面字符串是否存在
        text=order_search.get_page_info(case["name"])

        #         断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))