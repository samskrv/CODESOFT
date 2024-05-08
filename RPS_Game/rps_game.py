from tkinter import *
from random import choice


window = Tk()
window.title("Rock Paper Scissors")
window.config(bg="#7BC9FF", padx =30 , pady = 20)

def play_game():
    # Create the options for rock, paper, and scissors
    options = ["Rock", "Paper", "Scissors"]

    # Asking the computer to make its choice
    computer_choice = choice(options)
    computer.config(text = f"Computer's Choice : {computer_choice}")

    # Geting the user's choice
    user_choice = str(entry.get())

    # Checking if the user's choice is in the list of options
    if user_choice in options:
        if user_choice == computer_choice:
            return "Tie!"
        elif (user_choice == "Paper" and computer_choice == "Scissors") or (user_choice == "Rock" and computer_choice == "Paper") or (user_choice == "Scissors" and computer_choice == "Rock"):
            return "You lose!"
        else:
            return "You wins!"
    else:
        return "Invalid choice. Try again!"
    
def show_result():
    result = play_game()
    result_label.config(text = result)

# Create a label and entry field for the user's choice
input_label = Label(text="Enter : 'Rock', 'Paper' or 'Scissors'\nPress the submit button to play!", font= ("Arial", 20), bg= "#7BC9FF")
input_label.grid(row = 0, column = 0)
input_label.config(pady= 10)

entry = Entry(width = 20, font = ("Arial", 20))
entry.grid(row = 1, column = 0)
entry.focus()

# Creating a button to submit the user's choice
button = Button(text="Submit", command=show_result, bg = "light green", font= ("Arial", 20))
button.grid(row =1, column = 1)

computer = Label(text = "Computer Choice : __", font=("Arial", 20), bg = "#7BC9FF")
computer.grid(row =2, column=0, columnspan = 2)

result_label = Label(text = "", font = ("Arial", 20), bg="#7BC9FF")
result_label.grid(row = 3, column = 0, columnspan = 2)

# Running the main loop
window.mainloop()