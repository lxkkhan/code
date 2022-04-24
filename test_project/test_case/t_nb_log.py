from nb_log import LogManager

logger = LogManager('log_demo').get_logger_and_add_handlers(log_filename='APITest.log')
print('haha ')
logger.info('你好')
logger.warning('警告')
logger.error('这是错误日志')
logger.debug('debug')
logger.critical('critical')