import tkinter
from tkinter import ttk
import random
#test
hp = 20
atkpower = 3
burkehp = 10
burkeatk = 4
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
        current_prof = "Dr. Burke!"


    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You dealt {dmgthisturn} damage to {current_prof} with slap!')
    label1.grid(column=0,row=0)
    NObutton = tkinter.ttk.Button(window2, text="I feel horrible.")
    if burkehp > 0:
        NObutton.bind("<Button-1>",burkestage2)
    else:
        NObutton.bind("<Button-1>",burkedefeat)
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
    NObutton.bind("<Button-1>",burkestage2)
    NObutton.grid(column=0,row=1)
def burkestage2(event):
    burkeatknum = random.randint(1,3) 
    global window2
    global hp
    window2.destroy() 
    if burkeatknum == 1:
        window2 = tkinter.Tk()
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


        

        


def burkedefeat(event):
    global window2
    window2.destroy()
    window2 = tkinter.Tk()
    label1 = tkinter.Label(window2)
    label1.configure(text=f'You have defeated me, congradulations, but it only gets more difficult from here.')
    label1.grid(column=0,row=0)



def nameconfirmed(event):
    global window1
    global window2
    global player_name
    window2.destroy()
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
    label3.configure(text=f'Current HP = {hp}')
    label3.grid(column=1, row=1)

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
