from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass

class Comparable(ABC):
    @abstractmethod
    def compare(self, other) -> int:
        pass


class Character:
    MAX_LEVEL = 100
    BASE_HEALTH = 100
    HEALTH_PER_LEVEL = 15
    EXP_PER_LEVEL = 100

    def __init__(self, name, level=1, health=None, experience=0):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой")
        self._name = name.strip()

        if not isinstance(level, (int, float)) or level < 1 or level > self.MAX_LEVEL:
            raise ValueError(f"Уровень должен быть от 1 до {self.MAX_LEVEL}")
        self._level = int(level)

        if not isinstance(experience, (int, float)) or experience < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self._experience = float(experience)

        if health is None:
            self._health = self.max_health
        else:
            if not isinstance(health, (int, float)) or health < 0 or health > self.max_health:
                raise ValueError(f"Здоровье должно быть от 0 до {self.max_health}")
            self._health = float(health)

        self._state = "alive"

    @property
    def max_health(self):
        return self.BASE_HEALTH + (self._level - 1) * self.HEALTH_PER_LEVEL

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def health(self):
        return self._health

    @property
    def experience(self):
        return self._experience

    @property
    def state(self):
        return self._state

    def _check_alive(self, action):
        if self._state != "alive":
            raise RuntimeError(f"Невозможно {action}: персонаж мёртв")

    def take_damage(self, amount):
        self._check_alive("получение урона")
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            self._state = "dead"
            print(f"{self._name} погиб!")

    def heal(self, amount):
        self._check_alive("лечение")
        if amount < 0:
            raise ValueError("Лечение не может быть отрицательным")
        self._health = min(self._health + amount, self.max_health)

    def gain_experience(self, amount):
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

    def __str__(self):
        return f"{self._name} (ур.{self._level}, зд.{self._health:.0f}/{self.max_health:.0f})"



class Voin(Character, Printable, Comparable):
    def __init__(self, name, level=1, health=None, experience=0, aura=0, motivazia=0):
        super().__init__(name, level, health, experience)
        self.aura = aura
        self.motivazia = motivazia

    def kill_mag(self, target_mag):
        self._check_alive("убийство мага")
        self.aura += 1000
        self.motivazia += 1000
        target_mag.take_damage(9999)
        return f'{self.name} безжалостно убил {target_mag.name}. Аура: {self.aura}. Мотивация: {self.motivazia}'

    def attack_mag(self, target_mag):
        self._check_alive("атака")
        damage = self._level * 10 + (self.aura // 100)
        target_mag.take_damage(damage)
        self.aura += 100
        return f'Воин {self.name} атакует {target_mag.name} и наносит {damage} урона! Аура: {self.aura}'

    def make_sound(self):
        return f"{self.name}: Кто последний, тот отчислен!"

    def use_skill(self, target_mag):
        return self.kill_mag(target_mag)

    def to_string(self) -> str:
        return f"Воин {self.name}: уровень {self.level}, аура {self.aura}, мотивация {self.motivazia}"

    def compare(self, other) -> int:
        if not isinstance(other, Voin):
            raise TypeError("Можно сравнивать только с Voin")
        if self.aura < other.aura:
            return -1
        elif self.aura > other.aura:
            return 1
        return 0

    def __str__(self):
        return f"Voin: {self.name} (ур.{self.level}, аура {self.aura})"



class Mag(Character, Printable, Comparable):
    def __init__(self, name, level=1, health=None, experience=0, mana=50, sleep=0):
        super().__init__(name, level, health, experience)
        self.mana = mana
        self.sleep = sleep

    def kill_voin(self, target_voin):
        self._check_alive("убийство воина")
        target_voin.take_damage(9999)
        self.mana += 100
        self.sleep += 10
        return f'{self.name} безжалостно убил {target_voin.name}. Мана: {self.mana}. Сонливость: {self.sleep}'

    def attack_voin(self, target_voin):
        self._check_alive("атака")
        if self.mana < 10:
            raise ValueError("Недостаточно маны")
        damage = self._level * 12
        self.mana -= 10
        self.sleep += 5
        target_voin.take_damage(damage)
        return f"Маг {self.name} атакует {target_voin.name} и наносит {damage} урона! Мана: {self.mana}"

    def make_sound(self):
        return f"{self.name}: Кто первый, тот красавчик!"

    def use_skill(self, target_voin):
        return self.kill_voin(target_voin)

    def to_string(self) -> str:
        return f"Маг {self.name}: уровень {self.level}, мана {self.mana}, сонливость {self.sleep}"

    def compare(self, other) -> int:
        if not isinstance(other, Mag):
            raise TypeError("Можно сравнивать только с Mag")
        if self.mana < other.mana:
            return -1
        elif self.mana > other.mana:
            return 1
        return 0

    def __str__(self):
        return f"Mag: {self.name} (ур.{self.level}, мана {self.mana})"


class CharacterTeam:
    def __init__(self, items=None):
        self._items = list(items) if items else []

    def add(self, character):
        if not isinstance(character, Character):
            raise TypeError("Можно добавлять только объекты Character")
        if self.find_by_name(character.name) is not None:
            raise ValueError(f"Персонаж с именем '{character.name}' уже существует")
        self._items.append(character)

    def remove(self, character):
        if character not in self._items:
            raise ValueError("Такого персонажа нет в коллекции")
        self._items.remove(character)

    def get_all(self):
        return self._items.copy()

    def find_by_name(self, name):
        for c in self._items:
            if c.name == name:
                return c
        return None

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    # для лр 5
    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        new_items = [item for item in self._items if predicate(item)]
        return CharacterTeam(new_items)

    def apply(self, func):
        for item in self._items:
            func(item)
        return self

    def map_to(self, transform_func):
        return list(map(transform_func, self._items))

    def __str__(self):
        if not self._items:
            return "Коллекция пуста"
        return "\n".join(str(item) for item in self._items)