"""
Тема: ООП Ч10. Знакомство с паттернами. Урок: 29
- Одиночка (Singleton)
    - Простой пример
    - Пример логгера
"""

# Импорт логгера Python
import logging
from logging import Logger, StreamHandler, Formatter
from typing import Optional, Literal, Any, ClassVar

# Импорт пакета для работы с датой и временем
import datetime

# Импорт библиотеки для цветного вывода
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

# Типы уровней логирования
LogLevel = Literal['info', 'debug', 'warning', 'error', 'critical']

class LoggerSingleton:
    """
    Класс LoggerSingleton - реализация паттерна Одиночка для логгера с цветным выводом.
    Обеспечивает единую точку логирования в приложении.
    
    Примеры использования:
        logger = LoggerSingleton()
        logger.log("Информационное сообщение")
        
        # Изменение уровня логирования через property
        logger.log_level = logging.DEBUG
        logger.log("Отладочное сообщение", 'debug')
    """
    # Статическая переменная для хранения единственного экземпляра
    _instance: ClassVar[Optional['LoggerSingleton']] = None
    
    # Цвета для разных уровней логирования
    _log_colors: ClassVar[dict[str, str]] = {
        'debug': Fore.CYAN,
        'info': Fore.GREEN,
        'warning': Fore.YELLOW,
        'error': Fore.RED,
        'critical': Fore.MAGENTA + Style.BRIGHT
    }
    
    def __new__(cls, log_level: int = logging.INFO) -> 'LoggerSingleton':
        """
        Переопределение метода создания экземпляра класса.
        Гарантирует, что будет создан только один экземпляр.
        
        Args:
            log_level: Уровень логирования из модуля logging (по умолчанию INFO)
            
        Returns:
            Экземпляр класса LoggerSingleton
        """
        if cls._instance is None:
            # Если экземпляр еще не создан, создаем его
            cls._instance = super().__new__(cls)
            # Флаг, чтобы отслеживать, был ли инициализирован объект
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, log_level: int = logging.INFO) -> None:
        """
        Инициализатор класса.
        Если экземпляр уже инициализирован, просто обновляет уровень логирования.
        
        Args:
            log_level: Уровень логирования из модуля logging (по умолчанию INFO)
        """
        if not getattr(self, '_initialized', False):
            # Первоначальная инициализация логгера
            self.logger: Logger = logging.getLogger('singleton_logger')
            handler = StreamHandler()
            
            # Создаем форматтер без цвета (цвет добавляем в методе log)
            formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            
            # Проверяем, не были ли уже добавлены обработчики
            if not self.logger.handlers:
                self.logger.addHandler(handler)
            
            self.logger.setLevel(log_level)
            self._initialized = True
    
    @property
    def log_level(self) -> int:
        """
        Получение текущего уровня логирования.
        
        Returns:
            Текущий уровень логирования
        """
        return self.logger.level
    
    @log_level.setter
    def log_level(self, level: int) -> None:
        """
        Установка уровня логирования.
        
        Args:
            level: Новый уровень логирования из модуля logging
        """
        self.logger.setLevel(level)
        print(f"{Fore.BLUE}Уровень логирования изменен на: {logging.getLevelName(level)}{Style.RESET_ALL}")
    
    def log(self, message: str, level: LogLevel = 'info') -> None:
        """
        Метод для логирования сообщений с цветным выводом.
        
        Args:
            message: Сообщение для логирования
            level: Уровень логирования (info, debug, warning, error, critical)
        """
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Получаем цвет для данного уровня логирования
        color = self._log_colors.get(level, Fore.WHITE)
        colored_message = f"{color}{timestamp} - {message}{Style.RESET_ALL}"
        
        match level.lower():
            case 'info':
                self.logger.info(colored_message)
            case 'debug':
                self.logger.debug(colored_message)
            case 'warning':
                self.logger.warning(colored_message)
            case 'error':
                self.logger.error(colored_message)
            case 'critical':
                self.logger.critical(colored_message)
            case _:
                self.logger.info(colored_message)
    
    def __str__(self) -> str:
        """
        Строковое представление объекта.
        
        Returns:
            Строка с информацией о логгере
        """
        return f'Логгер-одиночка (id: {id(self)}), уровень: {logging.getLevelName(self.logger.level)}'


# Примеры использования
if __name__ == '__main__':
    # Создаем первый экземпляр логгера с уровнем INFO
    logger1 = LoggerSingleton(logging.INFO)
    print(logger1)
    logger1.log("Это информационное сообщение")
    
    # Создаем "второй" экземпляр логгера и меняем уровень через property
    logger2 = LoggerSingleton()
    logger2.log_level = logging.DEBUG  # Используем setter для изменения уровня
    print(logger2)
    
    # Проверяем, что это тот же объект
    print(f"logger1 is logger2: {logger1 is logger2}")
    
    # Логируем с разными уровнями
    logger2.log("Это отладочное сообщение", 'debug')
    logger2.log("Это предупреждение", 'warning')
    logger2.log("Это ошибка", 'error')
    logger2.log("Это критическая ошибка", 'critical')
    
    # Создаем "третий" экземпляр и устанавливаем уровень ERROR
    logger3 = LoggerSingleton()
    logger3.log_level = logging.ERROR  # Используем setter
    print(logger3)
    
    # Эти сообщения не будут выведены из-за уровня логирования ERROR
    logger3.log("Это информационное сообщение не будет выведено", 'info')
    logger3.log("Это предупреждение не будет выведено", 'warning')
    
    # А эти будут выведены
    logger3.log("Эта ошибка будет выведена", 'error')
    logger3.log("Эта критическая ошибка будет выведена", 'critical')
    
    # Демонстрация работы с одним экземпляром
    print(f"\nВсе экземпляры совпадают:")
    print(f"logger1: {id(logger1)}")
    print(f"logger2: {id(logger2)}")
    print(f"logger3: {id(logger3)}")
