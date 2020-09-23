"""
============================
Author:丁琴
Time: 11:14
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
class LoginCase:
    # 正常登录的用例
    success_data = [{"title": "登录成功", "mobile": "18951818135", "pwd": "111111", "excepted": "登录成功"}]
    # 异常登录的用例
    error_data = [{"title": "手机号为空", "mobile": "", "pwd": "1", "excepted": "请输入账号"},
                  {"title": "手机号错误", 'mobile': "1868472055q", "pwd": "111111", "excepted": "用户不存在！"},
                  {"title": "密码为空", 'mobile': "18684720553", "pwd": "", "excepted": "请输入密码"},
                  {"title": "密码为空", 'mobile': "", "pwd": "", "excepted": "请输入账号"}
                  ]
