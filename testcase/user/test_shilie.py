import pytest
import requests
import random
import allure
from common.commonData import CommonData
from conftest import http

@allure.feature('注册模块')
class Test_lianxi:
    @allure.story('注册成功')
    def test_register_success(this):
        nickName=str(random.randint(10000000,100000000))
        userName='135'+nickName
        register_data = {
            "nickName":nickName ,
            "userName":userName ,
            "telNo": "",
            "email": "",
            "address": "",
            "roleIds": "",
            "regionId": 1,
            "regionLevel": 1
    }
        resp=http.post('/user/saveOrUpdateUser',register_data)
        assert resp['code']==401

        login_data={'userName': userName,'password': CommonData.password}
        login=http.post('/sys/login',login_data)
        assert login['code']==200
        userId=login['object']['userId']

        userlist_data={"pageCurrent": 1,"pageSize": 10,"nickName": "","userName": "","regionId": 1}
        userlist=http.post('/user/loadUserList',userlist_data)
        first_userid=userlist['object']['list'][0]['id']
        assert userlist['code']==200
        assert first_userid==userId

        userinfo_data={'id':first_userid}
        userinfo=http.post('/user/loadUserInfo',userinfo_data)
        assert userinfo['code']==200
