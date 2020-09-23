"""
============================
Author:丁琴
Time: 11:42
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By
class IndexLocator:
    # 首页瓦丁公司名称元素
    comp_ele=(By.XPATH, "//span[contains(text(),'瓦丁')]")
    # 退出按钮
    exit=(By.XPATH,"//a[text()=' 退出']")
    # 点击物品按钮
    goods_btn=(By.XPATH,"//span[text()='物品']")
    # 添加物品按钮（合同，订单，待交易都是这个加号）
    add_btn=(By.XPATH,"//a/img[@title='添加']")
    # # 物品模块点击搜索按钮
    # search_goods_btn=(By.XPATH,"//img[@title='搜索']")
    #
    # # 搜索弹框的物料号输入框
    # input_search_goods_no=(By.XPATH,"//input[@placeholder='物料号']")
    # # 搜索界面确定按钮
    # search_confim_btn=(By.XPATH,"(//button[contains(@class,'ant-btn ant-btn-primary ant-btn-lg')])[1]")
    # 搜索到物品定位一下物料号是不是搜索到了数据
    confirm_goodsno_exist=(By.XPATH,"//a[contains(text(),'1905G022')]")
    # 待交易相关的元素
#     点击加号选择新建需求点击
    new_business=(By.XPATH,"//a[text()='新建需求']")
    # 从订单生成需求
    purchase_from_order=(By.XPATH,"//a[text()='订单生成']")
    # 从报价生成需求（待交易和订单公用）
    purchase_from_price=(By.XPATH,"//a[text()='报价生成']")

#     首页点击订单模块的元素
    order=(By.XPATH,"//span[text()='订单']")
    # 从需求生成订单
    purchase_from_business=(By.XPATH,"//a[text()='需求生成']")
    # 从合同生成订单
    purchase_from_contract=(By.XPATH,"//a[text()='合同生成']")

#     公共的删除按钮
    common_delete_btn=(By.XPATH,"//a/img[@title='删除']")
#     公共的保存按钮
    common_save = (By.XPATH, "//a/img[@title='保存']")
#     点击仓库管理模块
    #       仓库管理模块
    warehouse_manage = (By.XPATH, "//span[text()='仓库管理']")
#     报价模块
    quoted_price=(By.XPATH,"(//span[text()='报价'])[1]")

