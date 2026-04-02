
from validate import (
    validate_name,
    validate_level,
    validate_health,
    validate_experience,
    validate_damage,
    validate_heal,
    validate_experience_gain
)


class Character:
    MAX_LEVEL = 100
    BASE_HEALTH = 100
    HEALTH_PER_LEVEL = 15
    EXP_PER_LEVEL = 100

    def __init__(self, name, level=1, health=None, experience=0):
        self._name = validate_name(name)
        self._level = validate_level(level)
        
        if self._level > self.MAX_LEVEL:
            raise ValueError(f"Уровень не может превышать {self.MAX_LEVEL}")
        
        self._experience = validate_experience(experience)
        
        if health is None:
            self._health = self.max_health
        else:
            self._health = validate_health(health, self.max_health)
        
        self._state = "alive"
    
    @property
    def max_health(self):
        return self.BASE_HEALTH + (self._level - 1) * self.HEALTH_PER_LEVEL
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = validate_name(value)
    
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
    
    def _check_experience_for_level_up(self):
        exp_needed = self.EXP_PER_LEVEL * self._level
        while self._experience >= exp_needed and self._level < self.MAX_LEVEL:
            self._level_up()
            exp_needed = self.EXP_PER_LEVEL * self._level
    
    def _level_up(self):
        if self._level >= self.MAX_LEVEL:
            raise RuntimeError("Достигнут максимальный уровень")
        
        self._level += 1
        self._health = self.max_health
        
        exp_needed = self.EXP_PER_LEVEL * (self._level - 1)
        self._experience -= exp_needed
        
        print(f"{self._name} повысил уровень до {self._level}!")
    
    def take_damage(self, amount):
        self._check_alive("получение урона")
        amount = validate_damage(amount)
        
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            self._state = "dead"
            print(f"{self._name} погиб!")
    
    def heal(self, amount):
        self._check_alive("лечение")
        amount = validate_heal(amount)
        
        self._health += amount
        if self._health > self.max_health:
            self._health = self.max_health
    
    def gain_experience(self, amount):
        self._check_alive("получение опыта")
        amount = validate_experience_gain(amount)
        
        self._experience += amount
        self._check_experience_for_level_up()
    
    def level_up(self):
        self._check_alive("повышение уровня")
        self._level_up()
    
    def attack(self, target):
        self._check_alive("атака")
        
        if not isinstance(target, Character):
            raise TypeError("Цель должна быть персонажем")
        
        damage = self._level * 10
        print(f"{self._name} атакует {target._name} и наносит {damage} урона")
        target.take_damage(damage)
    
    def __str__(self):
        return (f"Персонаж {self._name} (ур. {self._level}), "
                f"здоровье: {self._health:.1f}/{self.max_health:.1f}, "
                f"опыт: {self._experience:.1f}, статус: {self._state}")
    
    def __repr__(self):
        return f"Character('{self._name}', {self._level}, {self._health:.1f}, {self._experience:.1f})"
    
    def __eq__(self, other):
        if not isinstance(other, Character):
            return False
        return self._name == other._name and self._level == other._level