import random
dare = None     #dare is none as a global so it works in and out of functions

#Hero Classes
class Knight:
    def __init__(self, name):
        self.name = name        #lets you pick name    
        self.health = 50        #predetermined health

    def light(self):                    #light attack method
        bad_guy.health -= 3                 #subtracts custom light damage from bad guy
        print("You slice one of their limbs!")  #prints custom light attack line

    def heavy(self):                    #heavy attack method
        bad_guy.health -= 9                 #subtracts custom heavy damage from bad guy
        print("You stab them in the chest!")   #prints custom heavy attack line

    def heal(self):
        #if attack 3 picked givees a random 33 percent chance to regain health
        hope = random.randint(1, 3)
        if hope == 3:               #if random number is 3, hero gains custom health
            hero.health += 7
            print("Summmoning your courage you gain strength")  #prints custom heal line 
        print("Health:",hero.health) #prints hero health
        
    def attack_action(self):    #does attack action
        attack_menu()               #prints attack menu
        attack = None;              #attack is none initally
        while attack == None:       #while player doesnt choose an option it loops
            try:                        #try gets rid of error if str inputted
                attack = int(input("Pick an Attack: "))
            except:
                print("That is not an attack!") #if string inputted prints line and restarts loop
                continue
            if attack == 1:     #if light chosen calls custom hero light attack from class
                hero.light()
            elif attack == 2:   #if heavy chosen calls custome hero heavy attack from class
                hero.heavy()
            elif attack == 3:   #if heal chosen calls custom hero heal ability
                hero.heal()
            else:
                attack = None   #if no attack chosen prints line and resets attack value
                print("Don't hesitate! Attack!")
class Viking:
    def __init__(self, name):
        self.name = name        #lets you pick name  
        self.health = 45        #predetermined health

    def light(self):            #light attack method
        bad_guy.health -= 3         #subtracts custom light damage from bad guy
        print("You hit them!")      #prints custom light attack line

    def heavy(self):                        #heavy attack method
        bad_guy.health -= 8                     #subtracts custom heavy damage from bad guy
        print("You knock them backwards!")      #prints custom heavy attack line

    def heal(self):
        #if attack 3 picked gives a random 50 percent chance to regain health
        hope = random.randint(1, 2)
        if hope == 2:
            hero.health += 8        #custom health value
            print("Calling on the gods, their presence gives you strength") #prints heal line
        print("Health:",hero.health)    #prints hero health
        
    def attack_action(self):        #attack action method
        attack_menu()                   #prints attack menu
        attack = None;                  #attack is none initally
        while attack == None:           #while player doesnt choose an option it loops
            try:                             #try gets rid of error if str inputted
                attack = int(input("Pick an Attack: "))
            except:
                print("That is not an attack!") #if string inputted prints line and restarts loop
                continue
            if attack == 1:     #if light chosen calls custom hero light attack from class
                hero.light()
            elif attack == 2:   #if heavy chosen calls custom hero heavy attack from class
                hero.heavy()
            elif attack == 3:   #if heal chosen calls custom hero heal ability
                hero.heal()
            else:
                attack = None   #if no attack chosen prints line and resets attack value
                print("Don't hesitate! Attack!")
class Samurai:
    def __init__(self, name):
        self.name = name        #lets you pick name  
        self.health = 40        #predetermined health

    def light(self):            #light attack method
        bad_guy.health -= 4         #subtracts custom light damage from bad guy
        print("You slash them!")    #prints custom light attack line

    def heavy(self):                #heavy attack method
        bad_guy.health -= 7             #subtracts custom heavy damage from bad guy
        print("You slice their limb!")  #prints custom heavy attack line

    def heal(self):
        #if attack 3 picked givees a random 50 percent chance to regain health
        hope = random.randint(1, 2)
        if hope == 1:       #custom hope value
            hero.health += 6  #custom health value
            print("You feel a bit better after catching your breathe.")     #prints custom health line
        print("Health:",hero.health)    #prints hero health
        
    def attack_action(self):            #attack action method
        attack_menu()                   #prints attack menu
        attack = None;                  #initale attacke value
        while attack == None:           #loops until one of three attacks chosen
            try:                        #gets rid of str input error
                attack = int(input("Pick an Attack: "))
            except:
                print("That is not an attack!")     #if str inputted prints line and restarts loop
                continue
            if attack == 1:     #if light chosen calls custom hero light attack from class
                hero.light()
            elif attack == 2:   #if heavy chosen calls custome hero heavy attack from class
                hero.heavy()
            elif attack == 3:   #if heal chosen calls custom hero heal ability
                hero.heal()
            else:
                attack = None   #if no attack chosen prints line and resets attack value
                print("Don't hesitate! Attack!")
        

