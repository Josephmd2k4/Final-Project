import tkinter #imports the library for creating windows which will be used throughout the program
from tkinter import ttk
import random #import random for certain game mechanics.

def startingstats(): #creates all starting statistics for all fights
    global hp
    global atkpower
    global burkeatk
    global burkehp
    global cazalasatk
    global cazalashp
    global lewisatk
    global lewishp
    global eicholtzatk
    global eicholtzhp
    global robersonatk
    global robersonhp
    hp = 20
    atkpower = 3
    burkehp = 10
    burkeatk = 4
    cazalashp = 15
    cazalasatk = 6
    lewishp = 20
    lewisatk = 8
    eicholtzhp = 30
    eicholtzatk = 8
    robersonhp = 50
    robersonatk = 12

def clicked(event):
    global hp
    global label1
    global window1
    hp = hp + 1 #adds 1 to hp, to make the game easier if the user keeps losing, can be repeated infinitely
    label1.configure(text=f'Current HP = {hp}')
    
def slap(event):
    global atkpower
    global window2
    dmg_dealt = 1 + atkpower #you deal 1 damage more than your current atk power
    if current_fight == 1: #sorts by who you are fighting
        global burkehp
        burkehp = burkehp - dmg_dealt
        dmgthisturn = dmg_dealt
        dmg_dealt = 0
        current_prof = "Dr. Burke"
    if current_fight == 2:
        global cazalashp
        cazalashp = cazalashp - dmg_dealt
        dmgthisturn = dmg_dealt
        dmg_dealt = 0
        current_prof = "Dr. Cazalas"
    if current_fight == 3:
        global lewishp
        lewishp = lewishp - dmg_dealt
        dmgthisturn = dmg_dealt
        dmg_dealt = 0
        current_prof = "Dr. Lewis"
    if current_fight == 4:
        global eicholtzhp
        eicholtzhp = eicholtzhp - dmg_dealt
        dmgthisturn = dmg_dealt
        dmg_dealt = 0
        current_prof = "Dr. Eicholtz"
    if current_fight == 5:
        global robersonhp
        robersonhp = robersonhp - dmg_dealt
        dmgthisturn = dmg_dealt
        dmg_dealt = 0
        current_prof = "Dr. Roberson"


    window2.destroy() 
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You dealt {dmgthisturn} damage to {current_prof} with slap!') #so we dont have to repeat code, we decide the damage in smaller loops, and save the prof name to put it here
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="I feel horrible.")
    if current_fight == 1:   #sorts again by professor
        if burkehp > 0:
            NObutton.bind("<Button-1>",burkestage2)
        else: #if you did the final amount of damage, go to defeat, this is true for all profs
            NObutton.bind("<Button-1>",burkedefeat)
    elif current_fight == 2:
        if cazalashp > 0:
            NObutton.bind("<Button-1>",cazalasstage2)
        else:
            NObutton.bind("<Button-1>",cazalasdefeat)
    elif current_fight == 3:
        if lewishp > 0:
            NObutton.bind("<Button-1>",lewisstage2)
        else:
            NObutton.bind("<Button-1>",lewisdefeat)
    elif current_fight == 4:
        if eicholtzhp > 0:
            NObutton.bind("<Button-1>",eicholtzstage2)
        else:
            NObutton.bind("<Button-1>",eicholtzdefeat)
    elif current_fight == 5:
        if robersonhp > 0:
            NObutton.bind("<Button-1>",robersonstage2)
        else:
            NObutton.bind("<Button-1>",robersondefeat)
    NObutton.grid(column=0,row=1)

def powernap(event):
    global hp
    global current_fight
    global window2
    global atkpower
    window2.destroy()
    window2 = tkinter.Tk()
    hp = hp + (atkpower * 1.5) #gives you a stat increase
    label1 = tkinter.Label(window2)
    label1.configure(text=f'you replenished some health!')
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="phew.")
    if current_fight == 1: #sorts you out by which fight youre in and goes to their turn
        NObutton.bind("<Button-1>",burkestage2)
    if current_fight == 2:
        NObutton.bind("<Button-1>",cazalasstage2)
    if current_fight == 3:
        NObutton.bind("<Button-1>",lewisstage2)
    if current_fight == 4:
        NObutton.bind("<Button-1>",eicholtzstage2)
    if current_fight == 5:
        NObutton.bind("<Button-1>",robersonstage2)
    NObutton.grid(column=0,row=1)

