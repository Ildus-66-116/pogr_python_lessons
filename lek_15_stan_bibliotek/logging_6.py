"""● “%” — старый стиль форматирования текста с использованием символа %.
Это стиль по умолчанию для задания формата. Сохранён он для поддержки
обратной совместимости код. Ведь логирование работа ещё в Python 1.5.2
созданном в прошлом тысячелетии.
● “{“ — форматирование с использованием фигурных скобок. Метод str.format.
● “$” — форматирование в стиле string.Template с использованием денежного
символа для указания имени переменной."""
import logging
from other import log_all

FORMAT = ('{levelname:<8} - {asctime}. В модуле "{name}" '
          'в строке {lineno:03d} функция "{funcName}()" '
          'в {created} секунд записала сообщение: {msg}')
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger('main')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
