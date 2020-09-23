"""
============================
Author:丁琴
Time: 11:36
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""

class OrderCase:
    requirement_data=[{"title": "生成订单成功", "requirement_no": "20200728X468", "excepted": "生成订单成功"}]
    transaction_data = [{"title": "输入物料号", "transaction_no": "S2523", "excepted": "生成订单成功"}]
    contract_data = [{"title": "输入合同编号", "contract_no": "20200221H056", "excepted": "生成订单成功"}]
    error_requirement_data = [{"title": "输入需求编号", "requirement_no": "20200728X468", "excepted": "请选择需求"}]
    error_transaction_data = [{"title": "输入物料号", "transaction_no": "S2523", "excepted": "请选择报价"}]
    error_contract_data = [{"title": "输入合同编号", "contract_no": "20200331H060", "excepted": "请选择合同"}]
    delete_order_data=[{"title": "删除订单","excepted": "删除成功！"}]
    edit_order_data=[{"title": "编辑订单","num":"200","price":"60.89","excepted": "保存成功"}]
