import unittest
from parameterized import parameterized
from api.api_employee import ApiEmployee
from tool.assert_common import assert_common


def get_data():
    return [("李五04","13800010054","2019-07-01",1,"10001554","开发部","1066240656856453120","2019-11-30")]


class TestEmployee(unittest.TestCase):
    # 设置员工id
    emp_id = None
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiEmployee对象
        cls.emp = ApiEmployee()

    # 员工新增测试方法
    @parameterized.expand(get_data())
    def test01_post_employee(self, username, mobile, timeOfEntry, formOfEmployment, workNumber, departmentName,
                             departmentId, correctionTime):
        # username, mobile, timeOfEntry, formOfEmployment, workNumber, departmentName, departmentId, correctionTime
        result = self.emp.api_post_employee(username=username,
                                            mobile=mobile,
                                            timeOfEntry=timeOfEntry,
                                            formOfEmployment=formOfEmployment,
                                            workNumber=workNumber,
                                            departmentName=departmentName,
                                            departmentId=departmentId,
                                            correctionTime=correctionTime)
        print("新增员工结果：", result.json())
        # 获取 员工新增成功后 生成的id值
        TestEmployee.emp_id=result.json().get("data").get("id")
        # 调用公共断言
        assert_common(self, result)

    # 更新
    def test02_update_employee(self):
        username= "李四_update"
        result = self.emp.api_update_employee(emp_id=TestEmployee.emp_id, username=username)
        # 调用公共断言
        assert_common(self, result)

    # 查询指定员工
    def test03_get_employee(self):
        result = self.emp.api_get_employee(TestEmployee.emp_id)
        # 调用公共断言
        assert_common(self, result)

    # 删除员工测试方法
    def test04_delete_employee(self):
        result = self.emp.api_delete_employee(TestEmployee.emp_id)
        # 调用公共断言
        assert_common(self, result)