#Foe Classes
#Each class has a predetermined name and health
class Assassin:         #class for foe number 1
    def __init__(self):
        self.name = "Neya"  
        self.health = 35;
        
    def light(self):
        #picks two different lines to say
        vary = random.randint(1,2)
        if vary == 1:
            print(bad_guy.name,"niches your leg!")
        else:
            print(bad_guy.name,"slices your arm!")
        hero.health -= 4    #subtaracts custom amount from hero health for light
        
    def heavy(self):
        #picks two different lines to say
        vary = random.randint(1,2)
        if vary == 1:
            print(bad_guy.name,"stabs you in the chest!")
        else:
            print(bad_guy.name,"slashes your leg!")
        hero.health -= 6    #subtaracts custom amount from hero health for heavy

    def attack_action(self):        #method for attack action
        move = random.randint(1,2)      #randomly picks one of two atacks
        print("\n")
        if move == 1:
            bad_guy.light()     #does light attack
        else:
            bad_guy.heavy()     #does heavy attack
            
    def taunt(self):
        #function for bad guy taunts
        #picks a random number and either prints a taunt or remains silent
        #all taunts are custom to the class and the number balue of taunts are custom to class
        can_taunt = random.randint(1,12)    #picks number 1 to 12
        if can_taunt == 1:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'I'm an assassin, killing is what I do and you're next!'")
        elif can_taunt == 3:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'As soon as I was handed my blades you were already dead.'")
        elif can_taunt == 5:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'The mighty'", hero.name,"how foolish you are.")
        elif can_taunt == 7:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'You are no hero'")
        elif can_taunt == 9:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("''Do you know why I always win in the arena? Because i'm too fast.")

    def health_ind(self):
        #function to indicate foe health
        if bad_guy.health < 28 and bad_guy.health >= 17: #if under 3 quester prints line
            print(bad_guy.name,"looks injured.")
        elif bad_guy.health < 17 and bad_guy.health >= 10:  #if under half prints line
            print(bad_guy.name,"looks really injured.")
        elif bad_guy.health < 10:       #if under 10 prints line
            print(bad_guy.name,"is very weak!")
            
class Fighter:  #class for foe number 2
    def __init__(self):
        self.name = "Fenrir"    #predetermine name and health
        self.health = 55;

    def light(self):
        #picks two different lines to say for light attack
        vary = random.randint(1,2)
        if vary == 1:
            print(bad_guy.name,"cuts your arm!")
        else:
            print(bad_guy.name,"niches your chest!")
        hero.health -= 3    #takes away custom light damage from hero health
        
    def heavy(self):
        #picks two different lines to say based upon attack chosen
        vary = random.randint(1,2)
        if vary == 1:
            print(bad_guy.name,"strikes your shoulder!")
        else:
            print(bad_guy.name,"gashes your leg!")
        hero.health -= 8  #takes away custom heavy damage from hero health

    def attack_action(self):    #attack action method
        move = random.randint(1,2)  #picks a random attack move
        print("\n")
        if move == 1:
            bad_guy.light()     #calls light attack method
        else:
            bad_guy.heavy()     #calls heavy attack method
            
    def taunt(self):
        #function for bad guy taunts
        #picks a random number and either prints a taunt or remains silent
        #all taunts are custom to the class and the number value of taunts are custom to class
        can_taunt = random.randint(1,12)
        if can_taunt == 2:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'I am the fighter. I fight until I die!'")
        elif can_taunt == 4:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'You are in my Arena fool!'")
        elif can_taunt == 6:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'You are called",hero.name,"you should have been called dead man walking.'")
        elif can_taunt == 8:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'Face it you already lost.'")
        elif can_taunt == 10:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'Do you really think you can beat me!?'")

    def health_ind(self):
        #function to indicate foe health
        if bad_guy.health < 40 and bad_guy.health >= 27:    #if below 3/4 prints line
            print(bad_guy.name,"looks injured.")
        elif bad_guy.health < 27 and bad_guy.health >= 10:  #if below half prints line
            print(bad_guy.name,"looks really injured.")
        elif bad_guy.health < 10:                           #if below 10 prints line
            print(bad_guy.name,"is very weak!")

