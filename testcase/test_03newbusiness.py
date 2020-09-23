"""
============================
Author:丁琴
Time: 14:24
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import  pytest

from common.handle_db import HandleMysql
from common.handle_logging import my_log
from data.business_case import AddBusiness

class TestAddbusiness:
    # 创建操作数据库对象
    db=HandleMysql()
    # @pytest.mark.dd
    @pytest.mark.parametrize("case",AddBusiness.business_pass_case)
    def test_addbusiness(self,case,business_fixture):
        index_page,add_business=business_fixture
        # 移动到添加按钮选择新建需求
        index_page.move_to_add_element()
        index_page.click_new_business()
#         新增数据之前查询一下数据
        start_num=self.search_db()
#         选择类型，选择物品，保存
        add_business.choose_bustype()
        add_business.click_goods_btn()
        add_business.choose_goods(case["goodsno"])
        add_business.input_number(case["number1"],case["number2"],case["number3"],case["number4"])
        add_business.input_price(case["price"])
        add_business.click_material()
        add_business.choose_goods(case["purchase_no"])
        add_business.click_material_color()
        add_business.input_consumption(case["Unit_consumption"],case["loss"])
        add_business.save()
        res_save = add_business.toast_info()
        add_business.click_purchase()
        res_assertinfo=add_business.get_text_info()
        #         新增数据之后查询一下数据
        end_num = self.search_db()
#         断言
        try:
            assert case["expected1"]==res_save
            assert case["expected3"] == res_assertinfo
            assert end_num-start_num==2
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例---{}通过".format(case["title"]))
            # 删除待采购需求已经子需求
            add_business.delete_data()
            add_business.click_purchase_data()
            add_business.delete_data()

    # @pytest.mark.dd
    @pytest.mark.parametrize("case", AddBusiness.business_pass_order_case)
    def test_addbusiness_order(self, case, business_fixture):
        index_page, add_business = business_fixture
        # 移动到添加按钮从订单选择
        index_page.move_to_add_element()
        index_page.purchase_from_order()
        #         新增数据之前查询一下数据
        # start_num = self.search_db()
        add_business.choose_goods_order(case["orderno"])
        #         新增数据之后查询一下数据
        # end_num = self.search_db()
        res=add_business.toast_info()

        try:
            assert case["expected"] == res
            # assert end_num-start_num==1
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例---{}通过".format(case["title"]))
            # 删除从订单生成的待采购
            add_business.click_purchase_data()
            add_business.delete_data()
    # @pytest.mark.dd
    @pytest.mark.parametrize("case", AddBusiness.business_pass_price_case)
    def test_addbusiness_price(self,case, business_fixture):
        index_page, add_business = business_fixture
        # 移动到添加按钮从订单选择
        index_page.move_to_add_element()
        index_page.purchase_from_price()
        # 新增数据之前查询一下数据
        # start_num = self.search_db()
        add_business.choose_goods_price(case["cometogoodsno"])
        #         新增数据之后查询一下数据
        # end_num = self.search_db()
        res=add_business.toast_info()

        try:
            assert case["expected"] == res
            # assert end_num-start_num==1
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例---{}通过".format(case["title"]))
            # 删除从订单生成的待采购
            add_business.click_purchase_data()
            add_business.delete_data()


    @classmethod
    def search_db(cls):
        # 添加物品之前查询一下该用户新建的物品数量
        sql = "SELECT*from wd.t_requirement where user_id='510c0631527243788fdb74a14e24bac2'"
        count=cls.db.find_count(sql)
        return count
