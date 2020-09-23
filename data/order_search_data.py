"""
============================
Author:丁琴
Time: 10:41
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
class OrderSearchcase:
    # 订单搜索界面的数据
    order_no_data=[{"title": "搜索订单编号","order_no":"20200821D334","theme":"","product_name":"","goods_no":"","transaction_no":"","creater":"",
                   "contact_unit":"","label":"","excepted":2}]
    order_theme_data=[{"title": "搜索订单主题","order_no":"","theme":"PO#89567","product_name":"","goods_no":"","transaction_no":"","creater":"",
                   "contact_unit":"","label":"","excepted":14}]
    product_name_data = [{"title": "搜索订单品名", "order_no": "", "theme": "", "product_name": "白坯2001", "goods_no": "","transaction_no": "",
                          "creater": "","contact_unit": "", "label": "", "excepted": 3}]
    goods_no_data = [{"title": "搜索订单物料号", "order_no": "", "theme": "", "product_name": "", "goods_no": "1906G062","transaction_no": "",
                          "creater": "","contact_unit": "", "label": "", "excepted": "搜索数据成功"}]
    transaction_no_data = [{"title": "搜索订单往来物料号", "order_no": "", "theme": "", "product_name": "", "goods_no": "","transaction_no": "WC447",
                          "creater": "","contact_unit": "", "label": "", "excepted": "搜索数据成功"}]
    creater_data = [{"title": "搜索订单往来物料号", "order_no": "", "theme": "", "product_name": "", "goods_no": "","transaction_no": "WC447",
                          "creater": "王永刚","contact_unit": "", "label": "", "excepted": "搜索数据成功"}]

    contact_unit_data = [{"title": "搜索订单往来物料号", "order_no": "", "theme": "", "product_name": "", "goods_no": "","transaction_no": "WC447",
                          "creater": "","contact_unit": "海伦服饰", "label": "", "excepted": "搜索数据成功"}]
    label_data = [{"title": "搜索订单往来物料号", "order_no": "", "theme": "", "product_name": "", "goods_no": "","transaction_no": "WC447",
                          "creater": "","contact_unit": "", "label": "python测试", "excepted": "python测试"}]

    goods_type_data = [{"title": "搜索服装类型", "clothing_type":"服装", "excepted": "搜索数据成功"},
    {"title": "搜索面料类型", "fabric_type": "面料", "excepted": "搜索数据成功"},
    {"title": "搜索里料类型", "lining_type": "里料", "excepted": "搜索数据成功"}
]
    order_type_data = [{"title": "搜索采购类型", "purchase_type":"采购", "excepted": "搜索数据成功"},
                       {"title": "搜索销售类型", "sale_type":"销售", "excepted": "搜索数据成功"}]
    fail_search=[{"title": "搜索采购类型", "name":"214343","excepted": "搜索数据失败"}]