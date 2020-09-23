"""
============================
Author:丁琴
Time: 15:09
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import pytest
from data.warehouse_data import WarehouseCase
from common.handle_logging import my_log
from common.handle_db import HandleMysql
class Test_WareHouse:
    db=HandleMysql()
    # @pytest.mark.goodno
    @pytest.mark.parametrize("case",WarehouseCase.success_data)
    def test_success(self,case,warehouse_fixture):
        index_page, warehouse_page=warehouse_fixture
        # 点击仓库
        index_page.click_warehouse()
        # 点击添加按钮
        index_page.click_addgoods()
        # 输入正确的内容
        warehousename=self.random_warehousename()
        warehouse_page.build_warehouse(warehousename,case["contacts"],case["contact_number"],case["addr_data"],case["remarks"])
        # 获取成功提示
        text=warehouse_page.get_success_info()
        # 获取页面是否存在这个仓库的名字
        str_count=warehouse_page.get_warehousename_str(warehousename)

        # 断言
        try:
            assert case["excepted"]==text
            assert str_count==1
        except  AssertionError as e:
            my_log.error("用例--{}--不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例--{}--通过".format(case["title"]))
            sql='update wd.t_ware_house set STATUS=1 where name="{}"'.format(warehousename, encoding='utf-8')
            self.db.updata(sql)

    @pytest.mark.goodno
    @pytest.mark.parametrize("case",WarehouseCase.fail_data)
    def test_fail(self,case,warehouse_fixture):
        index_page, warehouse_page=warehouse_fixture
        # 点击添加按钮
        index_page.click_addgoods()
        # 输入内容不完整
        warehouse_page.build_warehouse_fail(case["warehousename"],case["contacts"])
        # 获取失败的提示
        text=warehouse_page.get_fail_toast()
        # 点击取消按钮
        warehouse_page.click_cacel()
        # 断言
        try:
            assert case["excepted"]==text
        except  AssertionError as e:
            my_log.error("用例--{}--不通过".format(case["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例--{}--通过".format(case["title"]))
    #         随机生成一个仓库名字是数据库不存在的
    @classmethod
    def random_warehousename(cls):
        while True:
            base_name1="扬州"
            base_name2="仓"
            for i in range(1,500):
                warehousename=base_name1+str(i)+base_name2
                sql = 'SELECT * from wd.t_ware_house WHERE name="{}"'.format(warehousename, encoding='utf-8')
                res = cls.db.find_count(sql)
                if res == 0:
                    return warehousename
