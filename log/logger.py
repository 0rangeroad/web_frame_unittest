import logging
import logging.handlers
import os


class Log:
    # 采用单例模式封装日志
    # 设置log为None
    log = None

    @classmethod
    def get_log(cls):
        # 如果log为None代码向下走，如果不是None则不执行代码，保证使用的是同一个log
        if cls.log is None:
            # 实例化logger，创建日志器
            cls.log = logging.getLogger()
            # 设置日志器的最低等级
            cls.log.setLevel(logging.INFO)
            # 创建控制台处理器
            stream_log = logging.StreamHandler()
            # 创建文件处理器
            img_path = os.path.dirname(__file__) + "/log.yaml"
            file_log = logging.handlers.TimedRotatingFileHandler(img_path,
                                                                 when="midnight",
                                                                 interval=1,
                                                                 backupCount=30,
                                                                 encoding="utf-8")
            file_log.setLevel(logging.ERROR)
            # 设置日志格式
            fmt = "%(asctime)s [%(levelname)s] [%(filename)s %(funcName)s:%(lineno)d] - %(message)s"
            # 获取日志格式器
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            stream_log.setFormatter(fm)
            file_log.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.log.addHandler(stream_log)
            cls.log.addHandler(file_log)
            # 返回日志器
        return cls.log
