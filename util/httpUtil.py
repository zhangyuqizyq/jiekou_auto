import requests
import json
from common.commonData import CommonData
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=UTF-8'}

    def post(self,path,data):
        proxies=CommonData.proxies
        host=CommonData.host
        data_json=json.dumps(data) #将data参数转化为json格式
        if CommonData.token is not None:
             self.headers['token']=CommonData.token
        resp_login=self.http.post(url=host+path,
                           proxies=proxies,
                           data=data_json,
                           headers=self.headers)
        assert resp_login.status_code==200
        resp_json=resp_login.text #获取response相应
        resp_dict=json.loads(resp_json) #将body值转化为dict
        return resp_dict

# http=requests.session()
# resp_dict=json.loads(resp.text)
# token=resp_dict['object']['token']
# headers['token']=token
# data={'token':token}
# data_json=json.dumps(data)
# resp=http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                    proxies=proxies,
#                    data='{"token":"'+ token +'"}',
#                    headers=headers)