def outcode(event):
    global atkpower
    global window2
    global current_fight
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'you literally cant outcode ur professor, stay humble.')
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="you know what? makes sense.")
    if current_fight == 1: #no stat increase given, same sorting as powernap to decide that you go back to fight you were in
        NObutton.bind("<Button-1>",burkestage2)
    if current_fight == 2:
        NObutton.bind("<Button-1>",cazalasstage2)
    if current_fight == 3:
        NObutton.bind("<Button-1>",lewisstage2)
    if current_fight == 4:
        NObutton.bind("<Button-1>",eicholtzstage2)
    if current_fight == 5:
        NObutton.bind("<Button-1>",robersonstage2)
    NObutton.grid(column=0,row=1)

def thinkattack(event):
    global atkpower
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    atkpower = atkpower * 1.5
    label1 = tkinter.Label(window2)
    label1.configure(text=f'you increased your power!')
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="Sick")
    if current_fight == 1: #stat increase similar to powernap, and then pushes you to the other persons fight since you definitely did not do damage
        NObutton.bind("<Button-1>",burkestage2)
    if current_fight == 2:
        NObutton.bind("<Button-1>",cazalasstage2)
    if current_fight == 3:
        NObutton.bind("<Button-1>",lewisstage2)
    if current_fight == 4:
        NObutton.bind("<Button-1>",eicholtzstage2)
    if current_fight == 5:
        NObutton.bind("<Button-1>",robersonstage2)
    NObutton.grid(column=0,row=1)

def multislap(event):
    global atkpower
    global window2
    global current_fight
    dmg_dealt = 1 + atkpower
    if current_fight == 5: #only allowed in roberson fight
        global robersonhp
        dmgthisturn = 0
        while True:
            chance_of_hit = random.randint(1,4) #you have a 1/4 chance of hitting, will repeat until misses
            if chance_of_hit == 1:
                break #breaks if misses
            else:
                robersonhp = robersonhp - dmg_dealt
                dmgthisturn += dmg_dealt
                dmg_dealt = 0
    current_prof = "Dr. Roberson"
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You dealt {dmgthisturn} damage to {current_prof} with multislap!')
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="I feel horrible, multiple times.")
    if current_fight == 5:    
        if robersonhp > 0:
            NObutton.bind("<Button-1>",robersonstage2) #pushes you back to robersons turn if he was not defeated here
        else:
            NObutton.bind("<Button-1>",robersondefeat) #if you defeated him here, push to that.
    NObutton.grid(column=0,row=1)





def burkestage1(event):
    global window2
    global player_name
    global hp
    global current_fight
    global burkehp
    current_fight = 1 #sets current fight at 1 will with be referenced in attacks.
    window2.destroy()
    window2=tkinter.Tk() #destroys old window makes a new one
    if hp > 0: #checks if you have enough HP to make an action
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Ra I am doctor burke and you will feel my wrath!')
        label1.grid(column=0,row=0)
        label2 = tkinter.Label(window2)
        label2.configure(text=f'Burke current HP = {burkehp}') #displays burke hp
        label2.grid(column=1,row=0)
        slapbutton = tkinter.ttk.Button(window2, text="slap!")
        slapbutton.bind("<Button-1>",slap) #will use slap attack
        slapbutton.grid(column=0,row=1)
        thinkbutton = tkinter.ttk.Button(window2, text="think")
        thinkbutton.bind("<Button-1>",thinkattack) #will go to think attack
        thinkbutton.grid(column=0,row=2) 
        label3 = tkinter.Label(window2)
        if hp < 10: #if you have low hp
            label3.configure(text =f'{player_name}\'s Current HP = {hp}', foreground= 'red')#makes your name red if you have low hp
        label3.configure(text=f'{player_name}\'s Current HP = {hp}') 
        label3.grid(column=1, row=1)
    else: #if you have no hp left, you lose, and will have to try again. you must close window here and restart
        label1 = tkinter.Label(window2) 
        label1.configure(text=f'Dr. Burke went bananas try again.')
        label1.grid(column=0,row=0)

