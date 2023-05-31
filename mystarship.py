import random

class Spaceship:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.take_damage(damage)
        print(f"{self.name} attacked {enemy.name} and dealt {damage} damage!")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, spaceship):
        damage = random.randint(1, self.attack_power)
        spaceship.take_damage(damage)
        print(f"{self.name} attacked {spaceship.name} and dealt {damage} damage!")

def main():
    spaceship = Spaceship("Falcon", 100, 20)
    enemies = [
        Enemy("Alien1", 50, 10),
        Enemy("Alien2", 60, 15),
        Enemy("Alien3", 70, 20)
    ]

    print("Space Battle Game")
    print(f"{spaceship.name} has entered the battle!")
    print("Enemies:")
    for enemy in enemies:
        print(f"{enemy.name} - Health: {enemy.health}, Attack Power: {enemy.attack_power}")
    print()

    while spaceship.is_alive() and any(enemy.is_alive() for enemy in enemies):
        # Player's turn
        print(f"{spaceship.name}'s turn:")
        enemy = random.choice(enemies)
        spaceship.attack(enemy)
        print()

        # Enemies' turn
        for enemy in enemies:
            if enemy.is_alive():
                print(f"{enemy.name}'s turn:")
                enemy.attack(spaceship)
                print()

        # Check game over condition
        if not spaceship.is_alive():
            print("Game Over! The spaceship has been destroyed.")
        elif not any(enemy.is_alive() for enemy in enemies):
            print("Congratulations! You have defeated all the enemies!")

if __name__ == "__main__":
    main()

