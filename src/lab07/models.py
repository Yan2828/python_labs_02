# models.py
from typing import TypeVar, Generic, Callable, Optional, Protocol, List
from abc import ABC, abstractmethod
import json

# ---------- Базовый класс Character ----------
class Character:
    MAX_LEVEL = 100
    BASE_HEALTH = 100.0
    HEALTH_PER_LEVEL = 15.0
    EXP_PER_LEVEL = 100.0

    def __init__(self, name: str, level: int = 1, health: Optional[float] = None, experience: float = 0.0) -> None:
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        self._name: str = name.strip()
        if not 1 <= level <= self.MAX_LEVEL:
            raise ValueError(f"Уровень должен быть от 1 до {self.MAX_LEVEL}")
        self._level: int = level
        if experience < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self._experience: float = float(experience)
        self._health: float = self.max_health if health is None else float(health)
        if self._health > self.max_health:
            self._health = self.max_health
        self._state: str = "alive"

    @property
    def max_health(self) -> float:
        return self.BASE_HEALTH + (self._level - 1) * self.HEALTH_PER_LEVEL

    @property
    def name(self) -> str:
        return self._name

    @property
    def level(self) -> int:
        return self._level

    @property
    def health(self) -> float:
        return self._health

    @property
    def experience(self) -> float:
        return self._experience

    @property
    def state(self) -> str:
        return self._state

    def _check_alive(self, action: str) -> None:
        if self._state != "alive":
            raise RuntimeError(f"Невозможно {action}: персонаж мёртв")

    def take_damage(self, amount: float) -> None:
        self._check_alive("получение урона")
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._health -= amount
        if self._health <= 0:
            self._health = 0.0
            self._state = "dead"

    def heal(self, amount: float) -> None:
        self._check_alive("лечение")
        if amount < 0:
            raise ValueError("Лечение не может быть отрицательным")
        self._health = min(self._health + amount, self.max_health)

    def gain_experience(self, amount: float) -> None:
        self._check_alive("получение опыта")
        if amount < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self._experience += amount
        while self._experience >= self.EXP_PER_LEVEL * self._level and self._level < self.MAX_LEVEL:
            self._level += 1
            self._experience -= self.EXP_PER_LEVEL * (self._level - 1)
            print(f"{self._name} повысил уровень до {self._level}!")

    def to_dict(self) -> dict:
        """Сериализация в словарь для JSON."""
        base = {
            "type": self.__class__.__name__,
            "name": self._name,
            "level": self._level,
            "health": self._health,
            "experience": self._experience,
            "state": self._state,
        }
        return base

    @classmethod
    def from_dict(cls, data: dict):
        """Воссоздание объекта из словаря. Должен быть переопределён в наследниках."""
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self._name} (ур.{self._level}, зд.{self._health:.0f}/{self.max_health:.0f})"


# ---------- Voin ----------
class Voin(Character):
    def __init__(self, name: str, level: int = 1, health: Optional[float] = None, experience: float = 0.0,
                 aura: int = 0, motivazia: int = 0) -> None:
        super().__init__(name, level, health, experience)
        self.aura: int = aura
        self.motivazia: int = motivazia

    def to_dict(self) -> dict:
        d = super().to_dict()
        d["aura"] = self.aura
        d["motivazia"] = self.motivazia
        return d

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            level=data["level"],
            health=data.get("health"),
            experience=data.get("experience", 0),
            aura=data.get("aura", 0),
            motivazia=data.get("motivazia", 0)
        )

    def __str__(self) -> str:
        return f"Воин {self.name} (ур.{self.level}, аура {self.aura})"


# ---------- Mag ----------
class Mag(Character):
    def __init__(self, name: str, level: int = 1, health: Optional[float] = None, experience: float = 0.0,
                 mana: int = 50, sleep: int = 0) -> None:
        super().__init__(name, level, health, experience)
        self.mana: int = mana
        self.sleep: int = sleep

    def to_dict(self) -> dict:
        d = super().to_dict()
        d["mana"] = self.mana
        d["sleep"] = self.sleep
        return d

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            level=data["level"],
            health=data.get("health"),
            experience=data.get("experience", 0),
            mana=data.get("mana", 50),
            sleep=data.get("sleep", 0)
        )

    def __str__(self) -> str:
        return f"Маг {self.name} (ур.{self.level}, мана {self.mana})"


# ---------- Generic-коллекция (упрощённая версия из ЛР-6) ----------
T = TypeVar('T')

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> List[T]:
        return list(self._items)

    def find_by_name(self, name: str) -> Optional[T]:
        for item in self._items:
            if hasattr(item, 'name') and item.name == name:
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)