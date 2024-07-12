from customtkinter import *
from tkinter import ttk
from tkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image
import time
import random
import os
from typing import Literal
from customtkinter import CTkToplevel
State1=NORMAL
State2=NORMAL
Mode="OneVOneH"
turn1=0
turn2=0  
Counter1=0
Counter2=0
Player1="Player1"
Player2="Player2"
set_window_scaling(1.5)
def resolve_path(file):
    return os.path.dirname(__file__) + file
def open_messagebox():
    top=CTkToplevel()
    top.attributes('-topmost', True)
    top.state('zoomed')
    top.title("Choose one of the following")
    def filemenu():
        folder = resolve_path("\\Saves\\OneVOneH")
        filelist = [fname.rstrip(".txt/n") for fname in os.listdir(folder) if fname.endswith('.txt')]
        optmenu = ttk.Combobox(top, values=filelist, state='readonly')
        optmenu.place(relx=0.3, rely=0.3)
            

        def get_selected_option(event):
            selected_option = optmenu.get()
            if selected_option!="":
                load_game(selected_option)
                Background.configure(size=(1370,900))
                top.destroy()    
        optmenu.bind('<<ComboboxSelected>>', get_selected_option)
    def NEWGAME():
        global Player1
        global Player2
        msg1 = CTkInputDialog(title="Player 1 name", text="Enter the name of the first player")
        Player1=msg1.get_input()
        while (Player1.isalpha() == False):
            msg1 = CTkInputDialog(title="Player 1 name", text="Invalid!! \n Your name should not contain numbers")
            Player1=msg1.get_input()
        msg2 = CTkInputDialog(title="Player 2 name", text="Enter the name of the second player")
        Player2=msg2.get_input()
        while (Player2.isalpha() == False):
            msg2 = CTkInputDialog(title="Player 2 name", text="Invalid!! \n Your name should not contain numbers")
            Player2=msg2.get_input()
        ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
        ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
        #Show Scores
        Player1Name=CTkLabel(root, text=Player1, font=("Arial", 17), fg_color="orange",text_color="white", anchor="center", width=100, height=30).place(x=1110, y=170)
        Player2Name=CTkLabel(root, text=Player2, font=("Arial", 17), fg_color="black",text_color="white", anchor="center", width=100, height=30).place(x=1210, y=170)
        Player1Score=CTkLabel(root, text=Counter1, font=("Arial", 20), fg_color="white", text_color="black", width=60, height=25).place(x=1200, y=200)
        Player2Score=CTkLabel(root, text=Counter2, font=("Arial", 20), fg_color="white",text_color="black", width=60, height=25).place(x=1260, y=200)
        rules()
        Background.configure(size=(1370,900))
        top.destroy()
    button_NEWGAME = CTkButton(top, text="New Game", command=NEWGAME)
    button_NEWGAME.place(relx=0.2, rely=0.6)
    button_LOAD=CTkButton(top,text="Load Game",command=filemenu )
    button_LOAD.place(relx=0.7,rely=0.6)


set_appearance_mode("dark")
set_default_color_theme("dark-blue")
x1=0
x2=50
y1=660
y2=660
#Creating Game title
root=CTk()
root.attributes('-fullscreen', True)
open_messagebox()
root.title("Snake and Ladder game")
#Creating Game icon
root.iconbitmap(resolve_path("\\Icon\\SnakeLadder.ico"))
#Set Dimensions
root.geometry("1200x800")
#progress bar
progressbar1 = CTkProgressBar(root , orientation = "horizental" , width = 100 , height= 12 , fg_color="white" , progress_color="orange" , border_width= 0 ,  corner_radius = 5 , mode = "determinate" , bg_color= "white")
progressbar1.set(0)
progressbar1.place(x = 800 , y = 300)
progressbar2 = CTkProgressBar(root , orientation = "horizental" , width = 100 , height= 12 , fg_color="white" , progress_color="black" , border_width = 0  , corner_radius = 5 , mode = "determinate" ,  bg_color= "white")
progressbar2.set(0)
progressbar2.place(x = 1100 , y = 300)
def rules():
    CTkMessagebox(title="First Rule", message="We are about to play the Game. But first Roll the dice to decide who starts",font=("Times New Roma", 20 , "bold"), icon=resolve_path("\\Icon\\GreenIntroduction.ico"), fg_color= "white", bg_color="white",text_color="black",title_color="black", icon_size=(250,300),width=320,height=210)

