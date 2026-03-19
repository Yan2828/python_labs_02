from model import Character

print("==========================================")
print("= СЦЕНАРИЙ 1: Создание персонажей")
print("==========================================")

# Создание с полными параметрами
hero = Character("Арагорн", level=5, health=150, experience=250)
print(hero)
print(repr(hero))

# Создание с параметрами по умолчанию
noob = Character("Новичок")
print(noob)

# Каждый персонаж получает свои характеристики
print("\n--- Разные способы создания ---")
hero2 = Character("Арагорн", level=5, health=150, experience=250)
hero3 = Character("Леголас", level=3, health=120, experience=80)
print(f"hero2: {hero2}")
print(f"hero3: {hero3}")

print("\n==========================================")
print("= СЦЕНАРИЙ 2: Валидация (обработка ошибок)")
print("==========================================")

print("--- Некорректные имена ---")
try:
    Character("")
except ValueError as e:
    print("Пустое имя:", e)

print("\n--- Некорректный уровень ---")
try:
    Character("Гимли", level=0)
except ValueError as e:
    print("Уровень 0:", e)
try:
    Character("Гимли", level=101)
except ValueError as e:
    print("Уровень 101:", e)

print("\n--- Некорректное здоровье ---")
try:
    Character("Фродо", level=1, health=-50)
except ValueError as e:
    print("Отрицательное здоровье:", e)
try:
    Character("Фродо", level=1, health=1000)
except ValueError as e:
    print("Здоровье больше максимума:", e)

print("\n==========================================")
print("= СЦЕНАРИЙ 3: Свойства (геттеры/сеттеры)")
print("==========================================")

print("--- Чтение свойств ---")
print(f"Имя: {hero.name}")
print(f"Уровень: {hero.level}")
print(f"Здоровье: {hero.health}/{hero.max_health}")
print(f"Опыт: {hero.experience}")
print(f"Статус: {hero.state}")

print("\n--- Изменение имени ---")
print(f"Старое имя: {hero.name}")
hero.name = "Арагорн, сын Араторна"
print(f"Новое имя: {hero.name}")
try:
    hero.name = ""
except ValueError as e:
    print("Попытка установить пустое имя:", e)

print("\n--- Попытка изменить уровень напрямую (ошибка) ---")
try:
    hero.level = 10
except AttributeError as e:
    print("Нельзя изменить уровень напрямую:", e)

print("\n==========================================")
print("= СЦЕНАРИЙ 4: Атрибуты класса")
print("==========================================")

print(f"Character.MAX_LEVEL = {Character.MAX_LEVEL}")
print(f"Character.BASE_HEALTH = {Character.BASE_HEALTH}")
print(f"Character.HEALTH_PER_LEVEL = {Character.HEALTH_PER_LEVEL}")
print(f"hero.MAX_LEVEL = {hero.MAX_LEVEL} (доступ через экземпляр)")

print("\n==========================================")
print("= СЦЕНАРИЙ 5: Боевые механики")
print("==========================================")

fighter = Character("Боец", level=3, health=130, experience=150)
print("Начальное состояние:")
print(fighter)

print("\n--- Получение урона ---")
fighter.take_damage(50)
print("После урона 50:", fighter)

print("\n--- Лечение ---")
fighter.heal(30)
print("После лечения 30:", fighter)

print("\n--- Получение опыта ---")
fighter.gain_experience(80)
print("После +80 опыта:", fighter)

print("\n--- Повышение уровня ---")
fighter.gain_experience(200)
print("После +200 опыта:", fighter)

print("\n==========================================")
print("= СЦЕНАРИЙ 6: Смерть и ограничения")
print("==========================================")

victim = Character("Жертва", level=1)
print("Начальное состояние:")
print(victim)

print("\n--- Смертельный урон ---")
victim.take_damage(150)
print("После урона 150:", victim)

print("\n--- Попытка действий с мёртвым персонажем ---")
try:
    victim.heal(50)
except RuntimeError as e:
    print("Попытка лечить:", e)
try:
    victim.gain_experience(100)
except RuntimeError as e:
    print("Попытка дать опыт:", e)

print("\n==========================================")
print("= СЦЕНАРИЙ 7: Атака между персонажами")
print("==========================================")

attacker = Character("Воин", level=10, health=200, experience=950)
defender = Character("Моб", level=5, health=150, experience=0)

print("Атакующий:")
print(attacker)
print("\nЗащитник:")
print(defender)

print("\n--- Атака ---")
attacker.attack(defender)
print("После атаки защитник:", defender)

if defender.state == "dead":
    print("Защитник мёртв!")

print("\n--- Попытка атаковать мёртвого ---")
try:
    attacker.attack(defender)
except RuntimeError as e:
    print("Результат:", e)

print("\n==========================================")
print("= СЦЕНАРИЙ 8: Повышение уровня и максимальный уровень")
print("==========================================")

low_level = Character("Слабый", level=1, health=100, experience=50)
print("Начальное состояние:")
print(low_level)

print("\n--- Получение опыта (несколько повышений) ---")
low_level.gain_experience(250)
print("После опыта:", low_level)

print("\n--- Попытка повысить уровень выше максимального ---")
max_char = Character("Макс", level=Character.MAX_LEVEL, 
                     health=Character.BASE_HEALTH + (Character.MAX_LEVEL - 1) * Character.HEALTH_PER_LEVEL)
print(max_char)
try:
    max_char.level_up()
except RuntimeError as e:
    print("Попытка level_up:", e)

print("\n==========================================")
print("= СЦЕНАРИЙ 9: Магические методы")
print("==========================================")

print("--- __str__ (пользовательский вывод) ---")
test_char = Character("Тест", level=7, health=120, experience=350)
print(test_char)

print("\n--- __repr__ (отладочный вывод) ---")
print(repr(test_char))

print("\n--- __eq__ (сравнение персонажей) ---")
c1 = Character("Один", level=10, health=190, experience=500)
c2 = Character("Один", level=10, health=190, experience=500)
c3 = Character("Два", level=10, health=190, experience=500)

print(f"c1 == c2: {c1 == c2} (True - одинаковые имя и уровень)")
print(f"c1 == c3: {c1 == c3} (False - разные имена)")
print(f"c1 == 'строка': {c1 == 'строка'} (False - разные типы)")

print("\n==========================================")
print("= СЦЕНАРИЙ 10: Проверка некорректных операций")
print("==========================================")

valid_char = Character("Валидный", level=5, health=140, experience=200)
print("Рабочий персонаж:")
print(valid_char)

print("\n--- Отрицательные значения в методах ---")
try:
    valid_char.take_damage(-10)
except ValueError as e:
    print("Отрицательный урон:", e)

try:
    valid_char.heal(-5)
except ValueError as e:
    print("Отрицательное лечение:", e)

try:
    valid_char.gain_experience(-20)
except ValueError as e:
    print("Отрицательный опыт:", e)

print("\n==========================================")