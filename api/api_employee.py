import requests

import api
from tool.ge_log import GetLog

log = GetLog.get_log()


class ApiEmployee:
    # 初始化
    def __init__(self):
        # 新增员工 url
        self.url_post = api.BASE_URL + "/api/sys/user"
        log.info("正在初始化新增员工url：{}".format(self.url_post))
        # 修改员工
        self.url_alter = api.BASE_URL + "/api/sys/user/{}"
        log.info("正在初始化修改员工url：{}".format(self.url_alter))

    # 新增员工
    def api_post_employee(self, username, mobile,
                          timeOfEntry, formOfEmployment,
                          workNumber, departmentName, departmentId,
                          correctionTime):

        data = {"username": username,
                "mobile": mobile,
                "timeOfEntry": timeOfEntry,
                "formOfEmployment": formOfEmployment,
                "workNumber": workNumber,
                "departmentName": departmentName,
                "departmentId": departmentId,
                "correctionTime": correctionTime}
        # 注意：一定要返回对象
        return requests.post(url=self.url_post, json=data, headers=api.headers)

    # 更新员工
    def api_update_employee(self, emp_id, username):
        data = {"username":username}
        return requests.put(url=self.url_alter.format(emp_id), json=data, headers=api.headers)

    # 查询指定员工
    def api_get_employee(self, emp_id):
        return requests.get(url=self.url_alter.format(emp_id), headers=api.headers)

    # 删除员工
    def api_delete_employee(self, emp_id):
        # 调用delete方法
        return requests.delete(url=self.url_alter.format(emp_id), headers=api.headers)
