from model import Character


class CharacterTeam:

    def __init__(self):
        self._items = []          
        
    def add(self, character):
        
        if not isinstance(character, Character):
            raise TypeError("Можно добавлять только объекты Character")

        if self.find_by_name(character.name) is not None:
            raise ValueError("Такое имя уже есть, дружище")
        self._items.append(character)

    def remove(self, character):

        if character not in self._items:
            raise ValueError("Такого актера нет в коллекции")
        self._items.remove(character)

    def get_all(self):
        return self._items.copy()

    def find_by_name(self, name):
        
        for c in self._items:
            if c.name == name:
                return c
        return None

    def find_by_level(self, level):
        result = []
        for c in self._items:
            if c.level == level:
                result.append(c)
        return result

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        
        if isinstance(index, slice):
            return self._items[index]  
            
        if  0 > index or index >= len(self._items):
            raise IndexError("Не попал, ищи диапозон")
        
        return self._items[index]

    def remove_at(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Не попал, ищи диапозон")
        del self._items[index]

    def sort_by_level(self, reverse=False):
        self._items.sort(key=lambda c: c.level, reverse=reverse)

    def sort_by_name(self, reverse=False):
        self._items.sort(key=lambda c: c.name, reverse=reverse)

    def sort(self, key, reverse=False):
        self._items.sort(key=key, reverse=reverse)

    def get_alive(self):
        new_team = CharacterTeam()
        for c in self._items:
            if c.state == "alive":
                new_team.add(c)
        return new_team

    def get_by_min_level(self, min_level):
        new_team = CharacterTeam()
        for c in self._items:
            if c.level >= min_level:
                new_team.add(c)
        return new_team

 
 


