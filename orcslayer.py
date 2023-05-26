import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_target(self, target):
        damage = self.calculate_damage(target)
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage.")

    def calculate_damage(self, target):
        base_damage = random.randint(1, self.attack)
        defense_reduction = random.randint(1, target.defense)
        total_damage = base_damage - defense_reduction
        if total_damage < 0:
            total_damage = 0
        return total_damage

class Room:
    def __init__(self, name, description, key, monster=None):
        self.name = name
        self.description = description
        self.key = key
        self.monster = monster
        self.is_visited = False

    def enter_room(self, player):
        if self.is_visited:
            print(f"You have already visited {self.name}.")
        else:
            print(f"You have entered {self.name}. {self.description}")
            self.is_visited = True
            if self.monster:
                self.battle_monster(player)
            if self.key:
                self.find_key(player)

    def battle_monster(self, player):
        print(f"A wild {self.monster.name} appears!")
        while player.is_alive() and self.monster.is_alive():
            player.attack_target(self.monster)
            if not self.monster.is_alive():
                print(f"You have defeated the {self.monster.name}!")
                break
            self.monster.attack_target(player)
            if not player.is_alive():
                print("You have been defeated!")
                break

    def find_key(self, player):
        print(f"You found a key in {self.name}!")
        player.keys.append(self.key)
        self.key = None

class RPGGame:
    def __init__(self, player, rooms):
        self.player = player
        self.rooms = rooms

    def run(self):
        print("RPG Game Starts!")
        current_room_index = 0
        while self.player.is_alive() and current_room_index < len(self.rooms):
            current_room = self.rooms[current_room_index]
            current_room.enter_room(self.player)

            if current_room.key is None or current_room.key in self.player.keys:
                current_room_index += 1
            else:
                print(f"You need a key to move to the next room.")

            if current_room_index < len(self.rooms):
                input("Press Enter to continue to the next room...")
                print()

        if self.player.is_alive():
            print("Congratulations! You have completed the game!")
        else:
            print("Game over!")

# Create player character
player = Character("Player", 100, 20, 10)
player.keys = []

# Create monsters
monster1 = Character("Goblin", 50, 10, 5)
monster2 = Character("Orc", 80, 15, 8)
monster3 = Character("Dragon", 150, 25, 15)

# Create rooms
room1 = Room("Room 1", "This is the first room.", "Key 1", monster1)
room

