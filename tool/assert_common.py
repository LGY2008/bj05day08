from tool.ge_log import GetLog

log = GetLog.get_log()


def assert_common(self,response,success=True, message="操作成功！", code=10000, status_code=201):
    try:
        # 断言状态码
        self.assertEqual(response.status_code, status_code)
        # 断言是否成功
        self.assertEqual(response.json().get("success"), success)
        # 断言message消息
        self.assertEqual(response.json().get("message"), message)
        # 断言code
        self.assertEqual(response.json().get("code"), code)
    except Exception as e:
        log.error(e)
        # 抛异常
        raise  # 捕获哪个异常，抛出哪个