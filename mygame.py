import random

class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.health = 100
        self.level = 1
        self.magic_points = 10
        self.inventory = []
        self.companion = None

    def display_stats(self):
        print("\n" + "=" * 50)
        print(f"Player Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Magic Points: {self.magic_points}")
        print("Inventory:")
        for item in self.inventory:
            print(f"- {item.name}")

    def attack_enemy(self, enemy):
        damage = random.randint(5, 10) * self.level
        enemy.health -= damage
        print(f"You attack the {enemy.name} for {damage} damage.")

    def use_magic(self, enemy):
        if self.magic_points >= 5:
            damage = random.randint(10, 15) * self.level
            enemy.health -= damage
            self.magic_points -= 5
            print(f"You cast a powerful spell on the {enemy.name} for {damage} damage.")
        else:
            print("Not enough magic points to cast a spell.")

    def heal(self):
        if self.magic_points >= 3:
            heal_amount = random.randint(10, 15) * self.level
            self.health += heal_amount
            self.magic_points -= 3
            print(f"You use a healing spell and restore {heal_amount} health.")
        else:
            print("Not enough magic points to cast a healing spell.")

    def add_item_to_inventory(self, item):
        self.inventory.append(item)


class Companion:
    def __init__(self, name, race, char_class, health, level):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.health = health
        self.level = level

    def attack_enemy(self, enemy):
        damage = random.randint(3, 6) * self.level
        enemy.health -= damage
        print(f"The {self.name} attacks the {enemy.name} for {damage} damage.")


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_enemy(self, enemy):
        damage = random.randint(3, 8)
        enemy.health -= damage
        print(f"The {self.name} attacks you for {damage} damage.")


class Room:
    def __init__(self, name, description, key=None, monster=None):
        self.name = name
        self.description = description
        self.key = key
        self.monster = monster

    def enter_room(self, player):
        print("\n" + "=" * 50)
        print(f"You enter the {self.name}. {self.description}")

        if self.monster:
            self.battle_monster(player)
        elif self.key:
            self.find_key(player)
        else:
            print("There is nothing of interest in this room.")

    def battle_monster(self, player):
        print(f"A wild {self.monster.name} appears!")

        while player.health > 0 and self.monster.health > 0:
            print("\n" + "=" * 50)
            player.display_stats()
            self.monster.display_stats()

            print("\nWhat will you do?")
            print("1. Attack")
            print("2. Use Magic")
            print("3. Heal")
            choice = input("Enter your choice: ")

            if choice == "1":
                player.attack_enemy(self.monster)
                if self.monster.health > 0:
                    self.monster.attack_enemy(player)
            elif choice == "2":
                player.use_magic(self.monster)
                if self.monster.health > 0:
                    self.monster.attack_enemy(player)
            elif choice == "3":
                player.heal()
                self.monster.attack_enemy(player)
            else:
                print("Invalid choice. Try again.")

        if player.health <= 0:
            print("Game Over. You have been defeated.")
            exit(0)
        else:
            print(f"You have defeated the {self.monster.name}!")

    def find_key(self, player):
        print(f"You found a {self.key} in the room.")
        player.add_item_to_inventory(Item(self.key, "A key to unlock a door."))


# Create player character
name = input("Enter your name: ")
race = input("Choose your race (Elf, Dwarf, Human): ")
char_class = input("Choose your class (Mage, Warrior, Rogue): ")
player = Character(name, race, char_class)

# Choose companion
print("\nChoose your companion:")
print("1. Elf Mage")
print("2. Dwarf Warrior")
print("3. Human Rogue")
companion_choice = input("Enter your choice: ")
if companion_choice == "1":
    player.companion = Companion("Elrond", "Elf", "Mage", 8, 3)
elif companion_choice == "2":
    player.companion = Companion("Gimli", "Dwarf", "Warrior", 10, 5)
elif companion_choice == "3":
    player.companion = Companion("Arya", "Human", "Rogue", 7, 4)
else:
    print("Invalid choice. No companion selected.")

# Define rooms and their contents
room1 = Room("Forest Room", "You find yourself in a dense forest with towering trees.",
             "Forest Key", Monster("Goblin", 20, 5, 2))
room2 = Room("Cave Room", "You enter a dark cave with dripping water and eerie echoes.",
             "Cave Key", Monster("Orc", 30, 8, 3))
room3 = Room("Castle Room", "You arrive at a grand castle. The entrance is guarded by fearsome knights.",
             "Castle Key", Monster("Knight", 50, 10, 5))
room4 = Room("Swamp Room", "You step into a murky swamp filled with a foul stench.",
             None, Monster("Swamp Creature", 40, 7, 4))
room5 = Room("Mysterious Room", "You enter a room shrouded in mystery. Ancient symbols cover the walls.",
             None, Monster("Sphinx", 60, 12, 6))
room6 = Room("Treasure Room", "You stumble upon a room filled with glittering treasure. The sight is mesmerizing.",
             None, None)

# Start the game
print(f"\nWelcome, {player.name}, to the RPG Adventure Game!")
room1.enter_room(player)

