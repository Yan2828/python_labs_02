from collection import Voin, Mag

def by_name(obj):
    return obj.name

def by_level(obj):
    return obj.level

def by_aura(obj):
    return obj.aura if hasattr(obj, 'aura') else 0

def by_mana(obj):
    return obj.mana if hasattr(obj, 'mana') else 0

def make_sort_by_attr(attr_name):
    """Фабрика: создаёт функцию-ключ для сортировки по заданному атрибуту."""
    def key_func(obj):
        return getattr(obj, attr_name, 0)
    return key_func

def is_alive(obj):
    return obj.state == "alive"

def is_warrior(obj):
    return isinstance(obj, Voin)

def is_mage(obj):
    return isinstance(obj, Mag)


def make_min_level_filter(min_level):
    
    def predicate(obj):
        return obj.level >= min_level
    
    return predicate

def make_max_health_filter(max_health):
    return lambda obj: obj.health <= max_health

# CALLABLE

class SortByAttribute:
    
    def __init__(self, attr_name):
        self.attr_name = attr_name
    def __call__(self, obj):
        return getattr(obj, self.attr_name, 0)

class FilterByType:

    def __init__(self, class_type):
        self.class_type = class_type
    def __call__(self, obj):
        return isinstance(obj, self.class_type)

class AddExperienceStrategy:

    def __init__(self, amount):
        self.amount = amount
    def __call__(self, obj):
        obj.gain_experience(self.amount)

class HealStrategy:

    def __call__(self, obj):
        obj.heal(obj.max_health)

# map
def to_name(obj):
    return obj.name

def to_level_and_name(obj):
    return f"Уровень {obj.level}: {obj.name}"