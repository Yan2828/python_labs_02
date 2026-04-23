# interfaces.py
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        """Вернуть строковое представление объекта"""
        pass

class Comparable(ABC):
    @abstractmethod
    def compare(self, other) -> int:
        """
        Сравнить текущий объект с другим.
        Возвращает: -1 (self < other), 0 (равны), 1 (self > other)
        """
        pass