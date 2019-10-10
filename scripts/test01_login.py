import unittest

import api
from parameterized import parameterized
from api.api_login import ApiLogin
from tool.ge_log import GetLog
# 获取数据
from tool.assert_common import assert_common

log = GetLog.get_log()


def get_data():
    return [("13800000002","123456", 200, "操作成功！")]


class TestLogin(unittest.TestCase):
    def setUp(self):
        # 获取api_login对象
        self.login = ApiLogin()
        log.info("正在初始化 ApiLogin对象：{}".format(self.login))

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, mobile, password, status_code, message):
        # 调用登录方法
        result = self.login.api_login(mobile, password)
        # 断言状态码
        self.assertEqual(result.status_code, status_code)
        # 断言 登录状态
        self.assertTrue(result.json().get("success"))
        # 断言 message
        self.assertEqual(result.json().get("message"), message)

        # 提取data
        api.headers['Authorization']= "Bearer " + result.json().get('data')  # 提取 data值，并追加到headers

        # 查看此时header信息：
        print("追加data后,headers信息内容为：",api.headers)

        # 调用公共断言
        assert_common(self,result)