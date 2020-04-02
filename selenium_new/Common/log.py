# coding=utf-8

import logging
import time

from Common.function import project_path


class FrameLog():
    def __init__(self, logger=None):
        # 创建一个logger
        self.logger = logging.getLogger(logger)  # 创建一个logger
        self.logger.setLevel(logging.DEBUG)  # 指定日志级别

        # 创建一个handle， 用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        # 路径需要修改
        self.log_path = project_path() + "/Logs/"
        self.log_name = self.log_path + self.log_time + 'log.log'
        self.file_handle = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        """
       设置日志格式
           %(asctime)s         日志事件发生的时间
           %(filename)s        pathname的文件名部分，包含文件后缀
           %(funcName)s        调用日志记录函数的函数名
           %(levelname)s       该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
           %(message)s         日志记录的文本内容
       """
        file_formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d '
                                           '[%(levelname)s] %(message)s')
        self.file_handle.setFormatter(file_formatter)
        # 给logger添加handler
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    # 关闭handle
    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    log = FrameLog()
    logger = log.get_log()
    logger.info("info")
    logger.debug("debug")
    logger.error("error")
    logger.critical("critical")
    log.close_handle()