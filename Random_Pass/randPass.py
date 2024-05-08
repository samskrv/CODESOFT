from random import choice,shuffle, randint
from tkinter import *
import pyperclip

def lenghtOfPass():
    num = int(pass_length_entry.get())
    match num :
        case 8:
            return [2,2,3,1]
        case 9:
            return [2,2,3,2]
        case 10:
            return [3,2,3,2]
        case 11:
            return [3,3,3,2]
        case 12:
            return [3,3,4,2]
        case 13:
            return [4,3,4,2]
        case 14:
            return [4,4,3,3]
        case 15:
            return [4,4,4,3]
        
def difficulty():
    return pass_state.get()

# randomPassword generate a password
def randomPassword():
    lower_alpha = list("abcdefghijklmnopqrstuvwxyz")
    upper_alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = list("0123456789")
    symbol = list("!#$%&*+-./<?>@=_")

    length_list = lenghtOfPass()
    difficulty_level = difficulty()

    lowerLength = length_list[0]
    upperLength =length_list[1]
    numLength = length_list[2]
    symbolLength = length_list[3]

    password_list = [choice(upper_alpha) for _ in range(upperLength)] + [choice(lower_alpha) for _ in range(lowerLength)] + [choice(num) for _ in range(numLength)]+ [choice(symbol) for _ in range(symbolLength)]

    if (difficulty_level == 2):
        shuffle(password_list)

    randPass = "".join(password_list)
    return randPass

# newPass deletes the password which is already there and generate a new one
def newPass():
    pass_entry.delete(0,END)
    password = randomPassword()
    pass_entry.insert(0,password)
    pass_label.config(text = f"Click Generate Password to get a password.\nYour new Password is : {password}")
    display.config(text="This password is copied into the clipboard!")
    # using the pyperclip moudle the password is copied the clipboard.
    pyperclip.copy(password)


# creating a GUI model to generate random password generator

window = Tk()
window.title("Random Password Generator")
# adding padding the GUI
window.config(padx=30, pady=30)

# arranging the elements using grid

canvas = Canvas(height = 250, width = 250)
logo_img = PhotoImage(file="Projects/Random_Pass/logo.png")
canvas.create_image(150,150, image = logo_img)
canvas.grid(row = 0, column = 1, columnspan=2)

pass_length = Label(text="Enter the length of password.", font = ("Arial", 20))
pass_length.grid(row =1 , column = 0, columnspan = 3)

pass_length_entry = Spinbox(from_=8, to=15 ,width=8, font=("Arial", 15, "bold"), bg = "#CAF4FF")
pass_length_entry.grid(row =1 , column = 3)


pass_diff_label = Label(text="Difficulty Level", font = ("Arial", 20))
pass_diff_label.grid(row = 2 ,column = 0)

pass_state = IntVar()
pass_diff1 = Radiobutton(text = "Easy", value = 1 , variable = pass_state, font = ("cursive", 15), command = difficulty)
pass_diff1.select()
pass_diff1.grid(row = 2 ,column = 1)
pass_diff2 = Radiobutton(text = "Hard", value = 2, variable = pass_state, font = ("cursive", 15), command = difficulty)
pass_diff2.grid(row = 2 , column = 2)

pass_label = Label(text="Click Button to generate a new password" ,font=("Arial", 20, "italic"))
pass_label.grid(row= 3 ,column =0,columnspan=4)

pass_entry = Entry(width=23 ,font=("Arial", 15,"bold"), bg = "#CAF4FF")
pass_entry.grid(row =4 ,column =2)

button = Button(text = "Generate Password", font= ("cursive", 15),command=newPass, bg = "#8DECB4")
button.grid(row=4 ,column =3)

display = Label(text= "", font=("cursive", 15, "italic"))
display.grid(row=5 , column =0, columnspan = 4)

window.mainloop()