def burkestage2(event):
    burkeatknum = random.randint(1,3)  #decides at random which attack burke will use
    global window2
    global hp
    global burkeatk #grabs burke atk num from starting stats function previously
    window2.destroy() 
    window2 = tkinter.Tk()
    if burkeatknum == 1:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Burke uses fireball') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1: #you have a 1/10 chance to dodge
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!") 
            NObutton.bind("<Button-1>",burkestage1)#you take no damage and go back to your turn
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - burkeatk #this attack just does damage equal to burkes attack
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take {burkeatk} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="Ouch!")
            NObutton.bind("<Button-1>",burkestage1) #brings you back after you take damage
            NObutton.grid(column=0,row=2)
    elif burkeatknum == 2:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Burke uses Banana Bullseye!!!!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1: #you once again have a 1/10 chance to dodge
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!")
            NObutton.bind("<Button-1>",burkestage1) #will take no damage and be brought back to your turn.
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - (burkeatk * 2) #this will do double burkes attack damage
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take {burkeatk * 2} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="Ouch!")
            NObutton.bind("<Button-1>",burkestage1) #you go back to your turn
            NObutton.grid(column=0,row=2)
    elif burkeatknum == 3:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Burke uses tall mode!!!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1: #1/10 chance to fail rather than dodge, since it would not do damage to you
            label2 = tkinter.Label(window2)
            label2.configure(text=f'He fails!') 
            label2.grid(column=0,row=1)
            burkeatk = burkeatk - 1 #he loses some stats for failing
            NObutton = tkinter.ttk.Button(window2, text="good for me.")
            NObutton.bind("<Button-1>",burkestage1) #back to user turn
            NObutton.grid(column=0,row=2)
        else:
            burkeatk = burkeatk * 2 #doubles burkes attack permanently
            label2 = tkinter.Label(window2)
            label2.configure(text=f'Dr. Burke is so tall!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="Oh no he got stronger!")
            NObutton.bind("<Button-1>",burkestage1) #goes back to your turn
            NObutton.grid(column=0,row=2)

def burkedefeat(event):
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You have defeated me, congratulations, but it only gets more difficult from here.') #after defeating burke
    label1.grid(column=0,row=0)
    Nextbutton = tkinter.ttk.Button(window2, text="aweeee man")
    Nextbutton.bind("<Button-1>",level2screen) #going to level 2
    Nextbutton.grid(column=0,row=2)



def level2screen(event):
    global window2
    global player_name #if you want to reference player name on this screen
    global hp
    global atkpower
    atkpower = 4
    hp = 20 #updates user stats to make the game progress
    window2.destroy()
    window2=tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'Congratulations! you have gotten stronger and added a new ability!')
    label1.grid(column=0,row=0)
    label1 = tkinter.Label(window2)
    label1.configure(text=f'Which ability would you like?')
    label1.grid(column=0,row=1) #gives two button options, one to give you a certain ability that you will keep for the rest of the game
    getability1button = tkinter.ttk.Button(window2, text="outcode")
    getability1button.bind("<Button-1>",getoutcode) #runs a function to set your ability3 num 
    getability1button.grid(column=0,row=2)
    getability2button = tkinter.ttk.Button(window2, text="power nap!")
    getability2button.bind("<Button-1>",getpowernap) #runs a function to set your abiliy3 num
    getability2button.grid(column=0,row=3)

def getoutcode(event):
    global ability3
    ability3 = 1 #this function just sets your ability3 num to be referenced later, pushes you to cazalas
    cazalasstage1(event)

def getpowernap(event):
    global ability3
    ability3 = 2 #this function just sets your ability3 num to be referenced later, pushes you to cazalas
    cazalasstage1(event)



