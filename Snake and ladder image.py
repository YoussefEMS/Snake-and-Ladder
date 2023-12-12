from tkinter import *
import tkinter as tk 
from tkinter import messagebox
from PIL import ImageTk,Image,ImageSequence
import time
import random

root = tk.Tk()
#Creating Game title
root.title("Snake and Ladder game")
#Creating Game icon
root.iconbitmap("C:\Game\SnakeLadder.ico")
#Set Dimensions
root.geometry("1200x800")
#Set Game Board
F1= tk.Frame(root, width=1200, height=800, relief='raised').place(x=0,y=0)
#Set Position difference to zero
Position_Diff=0


GameBoard=ImageTk.PhotoImage(Image.open("C:\Game\GameBoard.png"))
Lab= tk.Label(F1, image=GameBoard).place(x=0, y=0)



#Creating Welcome Message
def Welcome_Message():
    messagebox.showinfo(title="Welcome to Snake and Ladder!", message="Welcome to our game We hope you have lots of fun!")
Welcome_Message()
#Creating Board

label1=Label(root)
#Creating the dice
DiceList=["C:\DiceList\Dice1.png", "C:\DiceList\Dice2.png", "C:\DiceList\Dice3.png", "C:\DiceList\Dice4.png", "C:\DiceList\Dice5.png", "C:\DiceList\Dice6.png"]
#Initializing Object start position at zero
Object_Position=0
#Creating function to get the animation of rolling a dice
def gif():
    global DiceGIF 
    DiceGIF=Image.open("C:\DiceList\Dice.gif")
    lb1= Label(root)
    lb1.after(2500,lb1.destroy)
    for DiceGIF in ImageSequence.Iterator(DiceGIF):
        DiceGIF=ImageTk.PhotoImage(DiceGIF)
        lb1.config(image=DiceGIF)
        root.update()
        time.sleep(0.01)
        root.after(1, diceimg)
#creating the function of the dice itself randomizing
        
def diceimg():
    global Position_Diff
    Position_Diff=0
    path=random.choice(DiceList)
    Position_Diff=(DiceList.index(path))+1
    DiceImage= ImageTk.PhotoImage(Image.open(path))
    label1.place(x=975, y=300)
    label1.configure(image=DiceImage)
    label1.image = DiceImage
    time.sleep(0.03)
ButtonPlayer1=Button(root, text="Player1", height=7, width=30, bg='red', command=gif).place(x=775,y=500)
ButtonPlayer2=Button(root, text="Player2", height=7, width=30, bg='blue', command=gif).place(x=1075, y=500)
Object_Position = Object_Position + Position_Diff



root.mainloop()
