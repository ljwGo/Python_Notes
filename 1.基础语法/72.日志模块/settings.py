standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    # handlers是日志的接受者，不同的handler会将日志输出到不同的位置
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        # 'default': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
        #     'formatter': 'standard',
        #     # 可以定制日志文件路径
        #     # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
        #     # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
        #     'filename': 'a1.log',  # 日志文件
        #     'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
        #     'backupCount': 5,
        #     'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        # },
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'test',
            'filename': 'a2.log',
            'encoding': 'utf-8',
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': 'a1.log',
            'encoding': 'utf-8',
        }
    },
    # loggers是日志的产生着，会将产生的日志交给handlers处理
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        'kkk': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        'bbb': {
            'handlers': ['other', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ddd': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handles': ['default', ],
            'level': 'DEBUG',
            'propagate': False,
        }
    },
}
