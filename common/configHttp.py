'''
功能描述：传入method方法，判断接口请求方式，执行相应的请求，并返回请求结果给testCase
实现逻辑：
1、读取readexcel的method、body、url
2、判断method方法
    2.1如果是get方法，就用get请求
    2.2如果是post方法，就用post请求
    ......
3、返回请求的errorcode
'''
import requests

class ConfigHttp():
    #初始化请求参数
    def __init__(self,url,body,method):
        self.url = url
        self.body = body
        self.method = method

    def runRequest(self):
        if str(self.method).lower() == 'get':
            return self.__get_request()
        elif str(self.method).lower() == 'post':
            return self.__post_request()

    def __get_request(self):
        response = requests.get(url=self.url, params=self.body)
        real_errorCode = response.json()['errorCode']
        status_code = response.status_code
        return status_code,real_errorCode

    def __post_request(self):
        response = requests.post(url=self.url, data=self.body)
        real_errorCode = response.json()['errorCode']
        status_code = response.status_code
        return status_code,real_errorCode

if __name__ == '__main__':
    data_list = [{'id': 1, 'interfaceurl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'body': "{'username':'liangchao','password':'123456'}", 'method': 'post', 'expect': 0, 'real': None, 'status': None}, {'id': 2, 'interfaceurl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'body': "{'username':'liangchao03','password':'123456','repassword':'123456'}", 'method': 'post', 'expect': 0, 'real': None, 'status': None}, {'id': 3, 'interfaceurl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'body': "{'username':'liangchao'}", 'method': 'get', 'expect': 0, 'real': None, 'status': None}]
    url = data_list[0]['interfaceurl']
    body = data_list[0]['body']
    method = data_list[0]['method']
    request = ConfigHttp(url=url,body=body,method=method)
    real = request.runRequest()
    print(real)