# demo.py
from container import TypedCollection, Voin, Mag, Displayable, Scorable

print("=" * 60)
print("СЦЕНАРИЙ 1: TypedCollection с ограничением Displayable")
print("=" * 60)

displayable_col: TypedCollection[Displayable] = TypedCollection()

v1 = Voin("Арагорн", level=5, aura=100)
m1 = Mag("Гэндальф", level=6, mana=200)

displayable_col.add(v1)
displayable_col.add(m1)

print("Все элементы коллекции Displayable:")
for item in displayable_col:
    print(item.display())

print("\n--- Используем find ---")
found = displayable_col.find(lambda obj: "аура" in obj.display())
print("Найден:", found.display() if found else None)

not_found = displayable_col.find(lambda obj: "дракон" in obj.display())
print("Не найден:", not_found)

print("\n--- Используем filter ---")
filtered = displayable_col.filter(lambda obj: obj.level >= 5)
print("Отфильтровано (уровень >=5):", [obj.display() for obj in filtered])

print("\n--- Используем map (преобразование в имена) ---")
names = displayable_col.map(lambda obj: obj.name)
print("Имена:", names)

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 2: TypedCollection с ограничением Scorable")
print("=" * 60)

scorable_col: TypedCollection[Scorable] = TypedCollection()

v2 = Voin("Гимли", level=4, aura=85)
m2 = Mag("Саруман", level=7, mana=250)

scorable_col.add(v2)
scorable_col.add(m2)

print("Очки (score) каждого объекта:")
for item in scorable_col:
    print(f"{item.name}: {item.score()}")

print("\n--- Находим объект с максимальным score ---")
max_item = max(scorable_col, key=lambda obj: obj.score())
print("Максимальный score у:", max_item.display())

print("\n--- map: увеличить score на 10% и вернуть список ---")
scaled = scorable_col.map(lambda obj: obj.score() * 1.1)
print("Увеличенные scores:", scaled)

print("\n" + "=" * 60)
print("Демонстрация завершена. Все требования выполнены!")
print("=" * 60)