class Ninja:    #class for foe number 3
    def __init__(self):
        self.name = "Imagawa"
        self.health = 45;

    def light(self):
        #picks two different lines to say based upon attack chosen
        vary = random.randint(1,2)
        if vary == 1:
            print(bad_guy.name,"nicks your cheek!")
        else:
            print(bad_guy.name,"swings adown and cuts your leg!")
        hero.health -= 3    #subtracts custom light damage from hero
        
    def heavy(self):
        #picks two different lines to say based upon attack chosen
        vary = random.randint(1,2)
        if vary == 1:
            print(bad_guy.name,"cuts deeply into your arm!")
        else:
            print(bad_guy.name,"spins and slices your chest!")
        hero.health -= 7    #subtracts custom heavy damage from hero

    def attack_action(self):    #bad guy attack action method
        move = random.randint(1,2)  #determines attack based on random number
        print("\n")
        if move == 1:
            bad_guy.light()     #calls light attack method
        else:
            bad_guy.heavy()     #calls heavy attack method
            
    def taunt(self):
        #function for bad guy taunts
        #picks a random number and either prints a taunt or remains silent
        #all taunts are custom to the class and the number balue of taunts are custom to class
        can_taunt = random.randint(1,12)
        if can_taunt == 8:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'Were you too distracted to see my move or too slow?'")
        elif can_taunt == 9:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'You really made a mistake trying to fight me.'")
        elif can_taunt == 10:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'So many others have tried to fight me why are you any different?'")
        elif can_taunt == 11:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'Surrender",hero.name,"'")
        elif can_taunt == 12:
            print(bad_guy.name,"taunts you!",bad_guy.name,"says:")
            print("'I am the flower and the flower never gets cut!!'")

    def health_ind(self):
        #function to indicate foe health
        if bad_guy.health < 30 and bad_guy.health >= 22:    #if under about 3/4 prints line
            print(bad_guy.name,"looks injured.")
        elif bad_guy.health < 22 and bad_guy.health >= 10:  #id under half prints line
            print(bad_guy.name,"looks really injured.")
        elif bad_guy.health < 10:                           #if under 10 prints line
            print(bad_guy.name,"is very weak!")
    
def main_menu():    #prints main menu in function to clean up code
    print("""
WELCOME TO THE ARENA
    1-Start
    2-Quit
    """)
    
def hero_menu():
    #prints part of the txt file for heroes, to make hero menu
    hero_des = open("hero_pick.txt")    #open hero file
    heroes = hero_des.readlines()       #read lines fo file
    print("\n", heroes[0],heroes[1],heroes[4],heroes[7],heroes[10]) #print certain lines

def hero_descriptions():
    #prints all but one line of hero txt file for descriptions
    hero_des = open("hero_pick.txt")
    heroes = hero_des.readlines()
    for i in range(9):  #counts to 9 and prints first ten lines
        print(heroes[i])
    hero = None

def hero_announce():    #aanounce what hero was chosen and capitilizes their name
    print(hero.name.capitalize(), end=" ")
    print("enters the Arena")
    input("\n\tPress enter to continue")

def bad_guy_menu():
    #prints part of the txt file for bad guys
    bad_guy_des = open("bad_guy_pick.txt")  #opens file
    bad_guys = bad_guy_des.readlines()      #reads file
    print("\n", bad_guys[0], bad_guys[1], bad_guys[4], bad_guys[7], bad_guys[10])   #prints lines 0,1,4,7,10

def bad_descriptions():
    #prints all but one line of foe txt file for descriptions
    bad_guy_des = open("bad_guy_pick.txt")
    bad_guys = bad_guy_des.readlines()
    for k in range(9):  #prints first 10 lines, 0 to 9
        print(bad_guys[k])
    bad_guy = None
    
def announce(): #function for announcing who is fighitng
    print("\nThe Next Arena Battle is:")
    print(hero.name.capitalize(), end=" ")
    print("VS", end=" ")
    print(bad_guy.name)
    input("\n\tPress enter to continue")
    print("\n3.. 2.. 1..FIGHT!!")


def attack_menu():  #function for the hero attack menu
    #prints attack menu
    print("""
It is your Chance to Attack!
    1-Light Attack
    2-Heavy Attack
    3-Sidestep/Potential to Heal
    """)
            
def first_menu():   #function to print go first menu
            print("""
Attack First?
1-Attack first!
2-Wait for you Foe!
""")
            
def attack_first(): #function to determine fi player goes first
    #Gives the player the opprtunity to go first
    first = None
    count = 0
    while first != 1 and first != 2:    #loops until player says to go first or not
        first_menu()
        try:
            first = int(input("Pick:"))
        except:
            print("Not an option.")
        if first == 1:
            break
        elif first == 2:
            break
        else:
            count += 1
            if count == 3:  #if player does not the correct options, prints line, and breaks so bad guy goes first
                print("You hesitated too long. Your foe strikes first!")
                break
            print("Not an option")
    if first == 1:  #if player wants to go first lets them attack otherwise ignores
        hero.attack_action()
        input("\n\tPress enter to continue")
        
