import pytest
import requests
from common.commonData import CommonData
from conftest import http
import allure

@allure.feature('修改密码模块')
class Test_changePwd:
    @allure.story('修改密码成功')
    def test_change_success(this):
        data = {
        "userId": "134",
        "userName": CommonData.userName,
        "oldPwd": CommonData.password,
        "password": "123456"
    }
        resp=http.post('/sys/changePwd',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'

    @allure.story('修改密码失败')
    def test_change_fail(this):
        data = {
        "userId": "134",
        "userName": 15513366973,
        "oldPwd": "1234",
        "password": "123123"
    }
        resp=http.post('/sys/changePwd',data)
        assert resp['code']==411
        assert resp['msg']=='旧密码错误'
