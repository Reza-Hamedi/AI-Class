class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1

    def show_info(self):
      print(f"Name: {self.name} | Power: {self.power} | Health: {self.health} | Coins: {self.coins} | Level: {self.level}")

    def is_alive(self):
       return True if self.health > 0 else False

    def attack(self, target):
       target.health -= self.power
       print(f"{self.name} attacked {target.name}!")
       print(f"{target.name}'s health : {target.health}")

    def earn_coins(self, amount):
       self.coins += amount
       print(f"{amount} Coins added to {self.name}")
       print(f"{self.name} has {self.coins} COINS now.")

    def buy_heel_potion(self):
      if self.coins >= 20:
         self.coins -= 20
         self.health += 30
         print(f"{self.name} loses 20 coins :(\n {self.name} has {self.coins} coins.")
         print(f"{self.name} gain +30 health :)\n {self.name} has {self.health} health.")
      else:
         print("Not enough coins :(     !!!!!")

    def level_up(self):
       self.level += 1
       self.power += 5
       print(f"{self.name} reach Level {self. level} | Power {self.power}")


lion = Character("Aslan", 60, 100, 100)
duck = Character("Muffin", 20, 100, 100)
test_method = int(input("Method (1= one by one, 2= Teacher Senario) ? "))
if(test_method == 1):
   practice_number = int(input("Which Practise? "))
   if(practice_number == 1):
      lion.show_info()
   elif(practice_number == 2):
      print(f"{lion.name} is alive :) ") if lion.is_alive() else print(f"{lion.name} is died :(")
   elif(practice_number == 3):
      lion.attack(duck)
   elif(practice_number == 4):
      amount = int(input("How many coins would you give Aslan (Lion Charecter): "))
      lion.earn_coins(amount)
   elif(practice_number == 5):
      lion.buy_heel_potion()
   elif(practice_number == 6):
      lion.level_up()
elif(test_method == 2):
      lion.attack(duck)
      duck.attack(lion)
      duck.attack(lion)
      duck.attack(lion)
      lion.attack(duck)
      duck.buy_heel_potion()
      lion.level_up()
      duck.show_info()
      lion.show_info()
else:
      print("Chose 1 or 2 ")