def combat_loop():  #looops combat
    while hero.health > 0 and bad_guy.health > 0:   #loops combat until someone dies
        bad_guy.attack_action()     #calls bad guy attack method
        bad_guy.taunt()             #calls bad guy taunt method
        if hero.health <= 0:        #checks hero health
            break
        print("Health:",hero.health)            #displays hero health
        input("\n\tPress enter to continue")
        hero.attack_action()        #calls hero attack method
        if bad_guy.health <= 0:     #checks bad guy health
            break
        bad_guy.health_ind()        #calls bad guy health indicator method
        input("\n\tPress enter to continue")
        
def winner():   #function to declare winner based on health
    if hero.health <= 0:    #hero defeat section
        print("DEFEAT. YOU HAVE LOST THE ARENA.")
        print(bad_guy.name.upper(),"IS THE NEW CHAMPION!")
    elif bad_guy.health <= 0:   #foe defeat section
        print("\nWITH THIS HIT YOU DEAL A MORTAL BLOW")
        print("YOU HAVE WON THE ARENA!", bad_guy.name.upper(),"IS SLAIN!")
        print(hero.name.upper(),"IS OUR NEW CHAMPION!!!")
    input("\n\tPress enter to continue")
    
def again_menu():   #function to play again menu
    print("""
1-Play Again
2-Quit
    """)

#MAIN PART OF CODE
#main menu
dare = None
while dare != 1 and dare != 2:
    #only stops menu if you start or quit
    main_menu()
    try:        #gets rid of str input error
        dare = int(input("Choice:"))
    except:     #if str inputted prints line and restarts loop
        print("Inavlid choice")
        continue
    if dare == 2:   #checks if option either  valid option is used
        break
    elif dare == 1:
        break
    else:       #if not 1 or 2 prints line
        print("Invalid input")

#while you click start or want to keep playing it loops the game
#main loop of game
while dare == 1:
    #calls class based upon hero chosen and loops until picked
    hero = None
    while hero != 1 or 2 or 3:      #loops her omenu selection
        #hero selection menu
        hero_menu()
        try:    #gets rid of str error
            hero = int(input("\nPick:"))
        except:     #restarts loop if str inputted
            print("Not a hero.")
            continue
        if hero == 1:   #knight selection
            name = input("Name your knight: ")
            hero = Knight(name)
            break
        elif hero == 3: #samurai selection
            name = input("Name your Samurai: ")
            hero = Samurai(name)
            break
        elif hero == 2: #viking selection
            name = input("Name your Viking: ")
            hero = Viking(name)
            break
        elif hero == 4: #hero descriptions display option
            hero_descriptions()
        else:
            print("Not a hero")
            hero = None
    #announces who the hero is      
    hero_announce()
    #starts bad guy class based upon which one chosen and loops until picked
    bad_guy = None
    while bad_guy != 1 or 2 or 3:   #loops bad guy selection menu
        #bad guy selection menu
        bad_guy_menu()
        try:    #gets rid of str error
            bad_guy = int(input("Pick:"))
        except:
            print("That Foe is not in the Arena.")
            continue
        if bad_guy == 1:    #makes assasin class
            bad_guy = Assassin()
            break
        elif bad_guy == 2:  #makes fighter class
            bad_guy = Fighter()
            break
        elif bad_guy == 3:
            bad_guy = Ninja()   #makes ninja class
            break
        elif bad_guy == 4:  #displays bad guy descriptions
            bad_descriptions()
        else:   #if not an option prints line
            print("That Foe is not in the Arena")
            bad_guy =None 
    #announces who is fighitng
    announce()
    #lets player decide to go first
    attack_first()
    #loops combat actions
    combat_loop()
    #End of Game announces winner
    winner()
    #Play again option
    dare = None
    while dare != 1 or dare != 2:   #loops play again menu until play again or wuit is chosen
        again_menu()
        try:
            dare = int(input("Choice:"))
        except:
            print("Invalid Input.")
            continue
        if dare == 1:
            break
        elif dare == 2:
            break
        else:
            print("Invalid input")
    if dare == 2:   #if play choses to quit it breaks the main game loop
        break


#Game over and exit
print("\n\tGAME OVER")
input("\tPress enter to exit")
