"""
============================
Author:丁琴
Time: 14:33
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
class AddBusiness:
    # 正常新建需求
    business_pass_case=[
        {"title":"新建需求成功","goodsno":"1905G022","number1":"100","number2":"100.34","number3":"1000","number4":"100",
         "price":"12.5","Unit_consumption":"1.2","loss":"1.05","purchase_no":"2006F012","expected1":"添加成功","expected2":"采购成功","expected3":"2006F012"}
    ]
    # 新建需求从订单选择
    business_pass_order_case=[
        {"title":"新建需求从订单选择","orderno":"20191218D182","expected":"生成需求成功"}
    ]
    # 新建需求从报价选择
    business_pass_price_case=[
        {"title":"新建需求从报价选择","cometogoodsno":"VM2705","expected":"生成需求成功"}
    ]