def cazalasstage1(event):
    global window2
    global player_name
    global hp
    global current_fight
    global cazalashp
    global ability3
    global atkpower
    global basehp
    if current_fight == 1: #this shows if you can from the last fight, and will reset your stats for you!
        hp = basehp
        atkpower = 4
    current_fight = 2 #now sets it as 2 so you will not be reset mid fight
    window2.destroy()
    window2=tkinter.Tk()
    if hp > 0:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'My name is Dr. Cazalas and this is the saints year.')
        label1.grid(column=0,row=0)
        label2 = tkinter.Label(window2)
        label2.configure(text=f'Cazalas current HP = {cazalashp}')
        label2.grid(column=1,row=0)
        slapbutton = tkinter.ttk.Button(window2, text="slap!")
        slapbutton.bind("<Button-1>",slap)
        slapbutton.grid(column=0,row=1)
        thinkbutton = tkinter.ttk.Button(window2, text="think")
        thinkbutton.bind("<Button-1>",thinkattack)
        thinkbutton.grid(column=0,row=2)
        if ability3 == 1: #everything above this line is the same as burke except
            ability3button = tkinter.ttk.Button(window2, text ="out code!")
            ability3button.bind("<Button-1>",outcode) #we have different abilities here based on what you picked
            ability3button.grid(column=1, row = 2)
        elif ability3 == 2: #the ability3 num is referenced to know which you picked previously, deciding which will be on the screen.
            ability3button = tkinter.ttk.Button(window2, text ="powernap")
            ability3button.bind("<Button-1>",powernap)
            ability3button.grid(column=1, row = 2)
        label3 = tkinter.Label(window2)
        if hp < 10:
            label3.configure(text =f'{player_name}\'s Current HP = {hp}', foreground= 'red')
        label3.configure(text=f'{player_name}\'s Current HP = {hp}')
        label3.grid(column=1, row=1)
    else:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Cazalas kicked the ball on you. Try again.')
        label1.grid(column=0,row=0)

def cazalasstage2(event): #same overall concept as burke, just the exact numbers on how much damage or stat increases are different.
    cazalasatknum = random.randint(1,3) 
    global window2
    global hp
    global cazalasatk
    window2.destroy() 
    window2 = tkinter.Tk()
    if cazalasatknum == 1:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Cazalas used kick the ball') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!")
            NObutton.bind("<Button-1>",cazalasstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - cazalasatk
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take {cazalasatk} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="ouch!")
            NObutton.bind("<Button-1>",cazalasstage1)
            NObutton.grid(column=0,row=2)
    elif cazalasatknum == 2:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Cazalas uses Touchdown!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!")
            NObutton.bind("<Button-1>",cazalasstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - 6
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take 6 damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="Ouch!")
            NObutton.bind("<Button-1>",cazalasstage1)
            NObutton.grid(column=0,row=2)
    elif cazalasatknum == 3:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Cazalas used Trip to New Orleans') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'He doesn\'t make it there!') 
            label2.grid(column=0,row=1)
            cazalasatk = cazalasatk - 1
            NObutton = tkinter.ttk.Button(window2, text="awe.")
            NObutton.bind("<Button-1>",cazalasstage1)
            NObutton.grid(column=0,row=2)
        else:
            cazalasatk = cazalasatk * 2
            label2 = tkinter.Label(window2)
            label2.configure(text=f'damn. he made it.') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="damn I hate it here.")
            NObutton.bind("<Button-1>",cazalasstage1)
            NObutton.grid(column=0,row=2)

def cazalasdefeat(event): #cazalas end screen
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You have quite literally kicked the ball on me, great job') 
    label1.grid(column=0,row=0)
    label2 = tkinter.Label(window2)
    label2.configure(text=f'Your stats increase!')#actually happens in lewis stage 1
    label2.grid(column=0,row=1)
    Nextbutton = tkinter.ttk.Button(window2, text="awesome.")
    Nextbutton.bind("<Button-1>",lewisstage1) #will go to lewis now
    Nextbutton.grid(column=0,row=2)




def lewisstage1(event): #same exact stage 1 aside from custom changes to differetiate cazalas and lewis, you have the same options.
    global window2
    global player_name
    global hp
    global current_fight
    global lewishp
    global ability3
    global atkpower
    global basehp
    if current_fight == 2: #this is the stat increase from cazalasdefeat
        hp = basehp + 5
        atkpower = 5
    current_fight = 3
    window2.destroy()
    window2=tkinter.Tk()
    if hp > 0:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'My name is Dr. Lewis and I I used to be a cop.')
        label1.grid(column=0,row=0)
        label2 = tkinter.Label(window2)
        label2.configure(text=f'Lewis current HP = {lewishp}')
        label2.grid(column=1,row=0)
        slapbutton = tkinter.ttk.Button(window2, text="slap!")
        slapbutton.bind("<Button-1>",slap)
        slapbutton.grid(column=0,row=1)
        thinkbutton = tkinter.ttk.Button(window2, text="think")
        thinkbutton.bind("<Button-1>",thinkattack)
        thinkbutton.grid(column=0,row=2)
        if ability3 == 1:
            ability3button = tkinter.ttk.Button(window2, text ="out code!")
            ability3button.bind("<Button-1>",outcode)
            ability3button.grid(column=1, row = 2)
        elif ability3 == 2:
            ability3button = tkinter.ttk.Button(window2, text ="powernap")
            ability3button.bind("<Button-1>",powernap)
            ability3button.grid(column=1, row = 2)
        label3 = tkinter.Label(window2)
        if hp < 10:
            label3.configure(text =f'{player_name}\'s Current HP = {hp}', foreground= 'red')
        label3.configure(text=f'{player_name}\'s Current HP = {hp}')
        label3.grid(column=1, row=1)
    else:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Lewis Arrested you, try again.')
        label1.grid(column=0,row=0)

