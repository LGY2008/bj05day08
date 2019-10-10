import api
import requests

from tool.ge_log import GetLog
log = GetLog.get_log()


class ApiLogin:
    def __init__(self):
        # 定义登录 url
        self.url_login = api.BASE_URL + "/api/sys/login"

    # 登录接口
    def api_login(self, mobile, password):
        log.info("正在执行登录操作，手机：{} 密码：{}".format(mobile, password))
        data = {"mobile":mobile, "password": password}
        # 重点一定要返回响应对象
        return requests.post(url=self.url_login, json=data, headers=api.headers)
