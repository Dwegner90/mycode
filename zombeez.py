import random

# Base class for characters
class Character:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def attack(self, target):
        damage = random.randint(1, self.attack_damage)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")

# Zombie class, subclass of Character
class Zombie(Character):
    def __init__(self, name, health, attack_damage):
        super().__init__(name, health, attack_damage)

# Player class, subclass of Character
class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)
        self.supplies = 0
        self.weapon = "Fists"
        self.companion = None

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"You have equipped a {weapon}!")

# Companion class, subclass of Character
class Companion(Character):
    def __init__(self, name, health, attack_damage):
        super().__init__(name, health, attack_damage)

# Building class
class Building:
    def __init__(self, name):
        self.name = name

    def search(self, player):
        print(f"You search the {self.name}. What would you like to do?")
        print("1. Search for supplies")
        print("2. Look for weapons")
        print("3. Leave")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            self.search_supplies(player)
        elif choice == "2":
            self.search_weapons(player)
        elif choice == "3":
            print("You leave the building.")
        else:
            print("Invalid choice! Try again.")

    def search_supplies(self, player):
        supplies = random.randint(1, 5)
        player.supplies += supplies
        print(f"You found {supplies} supplies in the {self.name}.")

    def search_weapons(self, player):
        weapons = ["Baseball Bat", "Machete", "Shotgun"]
        weapon = random.choice(weapons)
        player.equip_weapon(weapon)
        print(f"You found a {weapon} in the {self.name}.")

    def combat(self, player):
        zombie = Zombie("Zombie", 50, 10)
        print(f"\nA {zombie.name} appears!")
        while True:
            print("\nOptions:")
            print("1. Attack")
            print("2. Defend")
            print("3. Run")
            choice = input("Enter your choice (1, 2, or 3): ")

            if choice == "1":
                attack(player, zombie)
            elif choice == "2":
                defend(player)
            elif choice == "3":
                run_away()
                break
            else:
                print("Invalid choice! Try again.")

            if player.health <= 0:
                print("Game Over! You have been defeated.")
                break
            elif zombie.health <= 0:
                print("Congratulations! You defeated the zombie.")

# Attack function
def attack(player, target):
    player.attack(target)
    if target.health > 0:
        target.attack(player)
        if player.health <= 0:
            print("Game Over! You have been defeated.")

# Defend function
def defend(player):
    player_defense = random.randint(1, 5)
    print(f"{player.name} takes a defensive stance and reduces incoming damage by {player_defense}.")
    player.defense += player_defense
    print(f"{player.name} defends against the enemy's attack.")

# Run away function
def run_away():
    print("You run away from the enemy.")

# Main game function
def main():
    print("Welcome to the Zombie Defense RPG!")
    print("The city has fallen to a zombie apocalypse. Your goal is to gather enough supplies to survive and find a way to escape.")
    print("You wake up inside a building with a faint memory of the events leading to the apocalypse.")

    player_name = input("Enter your name: ")
    player = Player(player_name)

    starting_choice = input("Do you want to search the building? (y/n): ")
    if starting_choice.lower() == "y":
        building_name = random.choice(["Abandoned House", "Empty Store", "Broken Office"])
        building = Building(building_name)
        building.search(player)
        building.combat(player)

    # Dictionary to connect different buildings/rooms
    rooms = {
        "Warehouse": Building("Warehouse"),
        "Hospital": Building("Hospital"),
        "Police Station": Building("Police Station"),
        "School": Building("School"),
        "Gas Station": Building("Gas Station"),
        "Abandoned House": Building("Abandoned House"),
        "Empty Store": Building("Empty Store"),
        "Broken Office": Building("Broken Office"),
        "Shady Alley": Building("Shady Alley"),
        "Apartment Building": Building("Apartment Building"),
        "Cathedral": Building("Cathedral"),
        "Library": Building("Library"),
        "Park": Building("Park")
    }

    random_building = random.choice(list(rooms.keys()))
    current_building = rooms[random_building]

    while True:
        print(f"\nYou are in the {current_building.name}. What would you like to do?")
        print("1. Search for supplies")
        print("2. Look for weapons")
        print("3. Move to another building")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            current_building.search_supplies(player)
        elif choice == "2":
            current_building.search_weapons(player)
        elif choice == "3":
            next_building = random.choice(list(rooms.keys()))
            current_building = rooms[next_building]
            current_building.search(player)
            current_building.combat(player)
            if player.health <= 0:
                print("Game Over! You have been defeated.")
                break
            elif player.supplies >= 20:
                print("\nYou have gathered enough supplies to survive and continue your journey.")
                print("You find a note that leads you to an old military outpost in the outskirts of the city.")
                print("The outpost is rumored to have a helicopter that can take you to safety.")
                break
        else:
            print("Invalid choice! Try again.")

    print("\nYou reach the old military outpost and find the helicopter.")
    print("As the engine roars to life, you take off and leave the zombie-infested city behind.")
    print("Congratulations! You have successfully escaped the apocalypse!")

if __name__ == "__main__":
    main()

