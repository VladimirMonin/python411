"""
Тема: ООП Ч10. Знакомство с паттернами. Урок: 29
- Одиночка (Singleton)
    - Простой пример
    - Пример логгера
"""

# Импорт логгера Python
import logging

# Импорт пакета для работы с датой и временем
import datetime

class LoggerSingleton:
    """
    Класс LoggerSingleton - реализация паттерна Одиночка для логгера.
    Обеспечивает единую точку логирования в приложении.
    """
    # Статическая переменная для хранения единственного экземпляра
    _instance = None
    
    def __new__(cls, log_level=logging.INFO):
        """
        Переопределение метода создания экземпляра класса.
        Гарантирует, что будет создан только один экземпляр.
        """
        if cls._instance is None:
            # Если экземпляр еще не создан, создаем его
            cls._instance = super().__new__(cls)
            # Флаг, чтобы отслеживать, был ли инициализирован объект
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, log_level=logging.INFO):
        """
        Инициализатор класса.
        Если экземпляр уже инициализирован, просто обновляет уровень логирования.
        """
        if not self._initialized:
            # Первоначальная инициализация логгера
            self.logger = logging.getLogger('singleton_logger')
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(log_level)
            self._initialized = True
        else:
            # Если экземпляр уже существует, просто обновляем уровень логирования
            self.logger.setLevel(log_level)
    
    def log(self, message, level='info'):
        """
        Метод для логирования сообщений.
        
        :param message: Сообщение для логирования
        :param level: Уровень логирования (info, debug, warning, error, critical)
        """
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        match level.lower():
            case 'info':
                self.logger.info(f'{timestamp} - {message}')
            case 'debug':
                self.logger.debug(f'{timestamp} - {message}')
            case 'warning':
                self.logger.warning(f'{timestamp} - {message}')
            case 'error':
                self.logger.error(f'{timestamp} - {message}')
            case 'critical':
                self.logger.critical(f'{timestamp} - {message}')
            case _:
                self.logger.info(f'{timestamp} - {message}')
    
    def __str__(self):
        """Строковое представление объекта"""
        return f'Логгер-одиночка (id: {id(self)}), уровень: {logging.getLevelName(self.logger.level)}'


# Примеры использования
if __name__ == '__main__':
    # Создаем первый экземпляр логгера с уровнем INFO
    logger1 = LoggerSingleton(logging.INFO)
    print(logger1)
    logger1.log("Это информационное сообщение")
    
    # Создаем "второй" экземпляр логгера с уровнем DEBUG
    # На самом деле будет возвращен тот же экземпляр, но с обновленным уровнем
    logger2 = LoggerSingleton(logging.DEBUG)
    print(logger2)
    
    # Проверяем, что это тот же объект
    print(f"logger1 is logger2: {logger1 is logger2}")
    
    # Логируем с разными уровнями
    logger2.log("Это отладочное сообщение", 'debug')
    logger2.log("Это предупреждение", 'warning')
    logger2.log("Это ошибка", 'error')
    logger2.log("Это критическая ошибка", 'critical')
    
    # Создаем "третий" экземпляр с уровнем ERROR
    # Все сообщения ниже уровня ERROR будут игнорироваться
    logger3 = LoggerSingleton(logging.ERROR)
    print(logger3)
    
    # Эти сообщения не будут выведены из-за уровня логирования ERROR
    logger3.log("Это информационное сообщение не будет выведено", 'info')
    logger3.log("Это предупреждение не будет выведено", 'warning')
    
    # А эти будут выведены
    logger3.log("Эта ошибка будет выведена", 'error')
    logger3.log("Эта критическая ошибка будет выведена", 'critical')
