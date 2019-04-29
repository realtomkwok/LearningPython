import random
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.health = random.randrange(70, 100)
        self.mood = random.randrange(50, 100)
        self.hunger = random.randrange(60)
        self.cleanliness = random.randrange(0,100)
        # changing value
        self.healthChange = 0
        self.moodChange = 0
        self.hungerChange = 0
        self.cleanlinessChange = 0
        self.is_alive = True

    def resetChangingValues(self):
        self.healthChange = 0
        self.moodChange = 0
        self.hungerChange = 0
        self.cleanlinessChange = 0

    def __repr__(self):
        return r"""
    .---------------------------------.
    | .-----------------------------. |
            
            Round {} 
            ^__^
            (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
                        
            {}                                                            
            Health: {}/100      
            Mood: {}/100    
            Hunger: {}/100
            Cleanliness: {}/100        

    | |_____________________________| |
    |_________________________________|      
        """.format(n_rounds, self.name, self.health, self.mood, self.hunger, self.cleanliness)
        
    def leave_alone(self):

        actions = ["takeARest","catchARat", "eatPoison", "fightWACat"]
        result = random.choice(actions)

        if result == "takeARest":
            time.sleep(1.0)
            print("Shhhhh {} is taking a rest. ZZZ".format(self.name))
            #Health+
            self.healthChange = random.randrange(5,10)
            self.health += self.healthChange     
            #Mood+
            self.moodChange = random.randrange(5,20)         
            self.mood += self.moodChange
            #print status
            time.sleep(1.5)
            print("Health: +{}".format(self.healthChange))
            time.sleep(0.5)
            print("Mood: +{}".format(self.moodChange))

        if result == "catchARat":
            time.sleep(1.0)
            print("{} caught a rat. LOL".format(self.name))
            self.moodChange = random.randrange(30,50)
            self.mood += self.moodChange
            self.cleanlinessChange = random.randrange(10,20)
            self.cleanliness -= self.cleanlinessChange
            time.sleep(0.5)
            print("Mood: +{}".format(self.moodChange))
            print("Cleanliness: -{}".format(self.cleanlinessChange))

        if result == "eatPoison":
            time.sleep(1.0)
            print("{} just ate some poisonous food! Poor {}!".format(self.name, self.name))
            self.healthChange = random.randrange(30,50)
            self.health -= self.healthChange
            time.sleep(0.5)
            print("Health: -{}".format(self.healthChange))

        if result == "fightWACat":
            print("{} came across a cat. A fight can't be avoided...".format(self.name))
            time.sleep(1.0)
            print("And the winner goes to (drum rolling)")
            time.sleep(1.0)
            resultOfFight = random.choice([0, 1])
            if resultOfFight == 0:
                print("{}!".format(self.name))
                self.moodChange = random.randrange(10,20)
                self.mood += self.moodChange
                time.sleep(0.5)
                print("Mood: +{}".format(self.moodChange))
            elif resultOfFight == 1:
                print("The Cat!")
                self.moodChange = random.randrange(10,20)
                self.mood -= self.moodChange
                time.sleep(0.5)
                print("Mood: -{}".format(self.moodChange))
            self.healthChange = random.randrange(10,20)
            self.health -= self.healthChange
            self.cleanlinessChange = random.randrange(20,40)
            self.cleanliness -= self.cleanlinessChange
            
            #print status
            time.sleep(0.5)
            print("Health: -{}".format(self.healthChange))
            print("Cleanliness: -{}".format(self.cleanlinessChange))

    
    def feed(self):
        if self.hunger < 0:  # overeats
            print("{} seems to have had too much!".format(self.name))
            self.healthChange = random.randrange(5, 15)
            self.health -= self.healthChange
            self.moodChange = random.randrange(5, 10)
            self.mood -= self.moodChange
            self.hungerChange = 0
            self.hunger -= self.hungerChange
            time.sleep(1.0)
            print(r"""
            Health: -{}
            Mood: -{}
            Hunger: \+{}
            """.format(self.healthChange, self.moodChange, self.hungerChange))
        else:
            print("{} has had a good meal!".format(self.name))
            self.hungerChange = random.randrange(20,35)
            self.hunger -= self.hungerChange
            self.moodChange = random.randrange(5, 10)
            self.mood += self.moodChange

            time.sleep(1.0)
            print(r"""
            Mood: +{}
            Hunger: -{}
            """.format(self.moodChange, self.hungerChange))
            
    def play(self):
        if self.hunger > 40:
            print("{} is too hungry to play. Why not feed {} some food?".format(self.name, self.name))
            return
        elif self.mood < 40:
            print("Seems {} is in a bad mood. Why not leave {} alone for a while?".format(self.name, self.name))
            return
        else:
            print(r"""
 _______________
    < Yay! >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
            """)
            self.moodChange = random.randrange(10, 30)
            self.mood += self.moodChange
            self.cleanlinessChange = random.randrange(10,40)
            self.cleanliness -= self.cleanlinessChange
            time.sleep(1.0)
            print("Mood: +{}".format(self.moodChange))
            print("Cleanliness: -{}".format(self.cleanlinessChange))


    def take_to_vet(self):
        self.moodChange = random.randrange(10,20)
        self.mood -= self.moodChange
        print(r"""
_________________
< I hate the vet >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
        
        """)
        time.sleep(0.5)
        print("Mood: -{}".format(self.moodChange))

        if self.health > 50:
            print("{} took some medicine.".format(self.name))
            self.healthChange = random.randrange(40,50)
            self.health += self.healthChange
            time.sleep(0.5)
            print("Health: +{}".format(self.healthChange))
            print("{} feels good now!".format(self.name))
        else:
            print("{} is seriously ill. A surgery is needed!".format(self.name))
            surgeryResult = random.choice([0,1]) #0 is better, 1 is worse.
            if surgeryResult == 0:
                self.healthChange = random.randrange(50,99)
                self.health += self.healthChange
                time.sleep(1.0)
                print("Health: +{}".format(self.healthChange))
                print("{} feels good now!".format(self.name))
            elif surgeryResult == 1:
                self.health = 0
                time.sleep(1.0)
                print("Sorry, we did everything we could.")
                return

    def takeABath(self):
        self.moodChange = random.randrange(10,30)
        self.mood -= self.moodChange
        print(r"""
_________________
< I hate bath >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
        
        """)
        time.sleep(0.5)
        print("Mood: -{}".format(self.moodChange))

        self.cleanlinessChange = random.randrange(30,60)
        self.cleanliness += self.cleanlinessChange
        print("Cleanliness: +{}".format(self.cleanlinessChange))
            

    def update(self):
        if self.healthChange == 0:
            self.health -= random.randrange(0,10)
        if self.cleanlinessChange == 0:
            self.cleanliness -= random.randrange(5,20) 
        if self.hungerChange == 0:
            self.hunger += random.randrange(10,20)

        if self.hunger > 100:  # cannot exceed the max value of 100
            self.is_alive = False
            print("{) died of starvation. Poor {}".format(self.name, self.name))
        elif self.hunger > 80:
            self.health -= random.randrange(10, 30)
        elif self.hunger < 0:
            self.hunger = 0

        if self.mood > 100:
            self.mood = 100

        if self.cleanliness < 0:
            self.cleanliness = 0
        elif self.cleanliness > 100:
            self.cleanliness = 100

        if self.health > 100:
            self.health = 100
        if self.health <= 0:
            self.is_alive = False
            
        

