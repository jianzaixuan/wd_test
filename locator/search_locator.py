"""
============================
Author:丁琴
Time: 12:15
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By

class Search_Locator:

    # 物品模块点击搜索按钮(与订单的搜索通用)
    search_goods_btn = (By.XPATH, "//img[@title='搜索']")
    # 定位到搜索界面物品类型框（与订单的物品类型通用）
    goods_type=(By.XPATH,"//div[@class='ant-select-selection__placeholder']")
    # 物品类型框选择一个物品类型
    # 服装类型(要注意设置里面物品类型的排序问题)（与订单的服装型通用）
    clothing_type=(By.XPATH,"((//div[contains(@id,'cdk-overlay-')])[2]//li)[1]")
    # 面料类型
    fabric_type=(By.XPATH,"((//div[contains(@id,'cdk-overlay-')])[2]//li)[2]")
    # 里料类型
    lining_type=(By.XPATH,"((//div[contains(@id,'cdk-overlay-')])[2]//li)[3]")
    # 品名搜索框
    product_name=(By.XPATH,"//input[@placeholder='品名']")
    # 搜索弹框的物料号输入框
    goods_no = (By.XPATH, "//input[@placeholder='物料号']")
    # 往来物料号搜索框
    transaction_no=(By.XPATH,"//input[@placeholder='往来物料号']")
    # 创建人
    creater=(By.XPATH,'//input[@placeholder="创建人"]')
    # 往来单位
    contact_unit=(By.XPATH,'//input[@placeholder="往来单位"]')
    # 开始时间(操作的时候需要通过js修改时间)
    start_time=(By.XPATH,"(//input[@class='ant-calendar-picker-input ant-input'])[1]")
    # 开始时间(操作的时候需要通过js修改时间)
    end_time=(By.XPATH,"(//input[@class='ant-calendar-picker-input ant-input'])[2]")
    # js="""
    # var data0=arguments[0];
    # var data1=arguments[1];
    # data.readonly=false;
    # data.value='2020-08-02'
    # data1.readonly=false;
    # data1.value='2020-08-14'
    # """
    # driver.execute_script(js,start_time,end_time)
    # 备注
    remarks=(By.XPATH,'//input[@placeholder="备注"]')
    # 标签
    label=(By.XPATH,'//input[@placeholder="标签"]')
    # 搜索泽冠往来单位列表显示的数据点击第一条数据进入物品详情后点击报价记录里面有泽冠2字泽成功
    # 定位到第一条记录的物料号元素
    unit_googsno=(By.XPATH,"//*[contains(text(),'2006G112')]")
    # 报价记录元素
    price_record=(By.XPATH,"(//div[@class='check-tab']/button)[2]")
    # 找到泽冠的往来单位字样
    contact_unit_confim=(By.XPATH,"//*[contains(text(),'泽冠')]")
    # 备注tab元素
    remarks_tab=(By.XPATH,"(//div[@class='check-tab']/button)[4]")
    # 找到备注的字样
    remarks_confim=(By.XPATH,"//textarea[@placeholder='输入备注']")

    # 搜索标签后点击物品的元素定位信息
    label_goodno=(By.XPATH,"//*[contains(text(),'2006F012')]")
    # 输入标签的文本元素
    label_confim=(By.XPATH,"(//input[@placeholder='请输入标签'])[1]")

    # 搜索界面确定按钮
    search_confim_btn = (By.XPATH, "(//button[contains(@class,'ant-btn ant-btn-primary ant-btn-lg')])[1]")

    # 搜索物品类型后页面最底部展示的类型元素定位
    low_clothing_type=(By.XPATH,"(//*[contains(text(),'服装')])[15]")
    low_fabric_type=(By.XPATH,"(//*[contains(text(),'面料')])[15]")
    low_lining_type=(By.XPATH,"(//*[contains(text(),'里料')])[15]")



# 订单搜索界面的元素（与物品搜索界面元素不一样的）
# 往来物料号
    order_transaction_no=(By.XPATH,"(//input[@placeholder='往来物料号'])[1]")
    order_no=(By.XPATH,'//input[@placeholder="订单编号"]')
    order_type=(By.XPATH,"(//div[contains(@class,'ant-select-selection__rendered ng-tns')])[2]")

    order_purchase=(By.XPATH,"((//div[contains(@id,'cdk-overlay')])[2]//li)[2]")
    order_sale=(By.XPATH,"((//div[contains(@id,'cdk-overlay')])[2]//li)[3]")
    order_theme=(By.XPATH,'(//input[@placeholder="主题"])[1]')


#     定位到订单第一条数据(为了点击进入详情使用)
    first_order=(By.XPATH,"(//datatable-body-row[contains(@class,'datatable-body')])[1]")
    # 订单详情点击标签
    label_tab=(By.XPATH,"(//button[contains(@class,'ng-tns-')])[3]")
    # 标签输入框元素
    label_input=(By.XPATH,'//input[@placeholder="请输入标签"]')