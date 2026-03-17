class Character:
    MAX_LEVEL = 100
    BASE_HEALTH = 100
    HEALTH_PER_LEVEL = 10

    def __init__(self, name, level=1, health=None, experience=0):
        self._name = self._validate_name(name)
        self._level = self._validate_level(level)
        self._experience = self._validate_experience(experience)
        # health: if None, set to max health for this level
        if health is None:
            health = self.max_health
        else:
            health = self._validate_health(health)
        self._health = health
        self._state = "alive"  # alive, dead

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if len(name.strip()) == 0:
            raise ValueError("Имя не может быть пустым")
        return name.strip()

    def _validate_level(self, level):
        if not isinstance(level, int):
            raise TypeError("Уровень должен быть целым числом")
        if level < 1 or level > self.MAX_LEVEL:
            raise ValueError(f"Уровень должен быть от 1 до {self.MAX_LEVEL}")
        return level

    def _validate_health(self, health):
        if not isinstance(health, (int, float)):
            raise TypeError("Здоровье должно быть числом")
        if health < 0:
            raise ValueError("Здоровье не может быть отрицательным")
        if health > self.max_health:
            raise ValueError(f"Здоровье не может превышать максимум ({self.max_health})")
        return float(health)

    def _validate_experience(self, exp):
        if not isinstance(exp, (int, float)):
            raise TypeError("Опыт должен быть числом")
        if exp < 0:
            raise ValueError("Опыт не может быть отрицательным")
        return float(exp)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._validate_name(value)

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

    @property
    def max_health(self):
        return self.BASE_HEALTH + self._level * self.HEALTH_PER_LEVEL

    def __str__(self):
        return f"Персонаж {self._name} (ур. {self._level}), здоровье: {self._health:.1f}/{self.max_health:.1f}, опыт: {self._experience:.1f}, статус: {self._state}"

    def __repr__(self):
        return f"Character('{self._name}', {self._level}, {self._health}, {self._experience})"

    def __eq__(self, other):
        if not isinstance(other, Character):
            return False
        return self._name == other._name and self._level == other._level  # можно по имени, но лучше добавить уникальный id? Для простоты по имени и уровню.

    def _check_alive(self, action=""):
        if self._state != "alive":
            raise RuntimeError(f"Невозможно {action}: персонаж мёртв")

    def take_damage(self, amount):
        self._check_alive("нанести урон")
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            self._state = "dead"
        # Не уменьшаем здоровье ниже 0

    def heal(self, amount):
        self._check_alive("лечение")
        if amount < 0:
            raise ValueError("Лечение не может быть отрицательным")
        self._health += amount
        if self._health > self.max_health:
            self._health = self.max_health

    def gain_experience(self, amount):
        self._check_alive("получение опыта")
        if amount < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self._experience += amount
        # Проверка на повышение уровня
        while self._experience >= 100 * self._level:  # Например, для повышения нужно 100 * уровень опыта
            self.level_up()

    def level_up(self):
        if self._level >= self.MAX_LEVEL:
            raise RuntimeError("Достигнут максимальный уровень")
        self._level += 1
        # Восстанавливаем здоровье до максимума нового уровня (или увеличиваем на часть)
        self._health = self.max_health
        # Можно также оставить текущее здоровье, но обычно при повышении уровня здоровье восстанавливается.
        # Для простоты: полное исцеление.

    # Дополнительный метод для демонстрации атаки на другого персонажа
    def attack(self, target):
        self._check_alive("атака")
        if not isinstance(target, Character):
            raise TypeError("Цель должна быть персонажем")
        # Простая атака: наносит урон = уровень * 10
        damage = self._level * 10
        target.take_damage(damage)
        print(f"{self._name} атакует {target._name} и наносит {damage} урона.")
        