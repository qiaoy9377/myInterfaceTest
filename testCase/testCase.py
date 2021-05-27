'''
功能描述：获取readExcel的结果数据，调用configHttp执行请求，得到请求结果，断言请求结果，写入报告
实现逻辑：
1-获取readexcel的数据结果
2-将测试数据传入configHttp模块执行请求，返回结果
3-断言测试结果
4-写入excel
'''
import unittest
from common.readExcel import ReadExcel
from ddt import ddt,data,unpack
from common.configHttp import ConfigHttp
from common.logs import logger

re = ReadExcel()
data_list = re.get_data()
@ddt
class TestCase(unittest.TestCase):

    @data(*data_list)
    @unpack
    def test_case1(self,id,interfaceurl,name,body,method,expect,real,status):
        ch = ConfigHttp(interfaceurl, eval(body), method)
        status_code, real_errorCode = ch.runRequest()
        try:
            self.assertEqual(int(status_code),200)
            self.assertEqual(str(real_errorCode),str(expect))
            status = 'success'
        except Exception as msg:
            status = 'fail'
            logger.info(f'请求失败：{msg}')

if __name__ == '__main__':
    unittest.main(verbosity=2)


