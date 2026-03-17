from model import Character

# Демонстрация создания и вывода
print("=== Создание персонажей ===")
hero = Character("Арагорн", level=5, health=150, experience=250)
print(hero)
print(repr(hero))

# Создание с параметрами по умолчанию
noob = Character("Новичок")
print(noob)

# Сравнение
hero2 = Character("Арагорн", level=5, health=150, experience=250)
print("hero == hero2:", hero == hero2)  # True (одинаковые имя и уровень)
hero3 = Character("Леголас", level=5)
print("hero == hero3:", hero == hero3)  # False

# Некорректное создание
print("\n=== Ошибки при создании ===")
try:
    Character("")  # пустое имя
except ValueError as e:
    print("Пустое имя:", e)

try:
    Character("Гимли", level=0)  # неверный уровень
except ValueError as e:
    print("Уровень 0:", e)

try:
    Character("Гэндальф", health=-10)  # отрицательное здоровье
except ValueError as e:
    print("Отрицательное здоровье:", e)

try:
    Character("Фродо", level=101)  # превышение MAX_LEVEL
except ValueError as e:
    print("Уровень > MAX:", e)

# Атрибут класса
print("\n=== Атрибут класса ===")
print("Character.MAX_LEVEL =", Character.MAX_LEVEL)
print("Character.BASE_HEALTH =", Character.BASE_HEALTH)
print("hero.MAX_LEVEL =", hero.MAX_LEVEL)

# Изменение имени через setter
print("\n=== Изменение имени ===")
print("Старое имя:", hero.name)
hero.name = "Арагорн, сын Араторна"
print("Новое имя:", hero.name)
try:
    hero.name = ""  # пустое
except ValueError as e:
    print("Попытка установить пустое имя:", e)

# Бизнес-методы
print("\n=== Бизнес-методы: урон, лечение, опыт ===")
fighter = Character("Боец", level=3, health=200, experience=150)
print(fighter)

# Получение урона
fighter.take_damage(50)
print("После урона 50:", fighter)

# Лечение
fighter.heal(30)
print("После лечения 30:", fighter)

# Получение опыта
fighter.gain_experience(80)
print("После +80 опыта:", fighter)

# Повышение уровня (должно сработать, если опыта достаточно)
# Установим опыт так, чтобы превысить порог
fighter.gain_experience(200)  # должно повысить уровень
print("После +200 опыта (повышение уровня):", fighter)

# Попытка лечить мертвого
print("\n=== Смерть и ограничения ===")
victim = Character("Жертва", level=1)
print(victim)
victim.take_damage(150)  # урон больше здоровья
print("После смертельного урона:", victim)
try:
    victim.heal(50)
except RuntimeError as e:
    print("Попытка лечить мертвого:", e)
try:
    victim.gain_experience(100)
except RuntimeError as e:
    print("Попытка дать опыт мертвому:", e)

# Атака между персонажами
print("\n=== Атака ===")
attacker = Character("Воин", level=10, health=500)
defender = Character("Моб", level=5, health=300)
print(attacker)
print(defender)
attacker.attack(defender)
print("После атаки защитник:", defender)

# Состояния и ограничения
print("\n=== Состояния ===")
print("Состояние атакующего:", attacker.state)
print("Состояние защитника:", defender.state)
if defender.state == "dead":
    print("Защитник мёртв!")

# Попытка атаковать мёртвого
try:
    attacker.attack(defender)  # мёртвый не может быть атакован? По логике можно, но take_damage у мертвого вызовет ошибку.
except RuntimeError as e:
    print("Атака мёртвого:", e)

# Демонстрация level_up отдельно
print("\n=== Повышение уровня вручную ===")
low_level = Character("Слабый", level=1, experience=50)
print(low_level)
low_level.gain_experience(200)  # должно повысить несколько раз
print("После опыта:", low_level)

# Проверка максимального уровня
print("\n=== Максимальный уровень ===")
max_char = Character("Макс", level=Character.MAX_LEVEL)
print(max_char)
try:
    max_char.level_up()
except RuntimeError as e:
    print("Попытка повысить уровень выше макс:", e)

# Сравнение через __eq__
print("\n=== Сравнение ===")
c1 = Character("Один", level=10)
c2 = Character("Один", level=10)
c3 = Character("Два", level=10)
print(f"c1 == c2: {c1 == c2}")
print(f"c1 == c3: {c1 == c3}")
print(f"c1 == 'строка': {c1 == 'строка'}")

# Дополнительно: проверка отрицательных значений в методах
print("\n=== Отрицательные значения в методах ===")
try:
    fighter.take_damage(-10)
except ValueError as e:
    print("Отрицательный урон:", e)
try:
    fighter.heal(-5)
except ValueError as e:
    print("Отрицательное лечение:", e)
try:
    fighter.gain_experience(-20)
except ValueError as e:
    print("Отрицательный опыт:", e)