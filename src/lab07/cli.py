# cli.py
from models import Voin, Mag
from typing import Optional
from app import App
from exceptions import HeroNotFoundError, DuplicateHeroError, InvalidInputError

def confirm(prompt: str) -> bool:
    """Запрашивает подтверждение y/n."""
    ans = input(prompt + " (y/n): ").strip().lower()
    return ans == 'y'

def print_heroes(heroes):
    """Выводит список героев в табличном виде."""
    if not heroes:
        print("Нет героев.")
        return
    print("\n" + "-" * 70)
    print(f"{'Имя':<15} {'Тип':<10} {'Уровень':<8} {'Здоровье':<10} {'Доп. параметр'}")
    print("-" * 70)
    for h in heroes:
        if hasattr(h, 'aura'):
            extra = f"аура {h.aura}"
        elif hasattr(h, 'mana'):
            extra = f"мана {h.mana}"
        else:
            extra = ""
        print(f"{h.name:<15} {type(h).__name__:<10} {h.level:<8} {h.health:.0f}/{h.max_health:.0f} {extra}")
    print("-" * 70)

def run_cli(app: App) -> None:
    """Главный цикл CLI."""
    while True:
        print("\n" + "=" * 50)
        print("ГЛАВНОЕ МЕНЮ")
        print("1. Добавить героя")
        print("2. Показать всех героев")
        print("3. Найти героя по имени")
        print("4. Удалить героя")
        print("5. Фильтрация (только воины / только маги / живые)")
        print("6. Сортировка")
        print("7. Статистика")
        print("0. Выход")
        choice = input("Ваш выбор: ").strip()

        if choice == "0":
            print("До свидания!")
            break

        elif choice == "1":
            # Добавление героя
            hero_type = input("Тип героя (voin/mag): ").strip().lower()
            if hero_type not in ("voin", "mag"):
                print("Неверный тип.")
                continue
            name = input("Имя: ").strip()
            if not name:
                print("Имя не может быть пустым.")
                continue
            try:
                level = int(input("Уровень (1-100): "))
            except ValueError:
                print("Ошибка: введите число.")
                continue
            try:
                if hero_type == "voin":
                    aura = int(input("Аура: "))
                    app.add_hero("voin", name, level, aura=aura)
                else:
                    mana = int(input("Мана: "))
                    app.add_hero("mag", name, level, mana=mana)
                print(f"Герой '{name}' добавлен.")
            except DuplicateHeroError as e:
                print(f"Ошибка: {e}")
            except (ValueError, InvalidInputError) as e:
                print(f"Ошибка ввода: {e}")

        elif choice == "2":
            heroes = app.get_all_heroes()
            print_heroes(heroes)

        elif choice == "3":
            name = input("Введите имя героя: ").strip()
            hero = app.find_hero(name)
            if hero:
                print_heroes([hero])
            else:
                print("Герой не найден.")

        elif choice == "4":
            name = input("Имя героя для удаления: ").strip()
            if confirm(f"Удалить героя '{name}'?"):
                try:
                    app.remove_hero(name)
                    print("Герой удалён.")
                except HeroNotFoundError as e:
                    print(f"Ошибка: {e}")

        elif choice == "5":
            print("Фильтрация:")
            print("1. Только воины")
            print("2. Только маги")
            print("3. Только живые")
            sub = input("Ваш выбор: ").strip()
            if sub == "1":
                filtered = app.filter_heroes(lambda h: isinstance(h, Voin))
            elif sub == "2":
                filtered = app.filter_heroes(lambda h: isinstance(h, Mag))
            elif sub == "3":
                filtered = app.filter_heroes(lambda h: h.state == "alive")
            else:
                print("Неверный пункт.")
                continue
            print_heroes(filtered)

        elif choice == "6":
            print("Сортировка по:")
            print("1. Имени")
            print("2. Уровню")
            print("3. Ауре (только воины)")
            print("4. Мане (только маги)")
            sub = input("Ваш выбор: ").strip()
            key_map = {"1": "name", "2": "level", "3": "aura", "4": "mana"}
            if sub not in key_map:
                print("Неверный пункт.")
                continue
            reverse = input("По убыванию? (y/n): ").strip().lower() == 'y'
            try:
                app.sort_heroes(key_map[sub], reverse)
                print("Сортировка выполнена.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "7":
            stats = app.get_stats()
            print(f"Всего героев: {len(app.get_all_heroes())}")
            print(f"Воинов: {stats['warriors']}, Магов: {stats['mages']}")
        else:
            print("Неверный пункт меню. Попробуйте снова.")