import logging

logging.info('Немного информации')
logging.error('Поймали ошибку')

"""Уровни логирования
По умолчанию логгер имеет следующие уровни журналирования
● NOTSET, 0 — уровень не установлен. Регистрируются все события.
● DEBUG, 10 — подробная информация, обычно представляющая интерес
только при диагностике проблем.
● INFO, 20 — подтверждение того, что все работает так, как ожидалось.
● WARNING, 30 — указание на то, что произошло что-то неожиданное, или
указание на какую-то проблему в ближайшем будущем (например,
«недостаточно места на диске»). Программное обеспечение по-прежнему
работает, как ожидалось.
● ERROR, 40 — из-за более серьезной проблемы программное обеспечение не
может выполнять некоторые функции.
● CRITICAL, 50 — серьезная ошибка, указывающая на то, что сама программа не
может продолжать работу.
Уровень NOTSET используется как значение по умолчанию при создании
обработчиков событий. Все остальные уровни имеют одноимённые функции —
регистраторы, которые позволяют зафиксировать события заданного уровня.
Кроме того уровни имеют числовой эквивалент от 0 до 50. Он нужен при создании
своих уровней логирования, чтобы определить место обработчика относительно
базовых"""