import tkinter
from tkinter import ttk

hp = 20

def clicked(event):
    global hp
    hp = hp + 1
    label1.configure(text=f'Current HP = {hp}')

def namesubmitted(event):
    window1.destroy()
    get_name(event)
    global label1
    global window2
    global username
    window2 =tkinter.Tk()
    global player_name
    label1 = tkinter.Label(window2)
    label1.configure(text=f'your name is {player_name}?')
    label1.grid(column=0,row=0)
    
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
def get_name(event):
        global player_name
        global username
        player_name = username.get()
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
    entername.bind("<Button-1>",namesubmitted)
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
