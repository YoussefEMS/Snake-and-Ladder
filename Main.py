from customtkinter import *
from subprocess import call
import os
from CTkMessagebox import CTkMessagebox
def resolve_path(file):
    return os.path.dirname(__file__)+file
app = CTk()  # create CTk window like you do with the Tk window
app.geometry("1200x800")
#Creating Game title
app.title("Snake and Ladder game")
#Creating Game icon
app.iconbitmap(resolve_path("\\Icon\\SnakeLadder.ico"))
app.attributes('-fullscreen', True)
Game_name = CTkLabel(app , text = "Snake and ladder" , anchor = CENTER , font=("Courier New", 45 , "bold"))
Game_name.place(relx = 0.4 , rely = 0.1)
def exit():
    app.destroy()
def play():
    call(["python", resolve_path("\\SelectGameMode.py")])
    app.destroy()
def about():
    CTkMessagebox(title="About Us", message="Guesssss what!!!! \n We are a team of 4 successful software developers Omar , Maroska, Hamdy and Youssef under supervision of Dr Basma and Eng Mohammed Salah \n We all love coding and developing games and the biggest proof is that you are playing our game now!!!!! \n Hope you like it , Enjoy your day ❤",font=("Courier New", 20 , "bold"), icon=resolve_path("\\Team images\\IMG_2488.ico"), fg_color= "white", bg_color="white",text_color="black",title_color="black", icon_size=(500,560),width=1020,height=650)

play_button = CTkButton(app, text="Play Game", font=("Arial", 20), fg_color=("green", "lime"), bg_color=("white", "white"), corner_radius=10,command=play)
play_button.place(relx=0.5, rely=0.3, anchor= CENTER)

about_button =  CTkButton(app, text="About Us", font=("Arial", 20), fg_color=("blue", "dodgerblue"), bg_color=("white", "white"), corner_radius=10 , command = about)
about_button.place(relx=0.5, rely=0.5, anchor=CENTER)

exit_button =  CTkButton(app, text="Exit", font=("Arial", 20), fg_color=("red", "tomato"), bg_color=("white", "white"), corner_radius=10, command=exit)
exit_button.place(relx=0.5, rely=0.7, anchor= CENTER)


app.mainloop()