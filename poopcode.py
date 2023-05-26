import pygame
import random


# Define constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Game")

clock = pygame.time.Clock()


class Character:
    def __init__(self, name, race, player_class, health, attack, defense):
        self.name = name
        self.race = race
        self.player_class = player_class
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} uses a healing potion and recovers {heal_amount} health.")

    def attack_target(self, target):
        damage = self.calculate_damage(target)
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage.")

    def use_spell(self, target):
        print(f"{self.name} casts a spell on {target.name}!")
        spell_damage = random.randint(10, 20)
        target.take_damage(spell_damage)
        print(f"The spell deals {spell_damage} damage to {target.name}.")

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
            print(f"You have entered {self.name}.")
            print(self.get_room_visual())
            print(self.description)
            self.is_visited = True
            if self.monster:
                self.battle_monster(player)
            if self.key:
                self.find_key(player)
            self.make_choice(player)

    def battle_monster(self, player):
        print(f"A wild {self.monster.name} appears!")
        while player.is_alive() and self.monster.is_alive():
            self.print_player_status(player)
            self.print_monster_status(self.monster)

            choice = input("Choose your action (1 - Attack, 2 - Defend, 3 - Use Spell, 4 - Heal): ")
            if choice == "1":
                player.attack_target(self.monster)
            elif choice == "2":
                player.defense *= 2
                print(f"{player.name} is defending.")
            elif choice == "3":
                player.use_spell(self.monster)
            elif choice == "4":
                player.heal()
            else:
                print("Invalid choice. Try again.")

            if self.monster.is_alive():
                self.monster.attack_target(player)
            print()

        if player.is_alive():
            print(f"You have defeated the {self.monster.name}!")
        else:
            print("You have been defeated!")

    def find_key(self, player):
        print(f"You found a key in {self.name}!")
        player.keys.append(self.key)
        self.key = None

    def make_choice(self, player):
        if self.name == "Forest Room":
            print("What will you do?")
            print("1. Search for berries")
            print("2. Chop down a tree")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("You found some delicious berries!")
                player.heal()
            elif choice == "2":
                print("You chopped down a tree and found a wooden club!")
                player.attack += 5
            else:
                print("Invalid choice.")

    def print_player_status(self, player):
        print(f"{player.name} ({player.race}, {player.player_class})'s Health: {player.health}/{player.max_health}")

    def print_monster_status(self, monster):
        print(f"{monster.name}'s Health: {monster.health}, Defense: {monster.defense}")


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


# Function to let the player choose a race
def choose_race():
    print("Choose your race:")
    print("1. Human (Balanced stats)")
    print("2. Elf (Higher attack, lower health)")
    print("3. Dwarf (Higher defense, lower attack)")
    race_choice = input("Enter the number of your race choice: ")
    if race_choice == "1":
        return "Human"
    elif race_choice == "2":
        return "Elf"
    elif race_choice == "3":
        return "Dwarf"
    else:
        print("Invalid choice. Defaulting to Human.")
        return "Human"


# Function to let the player choose a class
def choose_class():
    print("Choose your class:")
    print("1. Warrior (Higher attack)")
    print("2. Mage (Higher spell damage)")
    print("3. Healer (Higher healing ability)")
    class_choice = input("Enter the number of your class choice: ")
    if class_choice == "1":
        return "Warrior"
    elif class_choice == "2":
        return "Mage"
    elif class_choice == "3":
        return "Healer"
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return "Warrior"


# Function to let the player choose a name
def choose_name():
    name = input("Enter your name: ")
    return name


# Create player character
player_name = choose_name()
player_race = choose_race()
player_class = choose_class()
player = Character(player_name, player_race, player_class, 100, 20, 10)
player.keys = []

# Create monsters
monster1 = Character("Goblin", "Goblin", 50, 10, 5, 5)
monster2 = Character("Orc", "Orc", 80, 15, 8, 7)
monster3 = Character("Dragon", "Dragon", 150, 25, 15, 10)
monster4 = Character("Skeleton", "Skeleton", 40, 8, 4, 3)
monster5 = Character("Slime", "Slime", 30, 6, 3, 2)

# Create rooms
room1 = Room("Forest Room", "You are in a room surrounded by dense forest.", "Forest Key", monster1)
room2 = Room("Cave Room", "You have entered a dark cave.", "Cave Key", monster2)
room3 = Room("Castle Room", "You find yourself in a grand castle hall.", "Castle Key", monster3)
room4 = Room("Swamp Room", "You are in a murky swamp filled with strange creatures.", "Swamp Key", monster4)
room5 = Room("Mysterious Room", "You enter a mysterious room shrouded in darkness.", "Mysterious Key", monster5)
room6 = Room("Treasure Room", "You found a room filled with treasure!", "Treasure Key")

# Define room connections
room1.connections = [room2]
room2.connections = [room1, room3, room4]
room3.connections = [room2]
room4.connections = [room2, room5, room6]
room5.connections = [room4]
room6.connections = [room4]

# Create and run the RPG game
game = RPGGame(player, [room1, room2, room3, room4, room5, room6])
game.run()
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the current room image
    current_room = game.current_room
    room_image = room_images.get(current_room.name)
    if room_image:
        screen.blit(room_image, (0, 0))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

# Quit the game
pygame.quit()
