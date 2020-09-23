"""
============================
Author:丁琴
Time: 13:48
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By
class AddBusinesslocator:
    # 新建需求详情选择类型
    click_business_type=(By.XPATH,"(//div[@class='ant-select-selection__placeholder'])[1]")
    # 选择采购类型
    buy_type=(By.XPATH,"(//ul[contains(@class,'ant-select-dropdown-menu')]/li)[1]")
    # 选择物品
    choose_goods=(By.XPATH,"//td[@class='choose-goods-item']/a")
    # 弹出物品选择界面，搜索物品选择
    search_goodsno=(By.XPATH,"//input[@placeholder='物料号']")
    search_btn=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[3]")

    # 选择物品前面的勾选框
    choose_checkbox=(By.XPATH,"(//input[@type='checkbox'])[1]")
    # 删除选择确定按钮
    confirm_btn=(By.XPATH,"(//button[contains(@class,'ant-btn')])[2]")
    # 选择商品后确定
    goods_confirm_btn=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[4]")
    # 点击保存按钮
    save=(By.XPATH,"//a/img[@title='保存']")

    # toast提示信息

    toast_info=(By.XPATH,"//div[@class='ant-message-notice-content']//span")
    # 输入规格数量
    input_number1=(By.XPATH,"(//input[@placeholder='输入数量'])[1]")
    input_number2 = (By.XPATH, "(//input[@placeholder='输入数量'])[2]")
    input_number3 = (By.XPATH, "(//input[@placeholder='输入数量'])[3]")
    input_number4 = (By.XPATH, "(//input[@placeholder='输入数量'])[4]")
# 点击价格条款输入价格
    price_btn=(By.XPATH,"//span[text()='价格条款']")
    input_price=(By.XPATH,"//input[@placeholder='请输入均价']")
    # 点击材料单选择材料
    click_material=(By.XPATH,"(//button[contains(@class,'ng-star-inserted')])[3]")
    # 点击添加材料单按钮
    click_add_btn=(By.XPATH,"(//a[@class='cursor'])[2]")
    # 配色配码选择
    material_btn=(By.XPATH,"(//img[@class='ng-star-inserted'])[2]")
    material_color1=(By.XPATH,"(//div[@class='ant-select-selection__placeholder'])[6]")
    choose_color1=(By.XPATH,"(//li[contains(@class,'ant-select-dropdown-menu-item ng-tns-')])[2]")
    material_color2 = (By.XPATH, "(//div[@class='ant-select-selection__placeholder'])[7]")
    choose_color2 = (By.XPATH, "(//li[contains(@class,'ant-select-dropdown-menu-item ng-tns-')])[3]")

    # 配色配码后点击确定
    material_confirm=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[6]")
    # 输入单耗损耗
    Unit_consumption=(By.XPATH,"//input[@placeholder='单耗']")
    loss=(By.XPATH,"//input[@placeholder='损耗']")

    # 点击采购按钮
    purchase_btn=(By.XPATH,"//a/img[@title='采购']")
    # 点击待采购查看是否有数据
    click_purchase=(By.XPATH,"(//button[contains(@class,'ng-star-inserted')])[4]")
    purchase_no=(By.XPATH,"//td[contains(text(),'2006F012')]")

#     点击删除
    delete_btn=(By.XPATH,"//a/img[@title='删除']")
#     确认删除
    delete_confirm=(By.XPATH,"(//button[@class='ant-btn ant-btn-primary ant-btn-lg'])[1]")
#     定位到待采购生成的数据
    purchase_data=(By.XPATH,"(//datatable-body-row)[1]")

    # 从订单选择生成需求的物料号输入
    search__order_no=(By.XPATH,"//input[@placeholder='订单号']")

    # 从报价选择生成需求的物料号输入
    search_price_no=(By.XPATH,"(//input[@placeholder='往来物料号'])[2]")
    # 选择报价弹框页面搜索按钮
    search_btn_price=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[1]")
    # 选择商品后确定
    goods_confirm_price_btn=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[2]")
    confirm_order_btn=(By.XPATH,"(//button[@class='ant-btn ant-btn-default'])[4]")
