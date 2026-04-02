
from model import Character
from collection import CharacterTeam


print("=" * 60)
print("СЦЕНАРИЙ 1: Создание коллекции, добавление, удаление, вывод")
print("=" * 60)

aragorn = Character("Арагорн", level=5, health=150, experience=250)
legolas = Character("Леголас", level=4, health=120, experience=180)
gimli = Character("Гимли", level=4, health=140, experience=160)
gandalf = Character("Гэндальф", level=10, health=200, experience=500)

team = CharacterTeam()

team.add(aragorn)
team.add(legolas)
team.add(gimli)
team.add(gandalf)

print("Все персонажи в команде:")
for char in team:
    print(f"  {char.name} (ур.{char.level})")

team.remove(gimli)
print("\nПосле удаления Гимли:")
for char in team:
    print(char.name)

print("\nПопытка добавить дубликат (Арагорн):")
try:
    team.add(Character("Арагорн", level=5))
except ValueError as e:
    print(f"  Ошибка: {e}")

print("\nПопытка добавить строку вместо персонажа:")
try:
    team.add("Не персонаж")
except TypeError as e:
    print(f"  Ошибка: {e}")

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 2: Поиск, длина, итерация")
print("=" * 60)

found = team.find_by_name("Леголас")
print(f"Поиск по имени 'Леголас': {found}")

level4 = team.find_by_level(4)
print(f"Персонажи уровня 4: {[c.name for c in level4]}")

print(f"Количество персонажей в команде: {len(team)}")

print("Перебор через for:")
for char in team:
    print(char.name)

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 3: Индексация и удаление по индексу")
print("=" * 60)

print("Первый персонаж (индекс 0):", team[0].name)
print("Второй персонаж (индекс 1):", team[1].name)

print("\nСрез [1:3]:")
for char in team[1:3]:
    print(f"  {char.name}")

team.remove_at(1)   
print("\nПосле удаления элемента с индексом 1:")
for char in team:
    print(f"  {char.name}")

try:
    team[10]
except IndexError as e:
    print(f"\nОшибка при обращении по индексу 10: {e}")

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 4: Сортировка")
print("=" * 60)

team2 = CharacterTeam()
team2.add(aragorn)
team2.add(legolas)
team2.add(gimli)
team2.add(gandalf)

print("До сортировки по уровню (по возрастанию):")
for char in team2:
    print(f"  {char.name} (ур.{char.level})")

team2.sort_by_level()
print("\nПосле сортировки по уровню (по возрастанию):")
for char in team2:
    print(f"  {char.name} (ур.{char.level})")

team2.sort_by_name(reverse=True)
print("\nПосле сортировки по имени (по убыванию):")
for char in team2:
    print(f"  {char.name}")

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 5: Фильтрация (логические операции)")
print("=" * 60)

gimli.take_damage(200)   

alive_team = team2.get_alive()
print("Живые персонажи:")
for char in alive_team:
    print(f"  {char.name} (здоровье {char.health})")

high_level_team = team2.get_by_min_level(5)
print("\nПерсонажи с уровнем >= 5:")
for char in high_level_team:
    print(f"  {char.name} (ур.{char.level})")

print("\n" + "=" * 60)
print("Все демонстрации успешно выполнены!")
print("=" * 60)