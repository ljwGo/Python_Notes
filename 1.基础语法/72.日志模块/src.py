# 接下来要做的是：拿到日志的产生者即loggers来产生日志
# 第一个日志的产生者：kkk
# 第二个日志的产生者：bbb
import settings
from logging import config,getLogger

config.dictConfig(settings.LOGGING_DIC)
logger1 = getLogger('kkk')