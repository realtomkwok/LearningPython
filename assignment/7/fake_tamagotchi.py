import random
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.health = random.randrange(70, 100)
        self.mood = random.randrange(50, 100)
        self.hunger = random.randrange(60)
        self.is_alive = True
        
    def leave_alone(self):
        """
        some possible behavior:
            takes a rest most of the time, health and mood increase slightly
            catches a rat once in a while: mood increases dramatically
            eats some poisonous food: health decreases dramatically
        """
        actions = ["takeARest","catchARat", "eatPoison", "fightWACat"]
        result = random.choice(actions)
        if result == "takeARest":
            self.health += random.randrange(5,10)
            self.mood += random.randrange(5,20)
        elif result == "catchARat":
            self.mood += random.randrange(30,50)
        elif result == "eatPoison":
            self.health -= random.randrange(30,50)
        elif result == "fightWACat":
            self.mood -= random.randrange(10,20)
            self.health -= random.randrange(10,20)

    
    def feed(self):
        """
        some possible behavior:
            if not full, hunger decreases and mood increases
            if too full (overeating), health decreases and mood decreases 
        """
        self.hunger -= random.randrange(20,35)
        
        if self.hunger < 0:  # overeats
            print("{} seems to have had too much!".format(self.name))
            self.health -= random.randrange(5, 15)
            self.mood -= random.randrange(5, 10)
            self.hunger = 0
        else:
            print("{} has had a good meal!".format(self.name))
            self.mood += random.randrange(5, 10)
            
    def play(self):
        """
        some possible behavior:
            if too hungry or too unhappy, refuses to play
            otherwise, mood increases
        """
        
    def take_to_vet(self):
        """
        some possible behavior:
            health increases dramatically
            mood decreases since it hates seeing the vet
        """
        
    def show_status(self):
        if self.mood > 80:
            current_status = 'happy'
        elif self.mood > 50:
            current_status = "OK"
        else:
            current_status = "unhappy"
            
        if self.health < 30:
            current_status = "sick"
            
        print("{} looks {}".format(self.name, current_status))
        
    def update(self):
        """
        check and update the attributes of the pet
        Please add additional behavior
        """
        self.hunger += random.randrange(10,20)
        if self.hunger > 100:  # cannot exceed the max value of 100
            self.hunger = 100
        if self.hunger > 80:
            self.health -= random.randrange(10, 30)
            
        if self.health <= 0:
            self.is_alive = False
        
print("Welcome to Virtual Pet!")
print("Your goal in this game is to keep your pet alive for as many rounds as possible!")
name = input("Please give your pet a name: ")
pet = Pet(name)
n_rounds = 0
image = """
░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░ 
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░ 
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ 
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░
▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░ 
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░
░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░
"""
print("Say hi to {}! Isn't he cute?".format(name))
print(image)
menu = """
What would you like to do with {}: 
  (1) leave it alone
  (2) feed
  (3) play
  (4) take to the vet
Please choose an action: """.format(pet.name)
while True:
    n_rounds += 1
    time.sleep(1.5)
    print("-" * 100)
    action = input(menu)
    if action == "1":
        pet.leave_alone()
    elif action == "2":
        pet.feed()
    elif action == "3":
        pet.play()
    elif action == "4":
        pet.take_to_vet()
    else:
        print("Invalid action, will leave the pet alone")
        pet.leave_alone()
    pet.update()
    pet.show_status()
    if not pet.is_alive:
        print("{0} is dead! Poor {0}!".format(pet.name))
        break
        
print("Game over. {} lived for {} rounds".format(pet.name, n_rounds))