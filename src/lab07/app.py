# app.py
from typing import Optional, List, Callable
from models import TypedCollection, Voin, Mag, Character
from exceptions import HeroNotFoundError, DuplicateHeroError, InvalidInputError

class App:
    """Основной класс приложения, управляет коллекцией и бизнес-логикой."""

    def __init__(self, collection: TypedCollection) -> None:
        self.collection = collection

    def add_hero(self, hero_type: str, name: str, level: int, aura: int = 0, mana: int = 0) -> None:
        """Добавляет героя. Проверяет дубликаты по имени."""
        if self.collection.find_by_name(name) is not None:
            raise DuplicateHeroError(f"Герой с именем '{name}' уже существует.")
        if hero_type == "voin":
            hero = Voin(name, level, aura=aura)
        elif hero_type == "mag":
            hero = Mag(name, level, mana=mana)
        else:
            raise InvalidInputError("Неверный тип героя.")
        self.collection.add(hero)

    def remove_hero(self, name: str) -> None:
        """Удаляет героя по имени. Генерирует HeroNotFoundError, если не найден."""
        hero = self.collection.find_by_name(name)
        if hero is None:
            raise HeroNotFoundError(f"Герой '{name}' не найден.")
        self.collection.remove(hero)

    def get_all_heroes(self) -> List[Character]:
        return self.collection.get_all()

    def find_hero(self, name: str) -> Optional[Character]:
        return self.collection.find_by_name(name)

    def filter_heroes(self, predicate: Callable[[Character], bool]) -> List[Character]:
        """Фильтрация коллекции по произвольному условию."""
        return self.collection.filter(predicate)

    def sort_heroes(self, key: str, reverse: bool = False) -> None:
        """Сортирует коллекцию на месте по заданному ключу."""
        if key == "name":
            self.collection._items.sort(key=lambda h: h.name, reverse=reverse)
        elif key == "level":
            self.collection._items.sort(key=lambda h: h.level, reverse=reverse)
        elif key == "aura":
            # только для воинов (у магов аура = 0)
            self.collection._items.sort(key=lambda h: getattr(h, 'aura', 0), reverse=reverse)
        elif key == "mana":
            self.collection._items.sort(key=lambda h: getattr(h, 'mana', 0), reverse=reverse)
        else:
            raise ValueError("Неизвестный ключ сортировки")

    def get_stats(self) -> dict:
        """Возвращает статистику: количество воинов и магов."""
        warriors = sum(1 for h in self.collection.get_all() if isinstance(h, Voin))
        mages = sum(1 for h in self.collection.get_all() if isinstance(h, Mag))
        return {"warriors": warriors, "mages": mages}