#Set Position difference to zero
Position_Diff=0
snakes = {68:2,
        59:18,
        46:15,
        98:13,
        52:11,
        44:22,
        64:24,
        69:33,
        95:37,
        83:39,
        87:50,
        92:51,
        94:71,
        48:9
        }
ladders = {5:23,
        62:96,
        43:77,
        8:26,
        10:49,
        19:38,
        28:53,
        21:61,
        35:47,
        47:76,
        36:57,
        54:88,
        67:86,
        70:91,
        80:99,
        72:93
        }
Background=CTkImage(light_image=Image.open(resolve_path("//Backgrounds//Background1.png")), size=(1370,700))
Lab11= CTkLabel(root, image=Background, text=None, width=1370,height=700).place(x=0, y=0)
GameBoard=CTkImage(light_image=Image.open(resolve_path("//Board//GameBoardH.png")), size=(600,600))
Lab= CTkLabel(root, image=GameBoard, text=None, width=600,height=600).place(x=100, y=50)
#Initialize Player names
# Player1Score=CTkLabel(root, text=Counter1, font=("Arial", 20), fg_color="white", text_color="black", width=60, height=25).place(x=1200, y=200)
# Player2Score=CTkLabel(root, text=Counter2, font=("Arial", 20), fg_color="white",text_color="black", width=60, height=25).place(x=1260, y=200)
def PlayerTurn():
    global turn1
    global turn2
    global State1
    global State2
    global ButtonPlayer1
    global ButtonPlayer2
    if GlobalPath1>GlobalPath2:
        State1=NORMAL
        State2=DISABLED
        turn1=20
        turn2=20
    if GlobalPath2>GlobalPath1:
        State1=DISABLED
        State2=NORMAL
        turn1=20
        turn2=20
    elif GlobalPath1==GlobalPath2:
        turn1=0
        turn2=0
    ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
    ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
def start_new_game():
    global State1
    global State2
    global coin1_position
    global coin2_position
    global Player1
    global Player2
    global ButtonPlayer1
    global ButtonPlayer2
    global x1
    global x2
    global y1
    global y2
    global Counter1
    global Counter2
    global Player1Score
    global Player2Score
    global Player1Name
    global Player2Name
    global turn1
    global turn2
    turn1=0
    turn2=0
    State1=NORMAL
    State2=DISABLED
    Counter1=0
    Counter2=0
    coin1_position=0
    coin2_position=0
    x1=0
    x2=50
    y1=660
    y2=660
    player1_coin.place(x=x1, y=y1)
    player2_coin.place(x=x2, y=y2)
    msg1 = CTkInputDialog(title="Player 1 name", text="Enter the name of the first player")
    Player1=msg1.get_input()
    while (Player1.isalpha() == False):
        msg1 = CTkInputDialog(title="Player 1 name", text="Invalid!! \n Your name should not contain numbers")
        Player1=msg1.get_input()
    msg2 = CTkInputDialog(title="Player 2 name", text="Enter the name of the second player")
    Player2=msg2.get_input()
    while (Player2.isalpha() == False):
        msg2 = CTkInputDialog(title="Player 2 name", text="Invalid!! \n Your name should not contain numbers")
        Player2=msg2.get_input()
    Player1Score=CTkLabel(root, text=Counter1, font=("Arial", 17), fg_color="white", text_color="black", width=100, height=25).place(x=1110, y=200)
    Player2Score=CTkLabel(root, text=Counter2, font=("Arial", 17), fg_color="white",text_color="black", width=100, height=25).place(x=1210, y=200)
    Player1Name=CTkLabel(root, text=Player1, font=("Arial", 17), fg_color="orange",text_color="white", anchor="center", width=100, height=30).place(x=1110, y=170)
    Player2Name=CTkLabel(root, text=Player2, font=("Arial", 17), fg_color="black",text_color="white", anchor="center", width=100, height=30).place(x=1210, y=170)    
    ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
    ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="green",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
