# Лабораторная работа №1: Игровая логика — класс Character (Вариант 6) 🎮⚔️
![photo](https://private-user-images.githubusercontent.com/74038190/238200437-de038172-e903-4951-926c-755878deb0b4.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzM3NzU1NjAsIm5iZiI6MTc3Mzc3NTI2MCwicGF0aCI6Ii83NDAzODE5MC8yMzgyMDA0MzctZGUwMzgxNzItZTkwMy00OTUxLTkyNmMtNzU1ODc4ZGViMGI0LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAzMTclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMzE3VDE5MjEwMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFhMjNhYWI0MjNiMzU5MmNmY2YwYjg1M2Q0OGRkNDA3YTNhNTZmYzMyNzc2MjRjNTA5NTBiMGE3ZTRiYzA0MTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.DINjopjl4RNhw8_Cu-oEVQkvtsiWxFBLav4HwlKTknY)
## Цель работы
•	Освоить объявление пользовательских классов
•	Реализовать инкапсуляцию (закрытые поля)
•	Научиться использовать свойства (@property) с валидацией
•	Переопределить магические методы (__str__, __repr__, __eq__)
•	Понять разницу между атрибутами класса и экземпляра
•	Создать объект с логическим состоянием и поведением, зависящим от него
Идея
## Создать модель игрового персонажа (Character), который:
•	Следит за корректностью своих характеристик (имя, уровень, здоровье, опыт)
•	Имеет состояние (alive / dead), влияющее на доступные действия
•	Поддерживает основные RPG-механики: получение урона, лечение, набор опыта, повышение уровня, атаку других персонажей
________________________________________
## Реализованный класс
**Character** — ***основной класс, моделирующий игрового персонажа.
Атрибуты класса***
•	MAX_LEVEL = 100 — максимально достижимый уровень
•	BASE_HEALTH = 100 — базовое здоровье на 1 уровне
•	HEALTH_PER_LEVEL = 10 — прирост максимального здоровья за уровень
Закрытые поля экземпляра
•	_name — имя персонажа
•	_level — уровень (1..MAX_LEVEL)
•	_health — текущее здоровье (0..max_health)
•	_experience — накопленный опыт
•	_state — состояние: "alive" или "dead"
**Свойства** (`@property`)
name
•	Геттер: возвращает имя
•	Сеттер: проверяет, что новое имя — непустая строка, иначе ValueError
level (только чтение)
•	Возвращает текущий уровень (изменяется только через метод level_up)
health (только чтение)
•	Возвращает текущее здоровье (изменяется методами take_damage и heal)
experience (только чтение)
•	Возвращает накопленный опыт (изменяется через gain_experience)
state (только чтение)
•	Возвращает состояние ("alive" / "dead")
max_health (вычисляемое, только чтение)
•	Возвращает максимальное здоровье в зависимости от уровня:
BASE_HEALTH + (level - 1) * HEALTH_PER_LEVEL
**Магические методы**
•	__str__ — читаемое описание персонажа (для print)
•	__repr__ — представление для разработчиков (как создать объект)
•	__eq__ — сравнение персонажей по имени и уровню (можно дополнить уникальным ID)
**Бизнес-методы**
•	take_damage(amount) — уменьшает здоровье; если здоровье ≤ 0, состояние меняется на "dead".
•	heal(amount) — восстанавливает здоровье, но не выше максимума.
•	gain_experience(amount) — добавляет опыт; при достижении порога (100 × текущий уровень) автоматически повышает уровень.
•	level_up() — увеличивает уровень на 1, восстанавливает здоровье до максимума.
•	attack(target) — атакует другого персонажа, нанося урон = уровень × 10 (демонстрация взаимодействия объектов).
Все методы, изменяющие состояние, проверяют, жив ли персонаж (если нет — выбрасывают RuntimeError). Также проверяются корректность входных данных (тип, диапазон).git 