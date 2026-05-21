# exceptions.py
class HeroNotFoundError(Exception):
    """Герой не найден в коллекции."""
    pass

class DuplicateHeroError(Exception):
    """Герой с таким именем уже существует."""
    pass

class InvalidInputError(Exception):
    """Некорректный ввод данных."""
    pass