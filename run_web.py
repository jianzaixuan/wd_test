"""
============================
Author:丁琴
Time: 15:34
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
# import unittest
# from HTMLTestRunnerNew import HTMLTestRunner
# from common.handle_path import REPORT_DIR,CASE_DIR
# import os
# # 加载测试用例套件
# suite=unittest.defaultTestLoader.discover(CASE_DIR)
# # 创建运行程序
# runner=HTMLTestRunner(stream=open(os.path.join(REPORT_DIR,"report.html"), "wb"), title="第一份测试报告")
# 执行程序
# runner.run(suite)


import pytest
import os

from common.send_email import send_smg

pytest.main()

# pytest.main()
# 运行测试用例，生成测试报告
# pytest.main(["-m goodno",'--alluredir=allure_report'])
# 启动allure服务，查看测试报告
# os.system('allure serve allure_report')
# send_smg()
