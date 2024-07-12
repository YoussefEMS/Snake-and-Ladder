import customtkinter
from subprocess import call
import os


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def resolve_path(file):
    return os.path.dirname(__file__) + file

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1200x800")
#Creating Game title
app.title("Snake and Ladder game")
app.attributes('-fullscreen', True)
#Creating Game icon
app.iconbitmap(resolve_path("\\Icon\\SnakeLadder.ico"))
app.minsize(1500,1000)
app.maxsize(1500,1000)
SelectMode = customtkinter.CTkLabel(app, text="Select Mode",width=100, height=100, font=("Times New Roman",80))
SelectMode.place(x=450,y=50)
def OnevsOneH():
    call(["python", resolve_path("\\OneVsOneH.py")])
    app.destroy()
def OnevspcH():
    call(["python", resolve_path("\\OneVsPCH.py")])
    app.destroy()
def OnevsOneE():
    call(["python", resolve_path("\\OneVsOneE.py")])
    app.destroy()
def OnevspcE():
    call(["python", resolve_path("\\OneVsPCE.py")])
    app.destroy()
Easy1 = customtkinter.CTkLabel(app, text="Easy",width=100, height=100, font=("Times New Roman",40))
Easy1.place(x=400,y=450)
DifficultyText= customtkinter.CTkLabel(app, text="Difficulty Level", width=100, height=100, font=("Times New Roman",20))
DifficultyText.place(x=665, y=450, anchor=customtkinter.CENTER)
button1 = customtkinter.CTkButton(master=app, text="1 vs 1", command=OnevsOneE)
button2 = customtkinter.CTkButton(master=app, text="1 vs PC", command=OnevspcE)
button1.place(x=400, y=300, anchor=customtkinter.CENTER)
button2.place(x=900, y=300, anchor=customtkinter.CENTER)
def switch_function():
    global Easy
    global Hard
    global Easy1
    global button1
    global button2
    Easy1.place_forget()
    if switch1.get() == "Easy":
        Hard.place_forget()
        Easy = customtkinter.CTkLabel(app, text="Easy",width=100, height=100, font=("Times New Roman",40))
        Easy.place(x=400, y=450)
        button1 = customtkinter.CTkButton(master=app, text="1 vs 1", command=OnevsOneE)
        button2 = customtkinter.CTkButton(master=app, text="1 vs PC", command=OnevspcE)
        button1.place(x=400, y=300, anchor=customtkinter.CENTER)
        button2.place(x=900, y=300, anchor=customtkinter.CENTER)
    elif switch1.get() == "Hard":
        Easy.place_forget()
        Hard = customtkinter.CTkLabel(app, text="Hard",width=100, height=100, font=("Times New Roman",40))
        Hard.place(x=900, y=450)
        button1 = customtkinter.CTkButton(master=app, text="1 vs 1", command=OnevsOneH)
        button2 = customtkinter.CTkButton(master=app, text="1 vs PC", command=OnevspcH)
        button1.place(x=400, y=300, anchor=customtkinter.CENTER)
        button2.place(x=900, y=300, anchor=customtkinter.CENTER)
switch_var= customtkinter.StringVar(value="Easy")
switch1=customtkinter.CTkSwitch(app, text="", variable=switch_var, onvalue="Hard", offvalue="Easy", command=switch_function)
switch1.place(x=700, y=500, anchor=customtkinter.CENTER)
Easy=customtkinter.CTkLabel(app, text="Easy", width=100,height=100, font=("Times New Roman",15))
Hard=customtkinter.CTkLabel(app, text="Hard", width=100, height=100, font=("Times New Roman",15))








app.mainloop()

