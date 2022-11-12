import tkinter
from tkinter import ttk
import random
#test
hp = 20
atkpower = 3
burkehp = 10
burkeatk = 4
cazalashp = 15
cazalasatk = 6
lewishp = 20
lewisatk = 8
def clicked(event):
    global hp
    hp = hp + 1
    label1.configure(text=f'Current HP = {hp}')
def slap(event):
    global atkpower
    global window2
    dmg_dealt = 1 + atkpower
    if current_fight == 1:
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


    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You dealt {dmgthisturn} damage to {current_prof} with slap!')
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="I feel horrible.")
    if current_fight == 1:    
        if burkehp > 0:
            NObutton.bind("<Button-1>",burkestage2)
        else:
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
    NObutton.grid(column=0,row=1)
def powernap(event):
    global hp
    global current_fight
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    hp += 5
    label1 = tkinter.Label(window2)
    label1.configure(text=f'you replenished some health!')
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="oh W")
    if current_fight == 1:
        NObutton.bind("<Button-1>",burkestage2)
    if current_fight == 2:
        NObutton.bind("<Button-1>",cazalasstage2)
    if current_fight == 3:
        NObutton.bind("<Button-1>",lewisstage2)
    NObutton.grid(column=0,row=1)
def outcode(event):
    global atkpower
    global window2
    global current_fight
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'you literally cant outcode ur prof, stay humble.')
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="you know what? valid.")
    if current_fight == 1:
        NObutton.bind("<Button-1>",burkestage2)
    if current_fight == 2:
        NObutton.bind("<Button-1>",cazalasstage2)
    if current_fight == 3:
        NObutton.bind("<Button-1>",lewisstage2)
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
    NObutton = tkinter.ttk.Button(window2, text="Swag")
    if current_fight == 1:
        NObutton.bind("<Button-1>",burkestage2)
    if current_fight == 2:
        NObutton.bind("<Button-1>",cazalasstage2)
    if current_fight == 3:
        NObutton.bind("<Button-1>",lewisstage2)
    NObutton.grid(column=0,row=1)
def burkestage2(event):
    burkeatknum = random.randint(1,3) 
    global window2
    global hp
    global burkeatk
    window2.destroy() 
    window2 = tkinter.Tk()
    if burkeatknum == 1:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Burke uses fireball') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!")
            NObutton.bind("<Button-1>",burkestage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - burkeatk
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take {burkeatk} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="MAN FUCK!")
            NObutton.bind("<Button-1>",burkestage1)
            NObutton.grid(column=0,row=2)
    elif burkeatknum == 2:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Burke uses Banana Bullseye!!!!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'You dodge!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="I\'m just TOO NICE!")
            NObutton.bind("<Button-1>",burkestage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - (burkeatk * 2)
            label2 = tkinter.Label(window2)
            label2.configure(text=f'It hits! you take {burkeatk * 2} damage!') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="MAN FUCK!")
            NObutton.bind("<Button-1>",burkestage1)
            NObutton.grid(column=0,row=2)
    elif burkeatknum == 3:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Burke uses tall mode!!!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
        if dodgenum == 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'He fails!') 
            label2.grid(column=0,row=1)
            burkeatk = burkeatk - 1
            NObutton = tkinter.ttk.Button(window2, text="LMFAO")
            NObutton.bind("<Button-1>",burkestage1)
            NObutton.grid(column=0,row=2)
        else:
            burkeatk = burkeatk * 2
            label2 = tkinter.Label(window2)
            label2.configure(text=f'holy shit he just got so fucking tall') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="MAN FUCK! LOOK HOW TALL HE IS!!!! THATS BS")
            NObutton.bind("<Button-1>",burkestage1)
            NObutton.grid(column=0,row=2)


def burkedefeat(event):
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You have defeated me, congratulations, but it only gets more difficult from here.')
    label1.grid(column=0,row=0)
    Nextbutton = tkinter.ttk.Button(window2, text="aweeee man")
    Nextbutton.bind("<Button-1>",level2screen)
    Nextbutton.grid(column=0,row=2)

