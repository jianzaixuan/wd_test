"""
============================
Author:丁琴
Time: 11:24
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import pytest
from data.login_case_data import LoginCase
from common.handle_logging import my_log

class Test_Login():
    # @pytest.mark.skip
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", LoginCase.success_data)
    def test_login_pass(self, case, login_fixture):
        login_page, index_page = login_fixture
        # 传入参数登录
        login_page.login(case["mobile"], case["pwd"])
        #     断言是否进入首页
        res = index_page.get_info()
        try:
            assert case["excepted"] == res
        except AssertionError as e:
            my_log.error("用例----{}---不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例----{}---通过".format(case["title"]))
            # 退出
            index_page.exit()

    # @pytest.mark.goodno
    @pytest.mark.parametrize("case", LoginCase.error_data)
    def test_login_fail(self, case, login_fixture):
        login_page, index_page = login_fixture
        # 刷新页面
        login_page.refresh()
        # 传入参数登录
        login_page.login(case["mobile"], case["pwd"])
        #     断言错误提示是否一致
        res = login_page.login_error_info()
        try:
            assert case["excepted"] == res
        except AssertionError as e:
            my_log.error("用例----{}---不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例----{}---通过".format(case["title"]))
if __name__ == "__main__":
    pytest.main()