def rematch():
    global State1
    global State2
    global coin1_position
    global coin2_position
    global ButtonPlayer1
    global ButtonPlayer2
    global x1
    global x2
    global y1
    global y2
    global turn1
    global turn2
    turn1=0
    turn2=0
    State1=NORMAL
    State2=DISABLED
    coin1_position=0
    coin2_position=0
    ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
    ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
    x1=0
    x2=50
    y1=660
    y2=660
    player1_coin.place(x=x1, y=y1)
    player2_coin.place(x=x2, y=y2)
# Getting the x and Y coordinates of each cell 
Num = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 80, 79, 78, 77, 76, 75, 74,
        73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44,
        45, 46, 47, 48, 49, 50, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 20,
        19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# This is the Y coordinate of the first row
row = 89
i = 0
PositionDict = {}
# to iterate over the 10 cells
for x in range(1, 11):
# col = 45 is the x coordinate of the first cell
    col = 117
    for y in range(1, 11):
        PositionDict[Num[i]] = (col, row)
# x coordinate diffrence the two cells
        col += 59
        i += 1
# the Y coordinate difference between the two cells
    row += 55

PositionDict[0]=(50,660)   


#Input Player Names
def Input_Player1():
    global Player1
    global ButtonPlayer1
    Player1_Name = CTkInputDialog(title="Player 1 Name", text= "Enter First Player Name: ").get_input()
    if Player1_Name:
        CTkMessagebox(message=f"Welcome to the game: {Player1_Name}", bg_color="white",fg_color="white",title="Hey There!", text_color="black", font=("Times New Roma",15), icon=resolve_path("/Icon/OrangeIntroduction.ico"),icon_size=(200,800), width=200,height=200,title_color="black")
        Player1=Player1_Name
        ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
def Input_Player2():
    global Player2
    global ButtonPlayer2
    Player2_Name = CTkInputDialog(title="Player 2 Name", text= "Enter Second Player Name: ").get_input()
    if Player2_Name:
        CTkMessagebox(message=f"Welcome to the game: {Player2_Name}", bg_color="white",fg_color="white",title="Hey There!", text_color="black", font=("Times New Roma",15), icon=resolve_path("/Icon/GreenIntroduction.ico"),icon_size=(200,800), width=200,height=200,title_color="black")
        Player2=Player2_Name
        ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
#Creating Board

label1= CTkLabel(root, text=None, width=100, height=100)
#Creating the dice
DiceFilesList=["/Dice/Dice1.png", "/Dice/Dice2.png", "/Dice/Dice3.png", "/Dice/Dice4.png", "/Dice/Dice5.png", "/Dice/Dice6.png"]
DiceList = [resolve_path(file) for file in DiceFilesList]
#Initializing Object start position at zero
coin1_position=0
coin2_position=0
#creating the function of the dice itself randomizing
sixcount1=0
sixcount2=0
def diceimg1():
    global Position_Diff
    global path
    global State1
    global State2
    global ButtonPlayer1
    global ButtonPlayer2
    global sixcount2
    global sixcount1
    global GlobalPath1
    global turn1
    global turn2
    sixcount2=0
    Position_Diff=0
    path=random.randint(1,6)
    dicephoto=DiceList[path-1]
    DiceImage= CTkImage(light_image=Image.open(dicephoto), size=(100,100))
    label1.place(x=950, y=250)
    label1.configure(image=DiceImage, text=None, width=100, height=100)
    time.sleep(0.03)
    if turn1>0:
        if path==6:
            sixcount1+=1
        else:
            sixcount1=0
        root.after(500, coin1_move)
        if sixcount1>0 and sixcount1<4:
            State1=NORMAL
            State2=DISABLED
            ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
            ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)        
        else:
            State1=DISABLED
            State2=NORMAL
            ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
            ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
    else:
        GlobalPath1=path
        turn1+=1
        State1=DISABLED
        State2=NORMAL
        ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
        ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
