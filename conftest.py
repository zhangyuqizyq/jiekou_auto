import pytest
import requests
import json
from util.httpUtil import HttpUtil
from common.commonData import CommonData
http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path="/sys/login"
    data = {
        'userName': CommonData.userName,
        'password': CommonData.password
    }
    resp_login=http.post(path,data)
    CommonData.token=resp_login['object']['token']



    # proxies = {'http': 'http://localhost:8888'}
    # headers = {'Content-Type': 'application/json;charset=UTF-8'}
    # resp_login= requests.post(url="http://192.168.1.203:8083/sys/login",
    #                      proxies=proxies,
    #                      data='{"userName": "18210034706","password": "123456"}',
    #                      headers=headers)
    # resp_dict = json.loads(resp_login.text)
    # token = resp_dict['object']['token']
    # assert resp_login.status_code==200
    # print("登录成功")
    # yield
    # headers['token'] = token
    # resp_logout=http.post(url="http://192.168.1.203:8083/sys/logout",
    #                  proxies=proxies,
    #                  data=None,
    #                  headers=headers)
    # assert resp_logout.status_code==200
    # print("退出成功")