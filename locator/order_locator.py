"""
============================
Author:丁琴
Time: 9:33
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By
class Order_locator:

    # 订单从需求相关元素定位
    #     新建订单选择从需求生成，弹出的需求弹框页面，搜索需求编号定位
    requirement_number=(By.XPATH,"//input[@placeholder='需求编号']")
    # 需求选择页面搜索按钮(20200728X468)
    search_btn_requirement=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[5]")
    # 搜索成功后 勾选需求()
    choose_checkbox = (By.XPATH, "//*[contains(text(),'1911G007')]")
    confirm_requirement_btn=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[6]")
#     生成订单成功的toast提示
    success_toast=(By.XPATH,"//*[contains(text(),'生成订单成功')]")
#     从报价生成订单(S2523)
    transaction_no=(By.XPATH,"(//input[@placeholder='往来物料号'])[3]")
    search_btn_transaction=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[3]")
    confirm_price_btn=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[4]")

#     从合同拉取(20200221H056)
    contract_no=(By.XPATH,"//input[@placeholder='合同编号']")
    search_btn_contract=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[1]")
    contract_choose_checkbox=(By.XPATH,'(//input[@type="checkbox"])[1]')
    confirm_contract_btn=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[2]")

#     定位到订单第一条数据(为了删除，使用)
    first_order=(By.XPATH,"(//datatable-body-row[contains(@class,'datatable-body')])[1]")

#     从需求拉取生成订单，报价，合同没有选择确认，提示信息元素
    error_requirement=(By.XPATH,"//*[contains(text(),'请选择需求')]")
    error_price=(By.XPATH,"//*[contains(text(),'请选择报价')]")
    error_contract=(By.XPATH,"//*[contains(text(),'请选择合同')]")

#     没有选择订单，报价，合同确定后关闭弹框
    close_alert_contract=(By.XPATH,'(//span[@class="ant-modal-close-x"])[3]')
    close_alert_requirement=(By.XPATH,'(//span[@class="ant-modal-close-x"])[5]')
    close_alert_price=(By.XPATH,'(//span[@class="ant-modal-close-x"])[4]')
#     编辑删除订单的元素
# 是否删除确定按钮
    delete_order_confim=(By.XPATH,"(//button[@class='ant-btn ant-btn-primary ant-btn-lg'])[1]")
# 删除保存成功提示
    toast_info=(By.XPATH,"//div[@class='ant-message-notice-content']//span")
    # //div[@class='ant-message-notice-content']//span
    # toast_info=(By.XPATH,"//*[contains(text(),'删除成功')]")
#     找找第八条记录编辑
    edit_order=(By.XPATH,"(//datatable-body-row[contains(@class,'datatable-body')])[8]")
#     编辑详情找到第一个输入框
    input_ordernum=(By.XPATH,'(//input[@placeholder="输入数量"])[1]')
#     价格条款tab
    price_tab=(By.XPATH,"(//button[contains(@class,' ant-btn-default')])[2]")
#     价格输入框
    input_orderprice=(By.XPATH,'//input[@placeholder="请输入均价"]')

# #     订单保存成功提示
#     sava_success_toast=(By.XPATH,"//*[contains(text(),'保存成功')]")









