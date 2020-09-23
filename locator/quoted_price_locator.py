"""
============================
Author:丁琴
Time: 12:02
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By
class QuotedprinceLocator:

# 报价模块
# 详情添加报价的加号
    add_price=(By.XPATH,"//button[@id='add']")
# 选择往来单位
    contact_unit=(By.XPATH,'(//div[@class="ant-select-selection__placeholder"])[1]')
# 选择匹配到的往来单位
    choose_contact=(By.XPATH,'//span[@title="南京青稞服装辅料有限公司"]')
# 点击往来物料号
    contact_no=(By.XPATH,'(//a[contains(@class,"ng-tns-c")])[5]')
#输入往来物料号
    input_contact_no=(By.XPATH,'//input[@placeholder="新物料号"]')
# 点击确定
    click_confirm=(By.XPATH,"(//button[contains(@class,'ant-btn')])[4]")


# toast提示信息
#     创建报价成功
    create_price_toast=(By.XPATH,"//span[text()='创建报价成功']")
# 保存成功提示
    save_toast=(By.XPATH,"//span[text()='保存成功']")
# 请选择物品提示
    choose_goods_toast=(By.XPATH,"//*[contains(text(),'请选择物品')]")
# 搜索按钮
    search_btn=(By.XPATH,'(//button[@class="ant-btn ant-btn-default"])[1]')
# 确定按钮
    confirm=(By.XPATH,'(//button[@class="ant-btn ant-btn-default"])[2]')