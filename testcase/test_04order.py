"""
============================
Author:丁琴
Time: 17:25
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from data.order_case import OrderCase
import pytest
from common.handle_logging import my_log
class Test_Order:
#     新建订单从需求选择
#     @pytest.mark.goodno
    @pytest.mark.parametrize("case",OrderCase.requirement_data)
    def test_order_requirement(self,case,order_fixture):
        order_page=order_fixture[1]
#         鼠标移动到添加订单按钮
        order_page.order_from_requirement(case["requirement_no"])
#         获取成功提示信息
        text=order_page.success_toast()
#         断言
        #     断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
#     新建订单从报价选择
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderCase.transaction_data)
    def test_order_price(self, case, order_fixture):
        order_page = order_fixture[1]
        #         鼠标移动到添加订单按钮
        order_page.order_from_price(case["transaction_no"])
        #         获取成功提示信息
        text = order_page.success_toast()
        #         断言
        #     断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
#     新建订单从合同
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderCase.contract_data)
    def test_order_contract(self, case, order_fixture):
        order_page = order_fixture[1]
        #         鼠标移动到添加订单按钮
        order_page.order_from_contract(case["contract_no"])
        #         获取成功提示信息
        text = order_page.success_toast()
        #         断言
        #     断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
#     新建订单从需求选择，没有选择需求确定
#     @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderCase.error_requirement_data)
    def test_order_requirementerror(self, case, order_fixture):
        order_page = order_fixture[1]
        #         鼠标移动到添加订单按钮
        order_page.order_from_requirementerror(case["requirement_no"])
        #         获取成功提示信息
        text = order_page.get_error_requirement()
        # 关闭弹框页面
        order_page.close_requirement_btn()
        #         断言
        #     断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
#         新建订单从报价选择，没有选择报价确定
#     @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderCase.error_transaction_data)
    def test_order_transactionerror(self,case, order_fixture):
        order_page = order_fixture[1]
        #         鼠标移动到添加订单按钮
        order_page.order_from_priceerror(case["transaction_no"])
        #         获取成功提示信息
        text = order_page.get_error_price()
        # 关闭弹框页面
        order_page.close_price_btn()
        #         断言
        #     断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    #         新建订单从报价选择，没有选择报价确定
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderCase.error_contract_data)
    def test_order_contracterror(self, case, order_fixture):
        order_page = order_fixture[1]
        #         鼠标移动到添加订单按钮
        order_page.order_from_contracterror(case["contract_no"])
        #         获取成功提示信息
        text = order_page.get_error_contract()
        # 关闭弹框页面
        order_page.close_contract_btn()
        #         断言
        #     断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderCase.delete_order_data)
    def test_delete_order(self,case,order_fixture):
        order_page = order_fixture[1]
        order_page.delete_order()
        #         获取成功提示信息
        text = order_page.toast_text()
        #     断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))

    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", OrderCase.edit_order_data)
    def test_edit_order(self,case,order_fixture):
        order_page = order_fixture[1]
        order_page.edit_order(case["num"],case["price"])
        #         获取成功提示信息
        text = order_page.toast_text()
        #     断言
        try:
            assert case["excepted"] == text
        except AssertionError as e:
            my_log.error("用例---{}不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}通过".format(case["title"]))