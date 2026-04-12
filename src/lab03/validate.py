
def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    if not name.strip():
        raise ValueError("Имя не может быть пустым")
    return name.strip()


def validate_level(level):
    if not isinstance(level, (int, float)):
        raise TypeError("Уровень должен быть числом")
    if level < 1:
        raise ValueError("Уровень должен быть от 1 до 100")
    if level > 100:
        raise ValueError("Уровень не может превышать 100")
    return int(level)


def validate_health(health, max_health):
    if not isinstance(health, (int, float)):
        raise TypeError("Здоровье должно быть числом")
    if health < 0:
        raise ValueError("Здоровье не может быть отрицательным")
    if health > max_health:
        raise ValueError(f"Здоровье не может превышать максимум ({max_health})")
    return float(health)


def validate_experience(experience):
    if not isinstance(experience, (int, float)):
        raise TypeError("Опыт должен быть числом")
    if experience < 0:
        raise ValueError("Опыт не может быть отрицательным")
    return float(experience)


def validate_damage(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Урон должен быть числом")
    if amount < 0:
        raise ValueError("Урон не может быть отрицательным")
    return float(amount)


def validate_heal(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Лечение должно быть числом")
    if amount < 0:
        raise ValueError("Лечение не может быть отрицательным")
    return float(amount)


def validate_experience_gain(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Опыт должен быть числом")
    if amount < 0:
        raise ValueError("Опыт не может быть отрицательным")
    return float(amount)