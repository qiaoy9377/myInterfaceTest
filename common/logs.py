'''
功能描述：自定义log，方便输出代码过程信息
实现逻辑：
1-定义log基本设置，重写basicconfig方法，定义等级、日志输出格式
2-创建log解释器并命名
'''

import logging

def log():
    #定义log等级，输出格式
    logging.basicConfig(level=logging.INFO,format=format('%(name)s-%(asctime)s-%(levelname)s-[line:%(lineno)d]-%(message)s'))
    #创建log解释器，并返回
    logger = logging.getLogger('myLog')
    return logger

#初始化log类的实例对象
logger = log()

if __name__ == '__main__':
    logger.info('test')