"""
============================
Author:丁琴
Time: 12:26
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By
class GoodsLocator:
    # 点击物品类型元素
    goods_type_btn=(By.XPATH,"(//div[contains(@class,'ant-select-selection__rendered ng-tns-c')])[1]")
    # 选择一个物品类型
    choose_goodstype=(By.XPATH,"(//li[contains(@class,'ant-select-dropdown-menu-item ng-tns-c')])[1]")
    # 品名输入框
    goods_name=(By.XPATH,"//input[@placeholder='品名']")
    # 选择单位框
    unit_btn=(By.XPATH,"(//div[@class='ant-select-selection__placeholder'])[2]")
    # 选择一个单位
    choose_unit=(By.XPATH,"(//li[contains(@class,' ng-star-inserted')])[3]")
    # 点击尺码
    click_btn=(By.XPATH,"(//input[@placeholder='请输入内容'])[3]")
    # 输入颜色尺码规格内容
    input_clor=(By.XPATH,"(//input[@placeholder='请输入规格'])[1]")
#     点击尺码输入尺码
    size_btn=(By.XPATH,"//input[@placeholder='请输入规格']")

    # 点击保存物品按钮
    save=(By.XPATH,"//a/img[@title='保存']")

    # 物品类型为空提示信息
    good_type_errorinfo=(By.XPATH,"//div[contains(@class,'ant-message-custom-content ng-tns-')]")
    # 添加物品失败错误提示信息
    good_errorinfo=(By.XPATH,"(//span[contains(@class,'ng-tns-')])[3]")

    # # 添加物品失败错误提示信息
    # goods_errorinfo=(By.XPATH,"(//span[contains(@class,'ng-tns-')])[3]")

#     保存成功按钮
#     save_success=(By.XPATH,"(//span[contains(@class,'ng-tns-')])[3]")
#     物品列表定位第一条数据点击进入详情
    list_goodsdata=(By.XPATH,"(//a[contains(text(),'裤子')])[1]")

#     物品详情定位到状态正常
    normal_status=(By.XPATH,"(//div[@class='ant-select-selection__placeholder'])[3]")
    # 选择作废的物品状态
    delete_status=(By.XPATH,"(//li[contains(@class,'ant-select-dropdown-menu-item ng-tns-')])[2]")
    # 作废物品保存的弹框点击确定
    goods_delete_confirm=(By.XPATH,"(//button[@class='ant-btn ant-btn-primary ant-btn-lg'])[1]")
    # 删除成功后点击物品返回到列表
    click_goods=(By.XPATH,"//a[text()='物品']")
#     搜索已使用的物品进入详情点击状态元素
    use_normal_status=(By.XPATH,"(//div[@class='ant-select-selection__placeholder'])[2]")



