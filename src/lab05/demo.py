# demo.py
from collection import Voin, Mag, CharacterTeam
import strategies as st

print("=" * 60)
print("СЦЕНАРИЙ 1: Сортировка разными стратегиями и фильтрация")
print("=" * 60)

team = CharacterTeam()
team.add(Voin("Zogg", level=5, aura=100))
team.add(Voin("Arthas", level=8, aura=150))
team.add(Voin("Grom", level=3, aura=80))
team.add(Mag("Gandalf", level=6, mana=200))
team.add(Mag("Saruman", level=4, mana=120))
team.add(Mag("Medivh", level=7, mana=180))

print("Исходная коллекция:")
for c in team:
    print(f"  {c}")

team.sort_by(st.by_name)
print("\nСортировка по имени (by_name):")
for c in team:
    print(f"  {c.name} ({type(c).__name__})")

sort_by_level = st.make_sort_by_attr("level")
team.sort_by(sort_by_level)
print("\nСортировка по уровню (make_sort_by_attr):")
for c in team:
    print(f"  {c.name} - уровень {c.level}")

team.sort_by(st.by_aura, reverse=True)
print("\nСортировка по ауре (by_aura, убывание):")
for c in team:
    aura = c.aura if hasattr(c, 'aura') else 0
    print(f"  {c.name} - аура {aura}")

warriors_team = team.filter_by(st.is_warrior)
print(f"\nФильтр is_warrior: {len(warriors_team)} воинов")

high_level_filter = st.make_min_level_filter(5)
high_team = team.filter_by(high_level_filter)
print(f"Фильтр уровень >=5: {len(high_team)} персонажей")

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 2: Использование map, фабрик и lambda")
print("=" * 60)

names = team.map_to(st.to_name)
print("Список имён (map):", names)

level_name = team.map_to(lambda obj: f"{obj.level}: {obj.name}")
print("Уровень и имя:", level_name)

filter_lvl4 = st.make_min_level_filter(4)
filtered_lvl4 = team.filter_by(filter_lvl4)
print(f"\nФильтр уровень >=4 (через фабрику): {len(filtered_lvl4)} персонажей")

healthy_filter = lambda obj: obj.health > 100
healthy_team = team.filter_by(healthy_filter)
print(f"λ-фильтр (здоровье >100): {len(healthy_team)} персонажей")

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 3: Цепочка операций и callable-стратегии")
print("=" * 60)

team2 = CharacterTeam()
team2.add(Voin("Eragon", level=3, aura=50))
team2.add(Voin("Murtagh", level=5, aura=90))
team2.add(Mag("Saphira", level=4, mana=150))
team2.add(Mag("Oromis", level=6, mana=220))

print("Исходная коллекция:")
for c in team2:
    print(f"  {c}")

sort_by_aura_callable = st.SortByAttribute("aura")
filter_warriors = st.FilterByType(Voin)
add_exp_50 = st.AddExperienceStrategy(50)

result_team = (team2
    .filter_by(filter_warriors)
    .sort_by(sort_by_aura_callable, reverse=True)
    .apply(add_exp_50)
)

print("\nПосле цепочки (фильтр воины -> сортировка по ауре -> +50 опыта):")
for c in result_team:
    print(f"  {c.name}: уровень {c.level}, опыт {c.experience:.0f}, аура {c.aura}")

team2.apply(st.HealStrategy())
print("\nПрименяем HealStrategy к исходной коллекции:")
for c in team2:
    print(f"  {c.name}: здоровье {c.health:.1f}/{c.max_health:.1f}")