def lewisstage2(event):
    cazalasatknum = 1
    global window2
    global hp
    global lewisatk
    global lewishp
    window2.destroy() 
    window2 = tkinter.Tk()
    if lewishp < 10: #lewis attack pattern is different, he uses an attack based on the amount of health he has left
        cazalasatknum = 2
    if lewishp < 5:
        cazalasatknum = 3
    if cazalasatknum == 1: #dog bit will be used if he has more than 10 hp
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Lewis used dog bite!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10) #dodge mechanic still present.
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - lewisatk
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take {lewisatk} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="ouch!")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)
    elif cazalasatknum == 2: #if lewis has between 5 and 10 hp, but not including 5
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Lewis uses cybersecure!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'he messed up his code') 
            label2.grid(column=0,row=1)
            lewisatk = lewisatk - 3
            NObutton = tkinter.ttk.Button(window2, text="thats tough for him.")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)
        else:
            lewishp = lewishp + 4
            label2 = tkinter.Label(window2)
            label2.configure(text=f'man he did it, he got some hp') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="that stinks.")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)
    elif cazalasatknum == 3: #if lewis has less than 5 hp but more than 0, he will use this
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Lewis used the big bad move') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,5) #much higher chance to dodge
        if dodgenum != 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'wow it missed that was close') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="yeesh.")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - 10000000 #effectively ends the game if you do not dodge.
            label2 = tkinter.Label(window2)
            label2.configure(text=f'you died.') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="man.")
            NObutton.bind("<Button-1>",lewisstage1) #even though you are guarantee lost, you go back to stage1 which checks your hp
            NObutton.grid(column=0,row=2)

def lewisdefeat(event):
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'damn thats so crazy even tho i had a dog')
    label1.grid(column=0,row=0)
    label2 = tkinter.Label(window2)
    label2.configure(text=f'your stats increase!')
    label2.grid(column=0,row=1)
    Nextbutton = tkinter.ttk.Button(window2, text="yea for sure.")
    Nextbutton.bind("<Button-1>", eicholtzstage1) #onto eicholtz, these defeat screens are the same
    Nextbutton.grid(column=0,row=2)




def eicholtzstage1(event): #same as past 2 stage1s
    global window2
    global player_name
    global hp
    global current_fight
    global eicholtzhp
    global ability3
    global atkpower
    global basehp
    if current_fight == 3: #same mechanic for stat increases, nothing new here at all
        hp = basehp + 10
        atkpower = 7
    current_fight = 4
    window2.destroy()
    window2=tkinter.Tk()
    if hp > 0:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'My name is Dr. Eicholtz and I am a robot')
        label1.grid(column=0,row=0)
        label2 = tkinter.Label(window2)
        label2.configure(text=f'Eicholtz current HP = {eicholtzhp}')
        label2.grid(column=1,row=0)
        slapbutton = tkinter.ttk.Button(window2, text="slap!")
        slapbutton.bind("<Button-1>",slap)
        slapbutton.grid(column=0,row=1)
        thinkbutton = tkinter.ttk.Button(window2, text="think")
        thinkbutton.bind("<Button-1>",thinkattack)
        thinkbutton.grid(column=0,row=2)
        if ability3 == 1:
            ability3button = tkinter.ttk.Button(window2, text ="out code!")
            ability3button.bind("<Button-1>",outcode)
            ability3button.grid(column=1, row = 2)
        elif ability3 == 2:
            ability3button = tkinter.ttk.Button(window2, text ="powernap")
            ability3button.bind("<Button-1>",powernap)
            ability3button.grid(column=1, row = 2)
        label3 = tkinter.Label(window2)
        if hp < 10:
            label3.configure(text =f'{player_name}\'s Current HP = {hp}', foreground= 'red')
        label3.configure(text=f'{player_name}\'s Current HP = {hp}')
        label3.grid(column=1, row=1)
    else:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Eicholtz smoked you, try again.')
        label1.grid(column=0,row=0)

