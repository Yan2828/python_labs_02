from base import Character


class Voin(Character):
    
    def __init__(self, name, level=1, health=None, experience=0, aura=0, motivazia=0):
        super().__init__(name, level, health, experience)

        self.aura = aura
        self.motivazia = motivazia

    def kill_mag(self, target_mag):
        
        self.aura += 1000
        self.motivazia += 1000
        
        damage = 9999
        target_mag.take_damage(damage)
    
        
        return f'Кто ты воин? {self.name} безжаластно убил {target_mag.name}. Аура: {self.aura}. Мотивация: {self.motivazia}'

    def attack_mag(self, target_mag):
        
        self._check_alive("атака")
        
        if not isinstance(target_mag, Character):
            raise TypeError("Цель должна быть персонажем")
        
        damage = self._level * 10 + (self.aura // 100)  
        target_mag.take_damage(damage)
        
        self.aura += 100
        return f'Воин атакует {target_mag.name} и наносит {damage} урона! А ты хорош, но недостаточно. Аура: {self.aura}. Мотивация: {self.motivazia}'
    
    def make_sound(self):
        return f"{self.name}: Кто последний, тот отчислен!"
    
    
    def __str__(self):
        return (f"Аура: {self.aura}, мотивация: {self.motivazia}")
    
    def use_skill(self, target_mag):
        return self.kill_mag(target_mag)


class Mag(Character):
    
    def __init__(self, name, level=1, health=None, experience=0, mana=50, sleep=0):
        
        super().__init__(name, level, health, experience)
        
        self.mana = mana
        self.sleep = sleep
    
    def kill_voin(self, target_voin):
        
        damage = 9999
        target_voin.take_damage(damage)

        self.mana += 100
        self.sleep += 10
        
        return f'Это было легко. {self.name} безжаластно убил {target_voin.name}. Мана: {self.mana}. Скучно, хочу спать: {self.sleep}'

    def attack_voin(self, target_voin):
        
        self._check_alive("атака")
        
        if not isinstance(target_voin, Character):
            raise TypeError("Цель должна быть персонажем")
        
        if self.mana < 10:
            raise ValueError(f"Не будь лузером, пополни ману!")
        
        damage = self._level * 12  
        
        self.mana -= 10
        self.sleep += 5
        
        target_voin.take_damage(damage)
        return f" Маг атакует {target_voin.name} и наносит {damage} урона! А ведь я хотел тебя убить. Мана: {self.mana}ю Скучно, хочу спать: {self.sleep}"
    
    def make_sound(self):
        return f"{self.name}: Кто первый, тот красавчик!"
    
    
    def __str__(self):
        return (f" мана: {self.mana}, усталость: {self.sleep}")

    def use_skill(self, target_voin):
        return self.kill_voin(target_voin)
    
    