def coin1_move():
    global coin1_position
    global x1
    global y1
    global Counter1
    global Player1Score
    global coin2_position
    global x2
    global y2
    Position_Diff=path
    if coin1_position==0:
        coin1_position=coin1_position+Position_Diff
        if coin1_position in PositionDict.keys():
            x1=PositionDict[coin1_position][0]
            y1=PositionDict[coin1_position][1]
            player1_coin.place(x=x1,y=y1)
            if coin1_position in snakes.keys():
                CTkMessagebox(title="Unlucky!!",title_color="black", message=f"{Player1} stepped on a snake", text_color= "Black", icon=resolve_path("/Icon/OrangeSnake.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
                time.sleep(1)
                coin1_position=snakes[coin1_position]
                x1=PositionDict[coin1_position][0]
                y1=PositionDict[coin1_position][1]
                player1_coin.place(x=x1,y=y1)
                if coin1_position==coin2_position:
                    coin2_position=1
                    x2=PositionDict[coin2_position][0]
                    y2=PositionDict[coin2_position][1]
                    player2_coin.place(x=x2,y=y2)
            elif coin1_position in ladders.keys():
                CTkMessagebox(title="Lucky!!",title_color="black", message=f"{Player1} stepped on a Ladder", text_color= "Black", icon=resolve_path("/Icon/OrangeLadder.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
                time.sleep(1)
                coin1_position=ladders[coin1_position]
                x1=PositionDict[coin1_position][0]
                y1=PositionDict[coin1_position][1]
                player1_coin.place(x=x1,y=y1)
                if coin1_position==coin2_position:
                    coin2_position=1
                    x2=PositionDict[coin2_position][0]
                    y2=PositionDict[coin2_position][1]
                    player2_coin.place(x=x2,y=y2)
                if coin1_position in ladders.keys():
                    coin1_position=ladders[coin1_position]
                    x1=PositionDict[coin1_position][0]
                    y1=PositionDict[coin1_position][1]
                    player1_coin.place(x=x1,y=y1)
                    if coin1_position==coin2_position:
                        coin2_position=1
                        x2=PositionDict[coin2_position][0]
                        y2=PositionDict[coin2_position][1]
                        player2_coin.place(x=x2,y=y2)
            elif coin1_position==coin2_position:
                coin2_position=1
                x2=PositionDict[coin2_position][0]
                y2=PositionDict[coin2_position][1]
                player2_coin.place(x=x2,y=y2)
    else:
        coin1_position=coin1_position+Position_Diff
        if coin1_position in PositionDict.keys():
            x1=PositionDict[coin1_position][0]
            y1=PositionDict[coin1_position][1]
            player1_coin.place(x=x1,y=y1)
            if coin1_position in snakes.keys():
                time.sleep(1)
                CTkMessagebox(title="Unlucky!!",title_color="black", message=f"{Player1} stepped on a snake", text_color= "Black", icon=resolve_path("/Icon/OrangeSnake.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
                coin1_position=snakes[coin1_position]
                x1=PositionDict[coin1_position][0]
                y1=PositionDict[coin1_position][1]
                player1_coin.place(x=x1,y=y1)
                if coin1_position==coin2_position:
                    coin2_position=1
                    x2=PositionDict[coin2_position][0]
                    y2=PositionDict[coin2_position][1]
                    player2_coin.place(x=x2,y=y2)
            elif coin1_position in ladders.keys():
                CTkMessagebox(title="Lucky!!",title_color="black", message=f"{Player1} stepped on a Ladder", text_color= "Black", icon=resolve_path("/Icon/OrangeLadder.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
                time.sleep(1)
                coin1_position=ladders[coin1_position]
                x1=PositionDict[coin1_position][0]
                y1=PositionDict[coin1_position][1]
                player1_coin.place(x=x1,y=y1)
                if coin1_position==coin2_position:
                    coin2_position=1
                    x2=PositionDict[coin2_position][0]
                    y2=PositionDict[coin2_position][1]
                    player2_coin.place(x=x2,y=y2)
                if coin1_position in ladders.keys():
                    coin1_position=ladders[coin1_position]
                    x1=PositionDict[coin1_position][0]
                    y1=PositionDict[coin1_position][1]
                    player1_coin.place(x=x1,y=y1)
                    if coin1_position==coin2_position:
                        coin2_position=1
                        x2=PositionDict[coin2_position][0]
                        y2=PositionDict[coin2_position][1]
                        player2_coin.place(x=x2,y=y2)
            elif coin1_position==coin2_position:
                coin2_position=1
                x2=PositionDict[coin2_position][0]
                y2=PositionDict[coin2_position][1]
                player2_coin.place(x=x2,y=y2)
            if coin1_position==100:
                Counter1 +=1
                Player1Score=CTkLabel(root, text=Counter1, font=("Arial", 20), fg_color="white", text_color="black", width=60, height=25).place(x=1200, y=200)
                EndMessage=CTkMessagebox(title="Game Over.",title_color="black", message=f"{Player1} Won!!", text_color= "Black", icon=resolve_path("/Icon/YouWon.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250,option_1='Exit', option_2='New Game', option_3='Rematch')
                response=EndMessage.get()
                if response == 'Rematch':
                    rematch()
                elif response =='New Game':
                    start_new_game()
                elif response =='Exit':
                    root.destroy()
            
        elif coin1_position >100:
            coin1_position=coin1_position-Position_Diff
            x1=PositionDict[coin1_position][0]
            y1=PositionDict[coin1_position][1]
            player1_coin.place(x=x1,y=y1)
    progressbar1.set(coin1_position/100)          

def diceimg2():
    global Position_Diff
    global path
    global State1
    global State2
    global ButtonPlayer1
    global ButtonPlayer2
    global sixcount1
    global sixcount2
    global GlobalPath2
    global turn2
    sixcount1=0
    State1=NORMAL
    State2=DISABLED
    ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
    ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
    Position_Diff=0
    path=random.randint(1,6)
    dicephoto=DiceList[path-1]
    DiceImage= CTkImage(light_image=Image.open(dicephoto), size=(100,100))
    label1.place(x=950, y=250)
    label1.configure(image=DiceImage, text=None, width=100, height=100)
    time.sleep(0.03)
    if turn2>0:
        if path==6:
            sixcount2+=1
        else:
            sixcount2=0
        root.after(500, coin2_move)
        if sixcount2>0 and sixcount2<3:
            State1=DISABLED
            State2=NORMAL
            ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
            ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
        else:
            State1=NORMAL
            State2=DISABLED
            ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
            ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
    else:
        GlobalPath2=path
        turn2+=1
        State1=NORMAL
        State2=DISABLED
        ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
        ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
        root.after(1000 , PlayerTurn())
def coin2_move():
    global coin2_position
    global Counter2  
    global x2
    global y2
    global Player2Score
    global coin1_position
    global x1
    global y1
    Position_Diff=path
    if coin2_position==0:
        coin2_position=coin2_position+Position_Diff
        if coin2_position in PositionDict.keys():
            x2=PositionDict[coin2_position][0]
            y2=PositionDict[coin2_position][1]
            player2_coin.place(x=x2,y=y2)
            if coin2_position in snakes.keys():
                CTkMessagebox(title="Unlucky!!",title_color="black", message=f"{Player2} stepped on a Snake", text_color= "Black", icon=resolve_path("/Icon/GreenSnake.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
                time.sleep(1)
                coin2_position=snakes[coin2_position]
                x2=PositionDict[coin2_position][0]
                y2=PositionDict[coin2_position][1]
                player2_coin.place(x=x2,y=y2)
                if coin2_position==coin1_position:
                    coin1_position=1
                    x1=PositionDict[coin1_position][0]
                    y1=PositionDict[coin1_position][1] 
                    player1_coin.place(x=x1,y=y1)
            elif coin2_position in ladders.keys():
                CTkMessagebox(title="Lucky!!",title_color="black", message=f"{Player2} stepped on a Ladder", text_color= "Black", icon=resolve_path("/Icon/GreenLadder.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
                time.sleep(1)
                coin2_position=ladders[coin2_position]
                x2=PositionDict[coin2_position][0]
                y2=PositionDict[coin2_position][1]
                player2_coin.place(x=x2,y=y2)
                if coin2_position==coin1_position:
                    coin1_position=1
                    x1=PositionDict[coin1_position][0]
                    y1=PositionDict[coin1_position][1] 
                    player1_coin.place(x=x1,y=y1)
                if coin2_position in ladders.keys():
                    coin2_position=ladders[coin2_position]
                    x2=PositionDict[coin2_position][0]
                    y2=PositionDict[coin2_position][1]
                    player2_coin.place(x=x2,y=y2)
                    if coin2_position==coin1_position:
                        coin1_position=1
                        x1=PositionDict[coin1_position][0]
                        y1=PositionDict[coin1_position][1] 
                        player1_coin.place(x=x1,y=y1)
            elif coin2_position==coin1_position:
                 coin1_position=1
                 x1=PositionDict[coin1_position][0]
                 y1=PositionDict[coin1_position][1] 
                 player1_coin.place(x=x1,y=y1)
    else:
        coin2_position=coin2_position+Position_Diff
        if coin2_position in PositionDict.keys():
            x2=PositionDict[coin2_position][0]
            y2=PositionDict[coin2_position][1]
            player2_coin.place(x=x2,y=y2)
            if coin2_position in snakes.keys():
                CTkMessagebox(title="Unlucky!!",title_color="black", message=f"{Player2} stepped on a Snake", text_color= "Black", icon=resolve_path("/Icon/GreenSnake.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
                time.sleep(1)
                coin2_position=snakes[coin2_position]
                x2=PositionDict[coin2_position][0]
                y2=PositionDict[coin2_position][1]
                player2_coin.place(x=x2,y=y2)
                if coin2_position==coin1_position:
                    coin1_position=1
                    x1=PositionDict[coin1_position][0]
                    y1=PositionDict[coin1_position][1] 
                    player1_coin.place(x=x1,y=y1)
            elif coin2_position in ladders.keys():
                CTkMessagebox(title="Lucky!!",title_color="black", message=f"{Player2} stepped on a Ladder", text_color= "Black", icon=resolve_path("/Icon/GreenLadder.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
                time.sleep(1)
                coin2_position=ladders[coin2_position]
                x2=PositionDict[coin2_position][0]
                y2=PositionDict[coin2_position][1]
                player2_coin.place(x=x2,y=y2)
                if coin2_position==coin1_position:
                    coin1_position=1
                    x1=PositionDict[coin1_position][0]
                    y1=PositionDict[coin1_position][1] 
                    player1_coin.place(x=x1,y=y1)
                if coin2_position in ladders.keys():
                    coin2_position=ladders[coin2_position]
                    x2=PositionDict[coin2_position][0]
                    y2=PositionDict[coin2_position][1]
                    player2_coin.place(x=x2,y=y2)
                    if coin2_position==coin1_position:
                        coin1_position=1
                        x1=PositionDict[coin1_position][0]
                        y1=PositionDict[coin1_position][1] 
                        player1_coin.place(x=x1,y=y1)
            elif coin2_position==coin1_position:
                coin1_position=1
                x1=PositionDict[coin1_position][0]
                y1=PositionDict[coin1_position][1]
                player1_coin.place(x=x1,y=y1)
            if coin2_position==100:
                Counter2 +=1
                Player2Score=CTkLabel(root, text=Counter2, font=("Arial", 20), fg_color="white",text_color="black", width=60, height=25).place(x=1260, y=200)
                EndMessage=CTkMessagebox(title="Game Over.",title_color="black", message=f"{Player2} Won!!", text_color= "Black", icon=resolve_path("/Icon/YouWon.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250,option_1='Exit', option_2='New Game', option_3='Rematch')
                response=EndMessage.get()
                if response == 'Rematch':
                    rematch()
                elif response =='New Game':
                    start_new_game()
                elif response =='Exit':
                    root.destroy()

        elif coin2_position >100:
            coin2_position=coin2_position-Position_Diff
            x2=PositionDict[coin2_position][0]
            y2=PositionDict[coin2_position][1]
            player2_coin.place(x=x2,y=y2)
    progressbar2.set(coin2_position/100)        
ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="black", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)

def PlayerTurn():
    global turn1
    global turn2
    global State1
    global State2
    global ButtonPlayer1
    global ButtonPlayer2
    if GlobalPath1>GlobalPath2:
        State1=NORMAL
        State2=DISABLED
        CTkMessagebox(title='Game start',title_color="black", message=f"{Player1} won.{Player1} will start the game!!", text_color= "Black", icon=resolve_path("/Icon/OrangeIntroduction.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)

    if GlobalPath2>GlobalPath1:
        State1=DISABLED
        State2=NORMAL
        CTkMessagebox(title='Game start',title_color="black", message=f"{Player2} won. {Player2} He will start game!!", text_color= "Black", icon=resolve_path("/Icon/OrangeIntroduction.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)
    elif GlobalPath1==GlobalPath2:
        turn1=0
        turn2=0
        CTkMessagebox(title='Game start',title_color="black", message=f"It is draw situation. You both will have to roll the dice again", text_color= "Black", icon=resolve_path("/Icon/OrangeIntroduction.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250)

    ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
    ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
#player 1 coin
player1_coin= CTkCanvas(root, width=30 , height=30)
player1_coin.create_rectangle(0,0,50,50, fill='Orange')
player1_coin.place(x=x1, y=y1)


#player 2 coin

player2_coin = CTkCanvas(root, width=30,height=30)
player2_coin.create_rectangle(0,0,50,50,fill="black" )
player2_coin.place(x=x2, y=y2)


#progress bar
progressbar1 = CTkProgressBar(root , orientation = "horizental" , width = 100 , height= 12 , fg_color="white" , progress_color="orange" , border_width= 0 ,  corner_radius = 5 , mode = "determinate" , bg_color= "white")
progressbar1.set(0)
progressbar1.place(x = 800 , y = 300)
progressbar2 = CTkProgressBar(root , orientation = "horizental" , width = 100 , height= 12 , fg_color="white" , progress_color="black" , border_width = 0  , corner_radius = 5 , mode = "determinate" ,  bg_color= "white")
progressbar2.set(0)
progressbar2.place(x = 1100 , y = 300)
def load_game(loadedfile):
    global Player1
    global Player2
    global State1
    global State2
    global coin1_position
    global x1
    global x2
    global y1
    global y2
    global coin2_position
    global Counter1
    global Counter2
    global sixcount1
    global sixcount2
    global turn1
    global turn2
    global ButtonPlayer1
    global ButtonPlayer2
    Load = open(resolve_path(f"\\Saves\\OneVOneH\\{loadedfile}.txt"), "r")
    Mode=Load.readline()
    Player1=Load.readline()
    Player1=Player1.rstrip()
    Player2=Load.readline()
    Player2=Player2.rstrip()
    state1value=Load.readline()
    state1value=state1value.rstrip()
    State1=state1value
    state2value=Load.readline()
    state2value=state2value.rstrip()
    State2=state2value
    coin1_positionvalue=Load.readline()
    coin1_position=int(coin1_positionvalue.rstrip())
    x1=PositionDict[coin1_position][0]
    y1=PositionDict[coin1_position][1]
    player1_coin.place(x=x1,y=y1)
    coin2_positionvalue=Load.readline()
    coin2_position=int(coin2_positionvalue.rstrip())
    x2=PositionDict[coin2_position][0]
    y2=PositionDict[coin2_position][1]
    player2_coin.place(x=x2,y=y2)
    Counter1Value=Load.readline()
    Counter1=int(Counter1Value.rstrip())
    Counter2Value=Load.readline()
    Counter2=int(Counter2Value.rstrip())
    sixcount1value=Load.readline()
    sixcount1=int(sixcount1value.rstrip())
    sixcount2value=Load.readline()
    sixcount2=int(sixcount2value.rstrip())
    turn1value=Load.readline()
    turn1=int(turn1value.rstrip())
    turn2value=Load.readline()
    turn2=int(turn2value.rstrip())
    ButtonPlayer1=CTkButton(root, text=Player1, height=50, width=100 ,hover_color="white", fg_color='orange',state=State1, command=diceimg1).place(x=785,y=450)
    ButtonPlayer2=CTkButton(root, text=Player2, height=50, width=100, fg_color='black',hover_color="black",text_color="white", text_color_disabled="grey", state=State2, command=diceimg2).place(x=1085, y=450)
    Player1Name=CTkLabel(root, text=Player1, font=("Arial", 17), fg_color="orange",text_color="white", anchor="center", width=100, height=30).place(x=1110, y=170)
    Player2Name=CTkLabel(root, text=Player2, font=("Arial", 17), fg_color="black",text_color="white", anchor="center", width=100, height=30).place(x=1210, y=170)
    Player1Score=CTkLabel(root, text=Counter1, font=("Arial", 20), fg_color="white", text_color="black", width=60, height=25).place(x=1200, y=200)
    Player2Score=CTkLabel(root, text=Counter2, font=("Arial", 20), fg_color="white",text_color="black", width=60, height=25).place(x=1260, y=200)

def save_game():
    Save = CTkInputDialog(title="Save Game", text="Write the save name")
    FileName=Save.get_input()
    F=open(resolve_path(f"\\Saves\\OneVOneH\\{FileName}.txt"), "w")
    SaveList=[Mode,Player1,Player2,State1,State2,coin1_position,coin2_position,Counter1,Counter2,sixcount1,sixcount2,turn1,turn2]
    for i in range(len(SaveList)):
        line=str(SaveList[i])
        F.write(f"{line}\n") 
    F.close()


    

    

    




def optionmenu_callback(choice):
    if choice=="Start New Game":
        start_new_game()
    elif choice=="Rematch":
        rematch()
    elif choice=='Exit Game':
        root.destroy()
    elif choice=='Save Game':
        save_game()
combobox = CTkOptionMenu(master=root,values=["Start New Game", "Rematch", "Save Game" , "Exit Game"],
                                    command=optionmenu_callback)
combobox.place(x=1200,y=10)


def button_window(event):
    message = CTkMessagebox(title="Exit",title_color="black", message = "Are you sure to exit", text_color= "Black", icon=resolve_path("/Icon/YouWon.ico"),icon_size=(200,250), bg_color="white", fg_color="white", width=300, height=250,option_1='Exit', option_2='Rematch' , option_3= "Continue")
    response=message.get()
    if response == 'Rematch':
        rematch()
    elif response == 'Exit':
        root.destroy()
    elif response  == "Continue":
        pass

# Use lambda to pass the event to button_window
root.bind('<Escape>', lambda event: button_window(event))





root.mainloop()