def cazalasdefeat(event):
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You have quite literally kicked the ball on me, great job')
    label1.grid(column=0,row=0)
    Nextbutton = tkinter.ttk.Button(window2, text="haha balls.")
    Nextbutton.bind("<Button-1>",lewisstage1)
    Nextbutton.grid(column=0,row=2)
def lewisstage1(event):
    global window2
    global player_name
    global hp
    global current_fight
    global lewishp
    global ability3
    global atkpower
    global basehp
    if current_fight == 2:
        hp = basehp
        atkpower = 5
    current_fight = 3
    window2.destroy()
    window2=tkinter.Tk()
    if hp > 0:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'My name is Dr. Lewis and I uh used to be a cop')
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
    cazalasatknum = random.randint(1,2) 
    global window2
    global hp
    global lewisatk
    global lewishp
    window2.destroy() 
    window2 = tkinter.Tk()
    if lewishp < 10:
        cazalasatknum = 3
    if cazalasatknum == 1:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Lewis used dog bite!') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,10)
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
            NObutton = tkinter.ttk.Button(window2, text="MAN FUCK!")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)
    elif cazalasatknum == 2:
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
            NObutton = tkinter.ttk.Button(window2, text="MAN FUCK!")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)
    elif cazalasatknum == 3:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Lewis used the big bad move') 
        label1.grid(column=0,row=0)
        dodgenum = random.randint(1,5)
        if dodgenum != 1:
            label2 = tkinter.Label(window2)
            label2.configure(text=f'wow it missed that was close') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="yeesh.")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)
        else:
            hp = hp - 10000000
            label2 = tkinter.Label(window2)
            label2.configure(text=f'holy shit it clapped ur cheeks for 10000000 damage.') 
            label2.grid(column=0,row=1)
            NObutton = tkinter.ttk.Button(window2, text="man shit.")
            NObutton.bind("<Button-1>",lewisstage1)
            NObutton.grid(column=0,row=2)

def lewisdefeat(event):
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'damn thats so crazy even tho i had a dog')
    label1.grid(column=0,row=0)
    Nextbutton = tkinter.ttk.Button(window2, text="yea for sure idc")
    Nextbutton.bind("<Button-1>")
    Nextbutton.grid(column=0,row=2)

def nameconfirmed(event):
    global window1
    global window2
    global player_name
    window2.destroy()
    global hp
    global basehp
    basehp = hp
    if player_name == "Dr. Roberson":
        window2=tkinter.Tk()
        label1 = tkinter.Label(window2)
        label1.configure(text=f'DR. ROBERSON???? this makes no sense!!! why would you fight yourself???')
        label1.grid(column=0,row=0)
        NObutton = tkinter.ttk.Button(window2, text="You caught me!")
        NObutton.bind("<Button-1>",namewindow)
        NObutton.grid(column=0,row=1)
    else:
        window2=tkinter.Tk()
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Okay {player_name}, here\'s the deal, we have to get past Dr. Roberson\'s minions before we can challenge him!')
        label1.grid(column=0,row=0)
        label2 = tkinter.Label(window2)
        label2.configure(text=f'First up is Dr. Burke!!!!!')
        label2.grid(column=0,row=1)
        NObutton = tkinter.ttk.Button(window2, text="I'm ready!")
        NObutton.bind("<Button-1>",burkestage1)
        NObutton.grid(column=0,row=2)
        
