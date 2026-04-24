# interfaces.py
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass

class Comparable(ABC):
    @abstractmethod
    def compare(self, other) -> int:
        pass