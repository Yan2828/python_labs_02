# storage.py
import json
from typing import List
from models import Voin, Mag, Character, TypedCollection

def save(collection: TypedCollection, filepath: str) -> None:
    """Сохраняет коллекцию в JSON-файл."""
    data = []
    for item in collection.get_all():
        if isinstance(item, (Voin, Mag)):
            data.append(item.to_dict())
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load(filepath: str) -> TypedCollection:
    """Загружает коллекцию из JSON-файла. Если файла нет, возвращает пустую коллекцию."""
    collection = TypedCollection()
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return collection
    for item_data in data:
        cls_name = item_data.get("type")
        if cls_name == "Voin":
            obj = Voin.from_dict(item_data)
        elif cls_name == "Mag":
            obj = Mag.from_dict(item_data)
        else:
            continue
        collection.add(obj)
    return collection