def eicholtzstage2(event): #he goes back to the previous attack patterns of randomness, otherwise same code again.
    burkeatknum = random.randint(1,3) 
    global window2
    global hp
    global eicholtzatk
    global eicholtzhp
    window2.destroy() 
    window2 = tkinter.Tk()
    if burkeatknum == 1:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Eicholtz uses robot!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!")
            NObutton.bind("<Button-1>",eicholtzstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - eicholtzatk
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take {eicholtzatk} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="ouch!")
            NObutton.bind("<Button-1>",eicholtzstage1)
            NObutton.grid(column=0,row=2)
    elif burkeatknum == 2:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Eicholtz runs a route on you!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,5)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'you swatted it.') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="thats the no fly zone for you.")
            NObutton.bind("<Button-1>",eicholtzstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - (eicholtzatk * 1.25)
            label2 = tkinter.Label(window2)
            label2.configure(text=f'HE MOSSES YOU!!! out of embarrassment you take {eicholtzatk * 1.25} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="wheres the flag??")
            NObutton.bind("<Button-1>",eicholtzstage1)
            NObutton.grid(column=0,row=2)
    elif burkeatknum == 3:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Eicholtz uses seminar') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'nobody shows up!') 
            label2.grid(column=0,row=1)
            burkeatk = burkeatk - 1
            NObutton = tkinter.ttk.Button(window2, text="should have made it a passport event")
            NObutton.bind("<Button-1>",eicholtzstage1)
            NObutton.grid(column=0,row=2)
        else:
            eicholtzatk = eicholtzatk * 1.5
            eicholtzhp += 7
            label2 = tkinter.Label(window2)
            label2.configure(text=f'he steals the brainpower of all the kids!! doubling his power and giving some hp!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="WHAT??")
            NObutton.bind("<Button-1>",eicholtzstage1)
            NObutton.grid(column=0,row=2)

def eicholtzdefeat(event):
    global window2
    global player_name
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'thats ok {player_name}, just show up to the next IM game.')
    label1.grid(column=0,row=0)
    label2 = tkinter.Label(window2)
    label2.configure(text=f'your stats increase!')
    label2.grid(column=0,row=1)
    Nextbutton = tkinter.ttk.Button(window2, text="you bet dude.")
    Nextbutton.bind("<Button-1>", robersonstage1) #pushes to the last fight with roberson
    Nextbutton.grid(column=0,row=2)




def robersonstage1(event): #same as other stage1s with one new added ability
    global window2
    global player_name
    global hp
    global current_fight
    global robersonhp
    global ability3
    global atkpower
    global basehp
    if current_fight == 4:
        hp = basehp + 15
        atkpower = 10
    current_fight = 5
    window2.destroy()
    window2=tkinter.Tk()
    if hp > 0:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Muahahaha it is me Dr. Roberson the final boss')
        label1.grid(column=0,row=0)
        label2 = tkinter.Label(window2)
        label2.configure(text=f'Dr. Roberson current HP = {robersonhp}')
        label2.grid(column=1,row=0)
        slapbutton = tkinter.ttk.Button(window2, text="slap!")
        slapbutton.bind("<Button-1>",slap)
        slapbutton.grid(column=0,row=1)
        thinkbutton = tkinter.ttk.Button(window2, text="think")
        thinkbutton.bind("<Button-1>",thinkattack)
        thinkbutton.grid(column=0,row=2)
        if ability3 == 1:
            ability3button = tkinter.ttk.Button(window2, text ="out code!")
            ability3button.bind("<Button-1>",outcode)
            ability3button.grid(column=1, row = 2)
        elif ability3 == 2:
            ability3button = tkinter.ttk.Button(window2, text ="powernap")
            ability3button.bind("<Button-1>",powernap)
            ability3button.grid(column=1, row = 2)
        label3 = tkinter.Label(window2)
        multibutton = tkinter.ttk.Button(window2, text="mutlislap") #new ability was added multislap
        multibutton.bind("<Button-1>",multislap)
        multibutton.grid(column=0,row=3)
        if hp < 10:
            label3.configure(text =f'{player_name}\'s Current HP = {hp}', foreground= 'red')
        label3.configure(text=f'{player_name}\'s Current HP = {hp}')
        label3.grid(column=1, row=1)
    else:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Roberson wins. Try again.')
        label1.grid(column=0,row=0)

def robersonstage2(event):
    burkeatknum = random.randint(1,3) #displays same exact attack pattern for randomness for burke original fight, but some numbers are changed on what they do, otherwise is a carbon copy
    global window2
    global hp
    global robersonatk
    global robersonhp
    window2.destroy() 
    window2 = tkinter.Tk()
    if burkeatknum == 1:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Roberson uses the force') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!")
            NObutton.bind("<Button-1>",robersonstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - robersonatk
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take {robersonatk} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="ouch!")
            NObutton.bind("<Button-1>",robersonstage1)
            NObutton.grid(column=0,row=2)
    elif burkeatknum == 2:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Roberson gives you a bad grade') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,5)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You did a makeup assignment') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="awesome.")
            NObutton.bind("<Button-1>",robersonstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - (robersonatk * 1.25)
            label2 = tkinter.Label(window2)
            label2.configure(text=f'that sucks, you take {robersonatk * 1.25} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="this class is literally completion how.")
            NObutton.bind("<Button-1>",robersonstage1)
            NObutton.grid(column=0,row=2)
    elif burkeatknum == 3:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Roberson uses boss') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It fails!') 
            label2.grid(column=0,row=1)
            burkeatk = burkeatk - 1
            NObutton = tkinter.ttk.Button(window2, text="great!")
            NObutton.bind("<Button-1>",robersonstage1)
            NObutton.grid(column=0,row=2)
        else:
            robersonatk = robersonatk * 1.5
            robersonhp += 7
            label2 = tkinter.Label(window2)
            label2.configure(text=f'He gets stronger!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="WHAT??")
            NObutton.bind("<Button-1>",robersonstage1)
            NObutton.grid(column=0,row=2)

def robersondefeat(event):
    global window2
    global player_name
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'{player_name}, you should have known I was not behind this,') #the big twist foreshadowing
    label1.grid(column=0,row=0)
    label2 = tkinter.Label(window2)
    label2.configure(text=f'what do you mean?')
    label2.grid(column=0,row=1)
    Nextbutton = tkinter.ttk.Button(window2, text="oh no.")
    Nextbutton.bind("<Button-1>", bigtwist)
    Nextbutton.grid(column=0,row=2)




def bigtwist(event):
    global window2
    global player_name
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'{player_name}, it was I, Adele') #i dont know why adele, can be any name
    label1.grid(column=0,row=0)
    label2 = tkinter.Label(window2)
    label2.configure(text=f'I should have known!')
    label2.grid(column=0,row=1)
    Nextbutton = tkinter.ttk.Button(window2, text="oh no.")
    Nextbutton.bind("<Button-1>", endingscene) #brings you to final 'fight' with adele
    Nextbutton.grid(column=0,row=2)

