import random

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 3, self.attack + 3)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")


# Game logic
def play_game():
    print("Welcome to the Strategy Game!")

    # Create players
    player = Player("Player 1")
    enemy = Player("Enemy")

    # Game loop
    while player.is_alive() and enemy.is_alive():
        # Player's turn
        print(f"\n{player.name}'s turn:")
        player.attack_enemy(enemy)
        if not enemy.is_alive():
            break

        # Enemy's turn
        print(f"\n{enemy.name}'s turn:")
        enemy.attack_enemy(player)

    # Game over
    print("\nGame over!")
    if player.is_alive():
        print(f"{player.name} wins!")
    else:
        print(f"{enemy.name} wins!")


# Start the game
play_game()

