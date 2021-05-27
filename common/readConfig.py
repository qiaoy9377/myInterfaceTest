'''
功能描述：读取配置文件信息，供testCase使用
实现逻辑：
1、读取config.ini文件
2、获取文件中的section
3、读取section下的option信息
'''

import configparser
import os
from common.logs import logger

class ReadConfig():
    def __init__(self):
        # 寻找相对路径
        cur_path = os.path.dirname(__file__)
        file_name = os.path.dirname(cur_path) + '/config.ini'
        logger.debug(file_name)
        # 实例化一个读取config文件的对象
        self.conf = configparser.ConfigParser()
        # 读文件
        self.conf.read(file_name,encoding='utf-8')

    def get_options(self,secion):
        try:
            #读取section下的options键值对
            option_list = self.conf.items(secion)
            return option_list
        except Exception as msg:
            return '系统错误：',msg

if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.get_options('redis'))