# -*- coding:utf8 -*-
import pytest
from wework.user import User
from util.utils import Utils
import allure

@allure.suite("企业微信成员测试用例")
class TestUser:

    @allure.feature("创建用户")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("userid, name, mobile, department, errcode, errmsg",
                             Utils().get_yaml("Normal_User", "data"))
    def test_create_user(self, userid, name, mobile, department, errcode, errmsg):
        with allure.step("开始创建用户……"):
            result = User().create_user(userid, name, mobile, department)
            print(result)
        with allure.step("开始校验……"):
            assert errcode == result['errcode']
            assert errmsg in result['errmsg']

    @allure.feature("创建userid存在的用户")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("userid, name, mobile, department, errcode, errmsg",
                             Utils().get_yaml("Repetition_UserId", "data"))
    def test_create_user_repetition_userid(self, userid, name, mobile, department, errcode, errmsg):
        with allure.step("开始创建用户……"):
            result = User().create_user(userid, name, mobile, department)
            print(result)
        with allure.step("开始校验……"):
            assert errcode == result['errcode']
            assert errmsg in result['errmsg']

    @allure.feature("创建手机号存在的用户")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("userid, name, mobile, department, errcode, errmsg",
                             Utils().get_yaml("Repetition_Mobile", "data"))
    def test_create_user_repetition_mobile(self, userid, name, mobile, department, errcode, errmsg):
        with allure.step("开始创建用户……"):
            result = User().create_user(userid, name, mobile, department)
            print(result)
        with allure.step("开始校验……"):
            assert errcode == result['errcode']
            assert errmsg in result['errmsg']

    @allure.feature("查找用户")
    @pytest.mark.run(order=2)
    def test_get_user(self):
        with allure.step("开始查询用户信息……"):
            result = User().get_user("guodong")
        print(result)
        with allure.step("开始校验……"):
            assert 0 == result['errcode']

    @allure.feature("删除用户")
    @pytest.mark.run(order=2)
    def test_delete_user(self):
        with allure.step("开始删除用户……"):
            result = User().delete_user("test0001")
        with allure.step("开始校验……"):
            assert 0 == result['errcode']



if __name__=="__Main__":
    pytest.main()