def endingscene(event):
    global window2
    global player_name
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'Jokes on you Adele, its about the friends you make along the way') #you striking back
    label1.grid(column=0,row=0)
    Nextbutton = tkinter.ttk.Button(window2, text="Use the big bad move")
    Nextbutton.bind("<Button-1>", finale) #brings you to the final window
    Nextbutton.grid(column=0,row=2)

def finale(event):
    global window2
    global player_name
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You deal 100000000 damage to adele') #its just for the story, not an actual fight, so this is a hard number that just pushes the end
    label1.grid(column=0,row=0)
    Nextbutton = tkinter.ttk.Button(window2, text="finish the game")
    Nextbutton.bind("<Button-1>", over) #will close final window
    Nextbutton.grid(column=0,row=2)

def over(event):
    global window2 #closes the final window
    window2.destroy()





def nameconfirmed(event):
    global window1
    global window2
    global player_name
    window2.destroy()
    global hp
    global basehp
    basehp = hp
    if player_name == "Dr. Roberson": #if you are Dr. Roberson it will ask why you want to fight yourself, I just thought this would be funny, name must be exact
        window2=tkinter.Tk()
        label1 = tkinter.Label(window2)
        label1.configure(text=f'DR. ROBERSON???? this makes no sense!!! why would you fight yourself???')
        label1.grid(column=0,row=0)
        NObutton = tkinter.ttk.Button(window2, text="You caught me!")
        NObutton.bind("<Button-1>",namewindow) #makes you choose a name that is not Dr. Roberson
        NObutton.grid(column=0,row=1)
    else:
        window2=tkinter.Tk()
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Okay {player_name}, here\'s the deal, we have to get past Dr. Roberson\'s minions before we can challenge him!')
        label1.grid(column=0,row=0)
        label2 = tkinter.Label(window2)
        label2.configure(text=f'First up is Dr. Burke!!!!!') #more text
        label2.grid(column=0,row=1)
        NObutton = tkinter.ttk.Button(window2, text="I'm ready!")
        NObutton.bind("<Button-1>",burkestage1) #will bring us to the first fight stage.
        NObutton.grid(column=0,row=2)

