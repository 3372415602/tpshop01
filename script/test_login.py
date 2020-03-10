# 编写登录模块测试用例及管理

# 导包
import unittest
import requests
from api.login import TpshopLogin

# 创建测试类
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tpshop_login =TpshopLogin()

    def setUp(self):
        self.session = requests.session()

    def tearDown(self):
        self.session.close()


    # 创建测试方法
    # 登录成功
    def test01_login_success(self):
        # 1.获取验证码
        response = self.tpshop_login.get_login_verify_code(self.session)
        # 2.断言验证码响应
        self.assertEqual(200,response.status_code)

        # 3.发送登录请求
        response = self.tpshop_login.login(self.session,"13488888888","123456","8888")
        json_data = response.json()
        print(json_data)
        # 4.断言登录响应结果
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, json_data.get("status"))
        self.assertIn("登陆成功",json_data.get("msg"))


    # 用户名不存在
    def test02_user_isnot_exist(self):
        # 1.获取验证码
        response = self.tpshop_login.get_login_verify_code(self.session)
        # 2.断言验证码响应
        self.assertEqual(200, response.status_code)

        # 3.发送登录请求
        response = self.tpshop_login.login(self.session, "13488888899", "123456", "8888")
        json_data = response.json()
        print(json_data)
        # 4.断言登录响应结果
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, json_data.get("status"))
        self.assertIn("账号不存在", json_data.get("msg"))

    # 密码错误
    def test03_password_error(self):
        # 1.获取验证码
        response = self.tpshop_login.get_login_verify_code(self.session)
        # 2.断言验证码响应
        self.assertEqual(200, response.status_code)

        # 3.发送登录请求
        response = self.tpshop_login.login(self.session, "13488888888", "error", "8888")
        json_data = response.json()
        print(json_data)
        # 4.断言登录响应结果
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, json_data.get("status"))
        self.assertIn("密码错误", json_data.get("msg"))