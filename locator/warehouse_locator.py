"""
============================
Author:丁琴
Time: 9:30
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from selenium.webdriver.common.by import By
class WarehouseLocator:
#     仓库相关的元素定位
        warehouse_name=(By.XPATH,'//input[@placeholder="请输入名称"]')
        contacts=(By.XPATH,'//input[@placeholder="请输入联系人"]')
        contact_number=(By.XPATH,'//input[@placeholder="请输入联系电话"]')
        # 选择省
        choose_province=(By.XPATH,'(//span[@class="ant-select-arrow"])[1]')
        province=(By.XPATH,'((//div[contains(@id,"cdk-overlay-")])[2]//li)[11]')
# 选择市
        choose_city = (By.XPATH, '(//span[@class="ant-select-arrow"])[2]')
        city=(By.XPATH,'((//div[contains(@id,"cdk-overlay-")])[3]//li)[11]')
        # 输入地址
        input_addr=(By.XPATH,'//input[@placeholder="请输入地址"]')
        # 选择类型
        choose_warehousetype=(By.XPATH,'(//div[@class="ant-select-selection__placeholder"])[3]')
#         选择内容仓库
        choose_innerwarehouse=(By.XPATH,'(//li[contains(@class,"ant-select-dropdown-menu-item ng-tns-")])[2]')
#         输入备注
        input_remarks=(By.XPATH,'//input[@placeholder="请输入备注"]')
#     确定
        confirm_btn=(By.XPATH,'//button[@class="ant-btn ant-btn-default"]')

# 保存成功提示
        success_toast=(By.XPATH,"//*[contains(text(),'保存成功')]")
# 保存失败提示
        fail_tosat=(By.XPATH,"//*[contains(text(),'请将信息填写完整！')]")
# 关闭弹框按钮
        cacle_btn=(By.XPATH,'(//button[@aria-label="Close"])[1]')