def namesubmitted(event):
    
    global player_name
    global label1
    global window2
    global username
    player_name = username.get() #gets the username that the player submitted, saves it into a usable variable.
    window1.destroy() #destroys previous window
    window2 =tkinter.Tk() #creates new window

    label1 = tkinter.Label(window2)
    label1.configure(text=f'your name is {player_name}?') #confirms your name and shows it back to you
    label1.grid(column=0,row=0)
    YESbutton = tkinter.ttk.Button(window2, text="YES")
    YESbutton.bind("<Button-1>",nameconfirmed) #will continue with the game
    YESbutton.grid(column=0,row=1)
    NObutton = tkinter.ttk.Button(window2, text="NO")
    NObutton.bind("<Button-1>",namewindow) #brings you back to name window to re input name
    NObutton.grid(column=0,row=2)
    
def back(event):
    global window2
    global window1
    window1.destroy()

    window2 = tkinter.Tk()
    window2.title("FSC GAME")

    window2label1 = tkinter.Label(window2, text = "Welcome to the game, but this is not a game, Dr. Roberson is really a robot and is going to boil the students alive in the secret basement, and it is up to you to stop him!")
    window2label1.grid(column=0,row=0)

    ohnobutton = tkinter.ttk.Button(window2, text="Oh no!")
    ohnobutton.bind("<Button-1>",namewindow)
    ohnobutton.grid(column=0,row=1)

def namewindow(event):
    global window1 #this is so we can use the window again
    window1 = tkinter.Tk()

    global label1 #overrides the previous label
    label1 = tkinter.Label(window1, text = "What is your name?")
    label1.grid(column=0,row=0)
    global player_name
    global username 

    username = tkinter.Entry(window1) #entry prompts for user entry
    username.grid(column=0,row=1)
    

    entername = tkinter.ttk.Button(window1, text="Submit name")
    entername.bind("<Button-1>", namesubmitted) #uses function that will read the user input
    entername.grid(column=0,row=2)
    global window2
    window2.destroy() #destroys previous window

def main():
    startingstats() #runs starting stats if i ever want to add something to bring you back to the beginning
    global window1
    global label1
    window1 = tkinter.Tk() #creates the window
    window1.title("FSC GAME") #puts a title on the window

    label = tkinter.Label(window1, text="Welcome to FSC game!") #first label welcoming to the game
    label.grid(column=0, row=0) #places it on the grid

    label1 = tkinter.Label(window1)
    label1.configure(text=f'Current HP = {hp}') #displays current HP to start which can be changed below
    label1.grid(column=0, row=1)

    custom_button = tkinter.ttk.Button(window1, text="Add 1 to HP") #text on button
    custom_button.bind("<Button-1>", clicked) #uses clicked function, adding 1 to hp
    custom_button.grid(column=1, row=0)

    custom_button2 = tkinter.ttk.Button(window1, text="Open game") #starts the game
    custom_button2.bind("<Button-1>", back)
    custom_button2.grid(column=2, row=0)


    window1.mainloop() #mainloop is used to keep it updating when 'clicked' is used.

main() # uses the main function, starts the program