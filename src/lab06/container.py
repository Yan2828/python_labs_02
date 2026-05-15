from typing import TypeVar, Generic, Callable, Optional, Protocol
from abc import ABC, abstractmethod

class Character:
    MAX_LEVEL: int = 100
    BASE_HEALTH: float = 100.0
    HEALTH_PER_LEVEL: float = 15.0
    EXP_PER_LEVEL: float = 100.0

    def __init__(self, name: str, level: int = 1, health: Optional[float] = None, experience: float = 0.0) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой")
        self._name: str = name.strip()

        if not isinstance(level, (int, float)) or level < 1 or level > self.MAX_LEVEL:
            raise ValueError(f"Уровень должен быть от 1 до {self.MAX_LEVEL}")
        self._level: int = int(level)

        if not isinstance(experience, (int, float)) or experience < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self._experience: float = float(experience)

        if health is None:
            self._health: float = self.max_health
        else:
            if not isinstance(health, (int, float)) or health < 0 or health > self.max_health:
                raise ValueError(f"Здоровье должно быть от 0 до {self.max_health}")
            self._health: float = float(health)

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
            print(f"{self._name} погиб!")

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
        exp_needed = self.EXP_PER_LEVEL * self._level
        while self._experience >= exp_needed and self._level < self.MAX_LEVEL:
            self._level += 1
            self._experience -= exp_needed
            print(f"{self._name} повысил уровень до {self._level}!")
            exp_needed = self.EXP_PER_LEVEL * self._level

    def __str__(self) -> str:
        return f"{self._name} (ур.{self._level}, зд.{self._health:.0f}/{self.max_health:.0f})"

class Voin(Character):
    def __init__(self, name: str, level: int = 1, health: Optional[float] = None,
                 experience: float = 0.0, aura: int = 0, motivazia: int = 0) -> None:
        super().__init__(name, level, health, experience)
        self.aura: int = aura
        self.motivazia: int = motivazia

    # Метод для протокола Displayable
    def display(self) -> str:
        return f"Воин {self.name}: аура {self.aura}, уровень {self.level}"

    # Метод для протокола Scorable
    def score(self) -> float:
        return float(self.aura)

    def __str__(self) -> str:
        return f"Voin: {self.name} (ур.{self.level}, аура {self.aura})"

class Mag(Character):
    def __init__(self, name: str, level: int = 1, health: Optional[float] = None,
                 experience: float = 0.0, mana: int = 50, sleep: int = 0) -> None:
        super().__init__(name, level, health, experience)
        self.mana: int = mana
        self.sleep: int = sleep

    def display(self) -> str:
        return f"Маг {self.name}: мана {self.mana}, уровень {self.level}"

    def score(self) -> float:
        return float(self.mana)

    def __str__(self) -> str:
        return f"Mag: {self.name} (ур.{self.level}, мана {self.mana})"

class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...

D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)
T = TypeVar('T')    
R = TypeVar('R')          

class TypedCollection(Generic[T]):

    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]


    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"
        return "\n".join(str(item) for item in self._items)