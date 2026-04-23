# demo.py
from models import Voin, Mag, CharacterTeam
from interfaces import Printable, Comparable

def print_all(items):
    """Универсальная функция, работающая через интерфейс Printable"""
    for item in items:
        print(item.to_string())

print("=" * 60)
print("СЦЕНАРИЙ 1: Создание объектов и интерфейс Printable")
print("=" * 60)

v1 = Voin("Красавчик Ян", level=5, aura=50, motivazia=30)
v2 = Voin("Супер воин", level=3, aura=20, motivazia=10)
m1 = Mag("Жуков Никита", level=5, mana=100)
m2 = Mag("Мудрый маг", level=4, mana=80)

print("Вызов to_string() напрямую:")
print(v1.to_string())
print(m1.to_string())

print("\nУниверсальная функция print_all со списком объектов:")
print_all([v1, m1, v2, m2])

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 2: Проверка типов и сравнение через Comparable")
print("=" * 60)

print("Проверка isinstance:")
print(f"v1 - Printable: {isinstance(v1, Printable)}")
print(f"v1 - Comparable: {isinstance(v1, Comparable)}")
print(f"m1 - Printable: {isinstance(m1, Printable)}")
print(f"m1 - Comparable: {isinstance(m1, Comparable)}")

print("\nСравнение воинов по ауре:")
cmp = v1.compare(v2)
if cmp >=  0:
    print(f"{v1.name} сильнее {v2.name}(аура {v1.aura} >= {v2.aura})")
else:
    print(f"{v2.name} просто везет")

print("\nСравнение магов по мане:")
cmp = m1.compare(m2)
if cmp >= 0:
    print(f"{m1.name} имеет больше маны ({m1.mana} >= {m2.mana})")
else:
    print(f"{m2.name} имеет больше маны")

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 3: Интеграция с коллекцией – фильтрация по интерфейсу")
print("=" * 60)

team = CharacterTeam()
team.add(v1)
team.add(v2)
team.add(m1)
team.add(m2)

print("Все персонажи в коллекции:")
for c in team:
    print(f"  {c.name} ({type(c).__name__})")

print("\nТолько объекты, реализующие Printable:")
for c in team.get_printable():
    print(c.to_string())

print("\nТолько объекты, реализующие с:")
for c in team.get_comparable():
    print(f"  {c.name} (можно сравнивать)")

print("\n" + "=" * 60)
print("Демонстрация завершена. Все требования выполнены!")
print("=" * 60)