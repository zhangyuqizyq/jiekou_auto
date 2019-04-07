import pytest
import requests
import allure
from common.commonData import CommonData
from conftest import http

@allure.feature('登录模块')
class Test_login:
    @allure.story('登录成功')
    def test_login_success(this):
        data = {
        "userName": CommonData.userName,
        "password": CommonData.password
    }
        resp=http.post('/sys/login',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        assert resp['object']['userId']==134

    @allure.story('登录失败')
    def test_login_fpwd(this):
        data = {
            "userName": CommonData.userName,
            "password": "12345678"
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 410
        assert resp['msg'] == '用户名或密码错误'

    def test_login_fusername(this):
        data = {
            "userName": "12345678900",
            "password": CommonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'

    def test_login_15username(this):
        data = {
            "userName": "123456781234567",
            "password": CommonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'

    def test_login_kusername(this):
        data = {
            "userName": "",
            "password": CommonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 3010
        assert resp['msg'] == '此账户禁止登录'

    def test_login_kcanshu(this):
        data = {
            "password": CommonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'