def burkestage1(event):
    global window2
    global player_name
    global hp
    global current_fight
    global burkehp
    current_fight = 1
    window2.destroy()
    window2=tkinter.Tk()
    if hp > 0:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Ra I am doctor burke and you will feel my wrath!')
        label1.grid(column=0,row=0)
        label2 = tkinter.Label(window2)
        label2.configure(text=f'Burke current HP = {burkehp}')
        label2.grid(column=1,row=0)
        slapbutton = tkinter.ttk.Button(window2, text="slap!")
        slapbutton.bind("<Button-1>",slap)
        slapbutton.grid(column=0,row=1)
        thinkbutton = tkinter.ttk.Button(window2, text="think")
        thinkbutton.bind("<Button-1>",thinkattack)
        thinkbutton.grid(column=0,row=2) 
        label3 = tkinter.Label(window2)
        if hp < 10:
            label3.configure(text =f'{player_name}\'s Current HP = {hp}', foreground= 'red')
        label3.configure(text=f'{player_name}\'s Current HP = {hp}')
        label3.grid(column=1, row=1)
    else:
        label1 = tkinter.Label(window2)
        label1.configure(text=f'Dr. Burke went bananas try again.')
        label1.grid(column=0,row=0)

def level2screen(event):
    global window2
    global player_name
    global hp
    global atkpower
    atkpower = 4
    hp = 20
    window2.destroy()
    window2=tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'Congratulations! you have gotten stronger and added a new ability!')
    label1.grid(column=0,row=0)
    label1 = tkinter.Label(window2)
    label1.configure(text=f'Which ability would you like?')
    label1.grid(column=0,row=1)
    getability1button = tkinter.ttk.Button(window2, text="outcode")
    getability1button.bind("<Button-1>",getoutcode)
    getability1button.grid(column=0,row=2)
    getability2button = tkinter.ttk.Button(window2, text="power nap!")
    getability2button.bind("<Button-1>",getpowernap)
    getability2button.grid(column=0,row=3)
def cazalasstage1(event):
    global window2
    global player_name
    global hp
    global current_fight
    global cazalashp
    global ability3
    global atkpower
    global basehp
    if current_fight == 1:
        hp = basehp
        atkpower = 3
    current_fight = 2
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
        label1.configure(text=f'Dr. Cazalas kicked ur balls, try again')
        label1.grid(column=0,row=0)

def cazalasstage2(event):
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
            NObutton = tkinter.ttk.Button(window2, text="MAN FUCK!")
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
            NObutton = tkinter.ttk.Button(window2, text="MAN FUCK!")
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
            NObutton = tkinter.ttk.Button(window2, text="LMFAO")
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


def getoutcode(event):
    global ability3
    ability3 = 1
    cazalasstage1(event)

def getpowernap(event):
    global ability3
    ability3 = 2
    cazalasstage1(event)

def namesubmitted(event):
    
    global player_name
    global label1
    global window2
    global username
    player_name = username.get()
    window1.destroy()
    window2 =tkinter.Tk()

    label1 = tkinter.Label(window2)
    label1.configure(text=f'your name is {player_name}?')
    label1.grid(column=0,row=0)
    YESbutton = tkinter.ttk.Button(window2, text="YES")
    YESbutton.bind("<Button-1>",nameconfirmed)
    YESbutton.grid(column=0,row=1)
    NObutton = tkinter.ttk.Button(window2, text="NO")
    NObutton.bind("<Button-1>",namewindow)
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
    global window1
    window1 = tkinter.Tk()

    global label1
    label1 = tkinter.Label(window1, text = "What is your name?")
    label1.grid(column=0,row=0)
    global player_name
    global username 

    username = tkinter.Entry(window1)
    username.grid(column=0,row=1)
    

    entername = tkinter.ttk.Button(window1, text="Submit name")
    entername.bind("<Button-1>", namesubmitted)
    entername.grid(column=0,row=2)
    global window2
    window2.destroy()


window1 = tkinter.Tk()
window1.title("FSC GAME")

label = tkinter.Label(window1, text="Welcome to FSC game!")
label.grid(column=0, row=0)

label1 = tkinter.Label(window1)
label1.configure(text=f'Current HP = {hp}')
label1.grid(column=0, row=1)

custom_button = tkinter.ttk.Button(window1, text="Add 1 to HP")
custom_button.bind("<Button-1>", clicked)
custom_button.grid(column=1, row=0)

custom_button2 = tkinter.ttk.Button(window1, text="Open game")
custom_button2.bind("<Button-1>", back)
custom_button2.grid(column=2, row=0)


window1.mainloop()
