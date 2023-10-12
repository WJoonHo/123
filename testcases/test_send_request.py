import requests


class TestSendRequests:
    access_token = ""
    token = ""
    session = requests.session()

    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid":"wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }

        rep = TestSendRequests.session.request("get", url=url, params=data)
        print(rep.json())
        TestSendRequests.access_token = rep.json()['access_token']

    def test_post_flag(self, conn_database):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token"+TestSendRequests.access_token+""
        data = {"tag": {"id":134, "name":"广东人"}}
        rep = TestSendRequests.session.request("post", url, json=data)
        print(rep.json())

    def test_post_login(self):
        url = "http://ihrm2-test.itheima.net/api/sys/login"
        data = {
    "mobile": "13800000002",
    "password": "123456"
    }
        rep = TestSendRequests.session.request("post", url, json=data)
        print(rep.json())
        TestSendRequests.token = rep.json()['data']

    def test_post_add(self):
        url = "http://ihrm2-test.itheima.net/api/sys/user"
        data = {
        "username": "王哈啦",
        "mobile": "18538178087",
        "timeOfEntry": "2023-09-11",
        "formOfEmployment": 1,
        "departmentName": "测试0789",
        "departmentId": "1412421425733889945",
        "workNumber": "389",
        "correctionTime": "2023-09-01T15:20:00.000Z"
    }
        headers = {
            "Authorization": TestSendRequests.token
        }
        rep = TestSendRequests.session.request("post", url, json=data, headers=headers)
        print(rep.json())