# Game Start
print(r"""
██╗   ██╗██╗██████╗ ████████╗██╗   ██╗ █████╗ ██╗         
██║   ██║██║██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║         
██║   ██║██║██████╔╝   ██║   ██║   ██║███████║██║         
╚██╗ ██╔╝██║██╔══██╗   ██║   ██║   ██║██╔══██║██║         
 ╚████╔╝ ██║██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗    
  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝    
                                                          
██████╗ ███████╗████████╗           
██╔══██╗██╔════╝╚══██╔══╝  
██████╔╝█████╗     ██║   
██╔═══╝ ██╔══╝     ██║ 
██║     ███████╗   ██║  
╚═╝     ╚══════╝   ╚═╝  
""")
time.sleep(0.5)
print("Your goal in this game is to keep your pet alive for as many rounds as possible!")
time.sleep(0.5)
name = input("Please give your pet a name: ")
pet = Pet(name)
n_rounds = 0
time.sleep(1.0)
print(r"""
Say hi to {}!
""".format(name))
print(r"""
 _______________
< Hello world! >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

""")
# print(image)

menu = """
What would you like to do with {}: 
  (1) leave it alone
  (2) feed
  (3) play
  (4) take to the vet
  (5) take a bath
Please choose an action: """.format(pet.name)
while True:
    n_rounds += 1
    time.sleep(1.0)
    print("-" * 100)
    print(pet)
    action = input(menu)
    if action == "1":
        pet.leave_alone()
    elif action == "2":
        pet.feed()
    elif action == "3":
        pet.play()
    elif action == "4":
        pet.take_to_vet()
    elif action == "5":
        pet.takeABath()
    else:
        print("Invalid action, will leave the pet alone")
        pet.leave_alone()
    pet.update()
    pet.resetChangingValues()
    if not pet.is_alive:
        print("{0} is dead! Poor {0}!".format(pet.name))
        break
        
print("Game over. {} lived for {} rounds".format(pet.name, n_rounds))