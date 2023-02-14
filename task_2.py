"""
2. Какие ты видишь проблемы в следующем фрагменте кода?
Как его следует исправить?
Исправь ошибку и перепиши код с использованием типизации.

>>> В lambda функции использовалась одна и та же переменная step = 4,
>>> Необходимо было добавить аргумент lambda функции со значением step.
"""
from typing import Callable, Any


def create_handlers(callback: Callable[[int], Any]) -> list:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step))
    return handlers


def execute_handlers(handlers: list) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
