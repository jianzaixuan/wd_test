"""
============================
Author:丁琴
Time: 14:11
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
class WarehouseCase:
    fail_data=[{"title":"字段输入都为空","warehousename":"","contacts":"","excepted": "请将信息填写完整！"},
                  {"title":"仓库名字为空","warehousename":"南京仓","contacts":"","excepted": "请将信息填写完整！"},
                  {"title":"仓库联系人为空","warehousename":"南京仓","contacts":"丁琴","excepted": "请将信息填写完整！"}]
    success_data=[{"title":"创建仓库成功","contacts":"丁琴","contact_number": "18965676787","province":"江苏","city":"扬州市","addr_data": "广陵区","remarks": "仓库","excepted": "保存成功！","check_sql":'update wd.t_ware_house set STATUS=1 where name="{}"'}]