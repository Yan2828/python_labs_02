from base import Character
from models import Voin, Mag


print("=" * 60)
print("СЦЕНАРИЙ 1: Создание персонажей и вывод информации")
print("=" * 60)

voin = Voin("Красавчик Ян", level=5, health=150, aura=50, motivazia=30)
mag = Mag("Жуков Никита", level=5, health=150, mana=100, sleep=0)

print("Создан воин:")
print(voin)
print("\nСоздан маг:")
print(mag)

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 2: Полиморфизм ")
print("=" * 60)

print(voin.make_sound())
print(mag.make_sound())

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 3: Атаки")
print("=" * 60)

print(f"\nЗдоровье мага до атаки воина: {mag.health}")
print(voin.attack_mag(mag))
print(f"Здоровье мага после атаки: {mag.health}")

print(f"\nЗдоровье воина до атаки мага: {voin.health}")
print(mag.attack_voin(voin))
print(f"Здоровье воина после атаки: {voin.health}")

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 4: Убийства")
print("=" * 60)

mag2 = Mag("Самурай", level=5, health=100, mana=80, sleep=0)
voin2 = Voin("Не красавчик", level=4, health=100, aura=30, motivazia=20)

print(f"\nЗдоровье {mag2.name} до убийства: {mag2.health}")
print(voin.kill_mag(mag2))
print(f"Здоровье {mag2.name} после убийства: {mag2.health}")
print(f"Состояние {mag2.name}: {mag2.state}")

print(f"\nЗдоровье {voin2.name} до убийства: {voin2.health}")
print(mag.kill_voin(voin2))
print(f"Здоровье {voin2.name} после убийства: {voin2.health}")
print(f"Состояние {voin2.name}: {voin2.state}")

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 5: Полиморфизм use_skill и проверка типов")
print("=" * 60)

temp_mag = Mag("маг", level=1, health=100, mana=50)
temp_voin = Voin("воин", level=1, health=100)

print("Воин использует skill на маге:")
print(voin.use_skill(temp_mag))

print("\nМаг использует skill на воине:")
print(mag.use_skill(temp_voin))
