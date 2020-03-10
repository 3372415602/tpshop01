# 登录模块接口封装

# 导包
import requests

# 创建类
class TpshopLogin:
    # 准备工作
    def __init__(self):
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.url_login  = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 创建方法
    # 获取验证码接口方法
    def get_login_verify_code(self, session):
        response = session.get(self.url_verify)
        return response

    # 登录方法
    def login(self, session, user, pwd , code):
        login_data = {
            "username": user,
            "password": pwd,
            "verify_code": code
        }
        response = session.post(url=self.url_login, data=login_data)
        return response