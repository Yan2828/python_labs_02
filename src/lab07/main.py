# main.py
import os
from models import TypedCollection
from app import App
from cli import run_cli
import storage

DATA_FILE = "data.json"

def main():
    # Загрузка данных
    if os.path.exists(DATA_FILE):
        collection = storage.load(DATA_FILE)
        print(f"Загружено {len(collection)} героев.")
    else:
        collection = TypedCollection()
        print("Создана новая коллекция.")

    app = App(collection)

    try:
        run_cli(app)
    finally:
        # Сохранение при выходе
        storage.save(collection, DATA_FILE)
        print("Данные сохранены.")

if __name__ == "__main__":
    main()