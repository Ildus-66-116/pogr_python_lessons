import logging

logging.basicConfig(level=logging.NOTSET)
logging.debug('Очень подробная отладочная информация. Заменяеммножество "принтов"')
logging.info('Немного информации о работе кода')
logging.warning('Внимание! Надвигается буря!')
logging.error('Поймали ошибку. Дальше только неизвестность')
logging.critical('На этом всё')
