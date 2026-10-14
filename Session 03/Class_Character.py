class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1
    def show_info(self):
      print(f"name: {} | power: {} | health: {} | coins: {}")

