# -*-coding:utf8-*-
import requests
from util.utils import Utils
import json


class User:
    def __init__(self):
        self.token = Utils().get_user_access_token()

    def create_user(self, userid, name, mobile, department):
        """
        创建成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        if department is None:
            department = [1]
        request_data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        request_data_json = json.dumps(request_data, ensure_ascii=False).encode("utf-8")
        request_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        return requests.post(request_url, data=request_data_json).json()
        # return requests.post(request_url, json=test_data)

    def get_user(self, userid):
        """
        读取成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        request_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        return requests.get(request_url).json()

    def update_user(self):
        """
        更新成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_data = {
            "userid": "test001",
            "name": "测试001",
            "mobile": 13800000002,
            "department": [1]
        }
        request_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        return requests.post(request_url, json=request_data).json()

    def delete_user(self, userid):
        """
        删除成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        request_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        return requests.get(request_url).json()

    def batch_delete_user(self):
        """
        批量删除成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token=ACCESS_TOKEN
        :return:
        """
        pass

    def get_department_user(self):
        """
        获取部门成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token=ACCESS_TOKEN&department_id=DEPARTMENT_ID&fetch_child=FETCH_CHILD
        :return:
        """
        pass

    def get_department_user_info(self):
        """
        获取部门成员详情
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token=ACCESS_TOKEN&department_id=DEPARTMENT_ID&fetch_child=FETCH_CHILD
        :return:
        """
        pass

    def invite_user(self):
        """
        邀请成员
        请求方式：POST（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/batch/invite?access_token=ACCESS_TOKEN
        :return:
        """
        pass

    def get_join_qr_code(self):
        """
        获取加入企业二维码
        请求方式：GET（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/corp/get_join_qrcode?access_token=ACCESS_TOKEN&size_type=SIZE_TYPE
        :return:
        """
        pass

    def get_active_statistics(self):
        """
        获取企业活跃成员数
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get_active_stat?access_token=ACCESS_TOKEN
        :return:
        """
        pass

if __name__=="__main__":
    print(User().update_user())
