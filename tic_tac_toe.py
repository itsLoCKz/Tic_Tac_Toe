# Tic-Tac-Toe by Adam Szcześniak

from tkinter import *
import random
import ctypes
import platform

def set_titlebar_color(window, color):
    system = platform.system().lower()
    if system == "windows" and ctypes.windll.user32:
        ctypes.windll.user32.SetSysColors(1, (ctypes.c_int * 3)(15, color, color))

def next_turn(row, column):
    
    global player
    
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        if player == players[0]:
            
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[1]
                label.config(text=("Turn of " + players[1]))
            
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        
        else:

            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=("Turn of " + player[0]))
            
            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))
            
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))


def check_winner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif empty_spaces() is False:
        
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else:
        return False

def empty_spaces():
     
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else: 
        return True

def new_game():
    global player

    player = random.choice(players)

    label.config(text="Turn of " + player)

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#231e2e", fg="white", highlightbackground="#1a1625")


window = Tk()
window.title("   Tic-Tac-Toe by Adam Szcześniak")
window.configure(bg="#1a1625")
window.tk_setPalette(background="#1a1625", foreground="white")
set_titlebar_color(window, 0x1a1625)

# Icon made by Pixel perfect from www.flaticon.com
window.iconbitmap("tic-tac-toe.1024x1024.ico")

players = ["X","O"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text="Turn of " + player, font=("Arial",40))
label.pack()

reset_button = Button(text="restart", font=("Arial",20), command=new_game, borderwidth=2, relief="ridge")
reset_button.pack(pady=10)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame,
            text="",
            font=("Arial", 40),
            width=5,
            height=2,
            command=lambda row=row, column=column: next_turn(row, column),
            bg="#231e2e",  
            fg="white",  
            highlightbackground="#1a1625",  
            borderwidth=2, 
            relief="ridge",  
        )
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
