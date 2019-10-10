import logging.handlers


class GetLog():

    logger = None
    # 获取日志器方法
    @classmethod
    def get_log(cls):

        if cls.logger is None:
            # 获取 日志器
            cls.logger = logging.getLogger()
            # 设置 总级别
            cls.logger.setLevel(logging.INFO)
            # 获取 以时间分隔文件处理，处理器
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/hr.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            # 设置 处理器级别
            th.setLevel(logging.INFO)
            # 获取 以时间分隔文件处理，处理器
            th_err = logging.handlers.TimedRotatingFileHandler(filename="../log/err.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            # 设置 处理器级别
            th_err.setLevel(logging.ERROR)
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            th_err.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.logger.addHandler(th)
            cls.logger.addHandler(th_err)
            # 返回日志器(日志入口)
        return cls.logger


if __name__ == '__main__':
    log = GetLog.get_log()
    log.info("info 级别信息测试")
    log.error("error 级别信息测试")
    log.criticly("criticly严重测试")