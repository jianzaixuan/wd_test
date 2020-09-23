"""
============================
Author:丁琴
Time: 17:48
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""

import pytest
from data.goods_add_case import GoodsCase
from common.handle_logging import my_log
from common.handle_db import HandleMysql


# 添加物品之前先登录,加一个类前置后置条件
class Test_Addgoods:
    # 创建操作数据库对象
    db=HandleMysql()
    # 点击加号添加物品直接保存的用例
    # @pytest.mark.skip
    # @pytest.mark.dd
    @pytest.mark.parametrize("case",GoodsCase.good_type_errorinfo_case)
    def test_type_error(self,case,goods_fixture):

    #     接收添加物品页面的对象
        addgoods, index_page = goods_fixture[0],goods_fixture[1]
        # 点击添加物品
        index_page.click_addgoods()
    #     啥也不填直接保存
        addgoods.save()
        res=addgoods.good_type_errorinfo()
    #     断言
        try:
            assert case["expected"]==res
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例---{}通过".format(case["title"]))
    #         回到物品列表
            addgoods.black_goodslist()

    # @pytest.mark.skip
    @pytest.mark.parametrize("case", GoodsCase.good_addpass_case)
    def test_pass_goodname(self, case, goods_fixture):
        #     用例执行之前查询数据库物品数量
        start_count = self.search_db()
        #     接收添加物品页面的对象
        addgoods, index_page = goods_fixture[0],goods_fixture[1]
        # 点击添加按钮
        index_page.click_addgoods()
        # 选择类型，输入品名，单位，尺寸颜色
        addgoods.choose_goodstype()
        addgoods.input_goodsname(case["goodsname"])
        addgoods.choose_unit()
        addgoods.input_clor(case["color"])
        addgoods.input_size(case["size"])

        addgoods.save()
        # 获取成功信息
        res = addgoods.good_errorinfo()
        # 刷新一下页面
        addgoods.refresh()
        #     用例执行之后查询数据库物品数量
        end_count = self.search_db()
        #     断言
        try:
            assert case["expected"] == res
            assert end_count - start_count == 1
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例---{}通过".format(case["title"]))
            # 删除物品
            addgoods.delete()

    # @pytest.mark.skip
    @pytest.mark.parametrize("case", GoodsCase.good_errorinfo_case)
    def test_errorinfo(self, case, goods_fixture):
        # 添物品失败的用例
        #     接收添加物品页面的对象
        addgoods, index_page = goods_fixture[0],goods_fixture[1]
        # 输入完整保存成功的用例
        # 点击添加按钮
        index_page.click_addgoods()
        # 选择类型，输入品名，单位，尺寸颜色
        addgoods.choose_goodstype()
        addgoods.input_goodsname(case["goodsname"])
        addgoods.choose_unit()
        addgoods.input_clor(case["color"])
        addgoods.input_size(case["size"])

        addgoods.save()
        # 获取成功信息
        res = addgoods.good_errorinfo()
        index_page.click_goods()
        #     断言
        try:
            assert case["expected"] == res
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例---{}通过".format(case["title"]))


    # @pytest.mark.skip
    @pytest.mark.parametrize("case", GoodsCase.search_goods_case)
    def test_search(self, case, goods_fixture):
        # 搜索物品
        #     接收添加物品页面的对象
        index_page = goods_fixture[1]
        # 点击搜索按钮
        # 输入搜索内容确定展示搜索结果

        index_page.search_btn()
        index_page.input_goodsno(case["goodsno"])
        index_page.search_confim_btn()
        # 获取搜索的成功数据信息
        res = index_page.confirm_goodsno_exist()
        #     断言
        try:
            assert case["expected"] == res
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例---{}通过".format(case["title"]))
    # @pytest.mark.skip
    @pytest.mark.parametrize("case", GoodsCase.delete_exsit_case)
    def test_delete_goodsexist(self, case, goods_fixture):
        # 搜索物品作废
        #     接收添加物品页面的对象
        addgoods, index_page = goods_fixture[0],goods_fixture[1]
        # 点击搜索按钮
        # 输入搜索内容确定展示搜索结果
        index_page.search_btn()
        index_page.clear_input_goodno()
        index_page.input_goodsno(case["goodsno"])
        index_page.search_confim_btn()
        # 获取搜索的成功数据信息点击进入物品详情页面操作作废，这个物品是要进入一个新的页面，先调用获取新窗口的方法切换到新页面再去操作
        index_page.get_windows()
        # 详情点击作废
        addgoods.use_delete()
        res=addgoods.good_errorinfo()
        #     断言
        try:
            assert case["expected"] == res
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例---{}通过".format(case["title"]))
    @classmethod
    def search_db(cls):
        # 添加物品之前查询一下该用户新建的物品数量
        sql = "SELECT * FROM wd.t_goods WHERE user_id='510c0631527243788fdb74a14e24bac2'"
        count=cls.db.find_count(sql)
        return count
