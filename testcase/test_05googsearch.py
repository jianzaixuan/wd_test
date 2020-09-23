"""
============================
Author:丁琴
Time: 12:14
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import pytest
from data.goods_search_data import GoodSearchcase
from common.handle_logging import my_log

class Test_Goodssearch:
    # 通过品名搜索
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case",GoodSearchcase.product_name_data)
    def test_product_name(self,case,goods_fixture):
        index_page,search_page=goods_fixture[1],goods_fixture[2]
        # 首页点击
        index_page.search_btn()
        # 输入品名，确定
        search_page.product_name_search(case["product_name"])
        search_page.click_confim()
#         获取页面的product_name的个数
        res_count=search_page.get_pagesource_str(case["product_name"])
        #     断言
        try:
            assert case["excepted"] == res_count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 通过物料号搜索
    @pytest.mark.parametrize("case",GoodSearchcase.goods_no_data)
    def test_goods_no(self,case,goods_fixture):
        index_page,search_page=goods_fixture[1],goods_fixture[2]
        # 在上一次搜索后刷新一下页面清掉之前搜索的数据
        search_page.refresh_page()
        # 首页点击
        index_page.search_btn()
        # 输入品名，确定
        search_page.goods_no_search(case["goods_no"])
        search_page.click_confim()
#         获取页面的goods_no的个数
        res_count=search_page.get_pagesource_str(case["goods_no"])
        #     断言
        try:
            assert case["excepted"] == res_count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索往来物料号
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", GoodSearchcase.transaction_no_data)
    def test_transaction_no(self, case, goods_fixture):
        index_page, search_page = goods_fixture[1], goods_fixture[2]
        # 在上一次搜索后刷新一下页面清掉之前搜索的数据
        search_page.refresh_page()
        # 首页点击
        index_page.search_btn()
        # 输入品名，确定
        search_page.transaction_no(case["transaction_no"])
        search_page.click_confim()
        #         获取页面的transaction_no的个数
        res_count = search_page.get_pagesource_str(case["transaction_no"])
        #     断言
        try:
            assert case["excepted"] == res_count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索创建人
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", GoodSearchcase.creater_data)
    def test_creater(self, case, goods_fixture):
        index_page, search_page = goods_fixture[1], goods_fixture[2]
        # 在上一次搜索后刷新一下页面清掉之前搜索的数据
        search_page.refresh_page()
        # 首页点击
        index_page.search_btn()
        # 输入创建人，确定
        search_page.creater(case["creater"])
        search_page.click_confim()
        # #         获取页面的creater的个数
        res_count = search_page.get_pagesource_str(case["creater"])
        #     断言
        try:
            assert case["excepted"] == res_count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
        # 搜索创建人
        # @pytest.mark.goodno
    # 搜索往来单位
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", GoodSearchcase.contact_unit_data)
    def test_contact_unit(self, case, goods_fixture):
        index_page, search_page = goods_fixture[1], goods_fixture[2]
        # 在上一次搜索后刷新一下页面清掉之前搜索的数据
        search_page.refresh_page()
        # 首页点击
        index_page.search_btn()
        # 输入往来单位，确定
        search_page.contact_unit(case["contact_unit"])
        search_page.click_confim()
        #        搜索到物品点击一个物品进入详情查看报价记录是否有该单位的名称字样
        text=search_page.get_contact_unit_info()
            # 需要再返回物品列表，不然下一条用例还是在详情刷新

            # 断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索备注
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", GoodSearchcase.remarks_data)
    def test_remarks(self, case, goods_fixture):
        index_page, search_page = goods_fixture[1], goods_fixture[2]
        # 在上一次搜索后刷新一下页面清掉之前搜索的数据
        search_page.refresh_page()
        # 首页点击
        index_page.search_btn()
        # 输入备注，确定
        search_page.remarks(case["remarks"])
        search_page.click_confim()
        # 搜索到数据后点击一条进入详情查看备注tab是否有该备注信息
        text=search_page.get_remark_info()
            # 断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索标签
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", GoodSearchcase.label_data)
    def test_label(self, case, goods_fixture):
        index_page, search_page = goods_fixture[1], goods_fixture[2]
        # 在上一次搜索后刷新一下页面清掉之前搜索的数据
        search_page.refresh_page()
        # 首页点击
        index_page.search_btn()
        # 输入标签，确定
        search_page.label(case["label"])
        search_page.click_confim()
        # 搜索到数据后点击一条进入详情查看标签是否存在
        text=search_page.get_label_info()
        # 断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索创建时间
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", GoodSearchcase.create_time)
    def test_create_time(self, case, goods_fixture):
        index_page, search_page = goods_fixture[1], goods_fixture[2]
        # 在上一次搜索后刷新一下页面清掉之前搜索的数据
        search_page.refresh_page()
        # 首页点击
        index_page.search_btn()
        # 输入时间，确定
        search_page.start_end_time()
        search_page.click_confim()
        # 搜索到数据后点击一条进入详情查看标签是否存在
        count=search_page.get_pagetime_str(case["starttime"],case["endtime"])
        # 断言
        try:
            assert case["excepted"] == count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # 搜索物品类型
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case",GoodSearchcase.goostype_data)
    def test_good_type(self,case,goods_fixture):
        global text
        index_page, search_page = goods_fixture[1], goods_fixture[2]
        search_page.refresh_page()
        # 首页点击搜索
        index_page.search_btn()
        if case["title"]=="搜索服装类型":
            search_page.click_clothing_type()
            # 点击确定按钮
            search_page.click_confim()
            text=search_page.get_lowpage_clothingtype()
        elif case["title"]=="搜索面料类型":
            search_page.click_fabric_type()
            # 点击确定按钮
            search_page.click_confim()
            text=search_page.get_lowpage_fabrictype()
        elif case["title"]=="搜索里料类型":
            search_page.click_lining_type()
            # 点击确定按钮
            search_page.click_confim()
            text=search_page.get_lowpage_liningtype()
        # 断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))


    # 搜索不存在的品名
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", GoodSearchcase.error_product_name)
    def test_error_product_name(self, case, goods_fixture):
        index_page, search_page = goods_fixture[1], goods_fixture[2]
        # 在上一次搜索后刷新一下页面清掉之前搜索的数据
        search_page.refresh_page()
        # 首页点击搜索
        index_page.search_btn()
        # 输入不存在的品名error_product_name，确定
        search_page.product_name_search(case["product_name"])
        search_page.click_confim()
        # 搜索到数据后判断是否存在
        count=search_page.get_exsit_product_name(case["product_name"])
        # 断言
        try:
            assert case["excepted"] == count
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))