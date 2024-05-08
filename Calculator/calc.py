from tkinter import *
from keyboard import *

calculation = ""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_label.delete(1.0,END)
    text_label.insert(1.0, calculation)

def evaluate_calc():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_label.delete(1.0, END)
        text_label.insert(1.0, calculation)
    except:
        clear_field()
        text_label.insert(1.0, "ERROR")

def clear_field():
    global calculation
    calculation = ""
    text_label.delete(1.0, END)


window = Tk()
window.geometry('300x325')
window.title("Calculator")
window.config(padx= 20, pady = 20)

text_label = Text(height = 2, width = 24, font= ("Arial", 15))
text_label.grid(row = 0,column = 0, columnspan = 5)
text_label.config(pady = 10)

#Buttons: numbers 

btn_1 = Button(text = "1", height = 1, width = 5, font= ("Arial", 15), command = lambda: add_calculation(1))
btn_1.grid(row =1, column = 0) 

btn_2 = Button(text = "2", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(2))
btn_2.grid(row =1, column =1)

btn_3 = Button(text = "3", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(3))
btn_3.grid(row =1, column = 2)

btn_4 = Button(text = "4", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(4))
btn_4.grid(row =2, column = 0)

btn_5 = Button(text = "5", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(5))
btn_5.grid(row =2, column = 1)

btn_6 = Button(text = "6", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(6))
btn_6.grid(row =2, column = 2)

btn_7 = Button(text = "7", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(7))
btn_7.grid(row =3, column = 0)

btn_8 = Button(text = "8", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(8))
btn_8.grid(row =3, column = 1)

btn_9 = Button(text = "9", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(9))
btn_9.grid(row =3, column = 2)

btn_0 = Button(text = "0", height = 1, width = 5, font= ("Arial", 15), command = lambda:add_calculation(0))
btn_0.grid(row =4, column = 1)

btn_period = Button(text= ".", height = 1 ,width = 5, font= ("Arial", 14, "bold"), command = lambda:add_calculation("."))
btn_period.grid(row=4, column = 2)

# Operators Buttons

btn_add = Button(text = "+",height = 1, width = 5, font= ("Arial", 15), command = lambda: add_calculation("+"))
btn_add.grid(row = 1, column = 4)

btn_sub = Button(text = "-",height = 1, width = 5, font= ("Arial", 15), command = lambda: add_calculation("-"))
btn_sub.grid(row = 2, column = 4)

btn_mul = Button(text = "x",height = 1, width = 5, font= ("Arial", 15), command = lambda: add_calculation("*"))
btn_mul.grid(row = 3, column = 4)

btn_div = Button(text = "/",height = 1, width = 5, font= ("Arial", 15), command = lambda: add_calculation("/"))
btn_div.grid(row = 4, column = 4)

# Clear Button and Evaluate Buttons

btn_clear = Button(text = "C", height = 1, width = 10, font= ("Arial", 15), command = clear_field, bg= "light green")
btn_clear.grid(row = 5, column = 0, columnspan = 2 )

btn_equal = Button(text="=", height = 1, width = 10, font = ("Arial", 15), command = evaluate_calc, bg = "light blue")
btn_equal.grid(row=5,column = 2,columnspan = 3)

window.mainloop()