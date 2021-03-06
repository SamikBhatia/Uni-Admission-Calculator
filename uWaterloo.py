#importing interface and math libraries
from tkinter import *
from math import *

#waterloo probability function
def uw(ent1, var2):
    prog = ["Arts", "Engineering", "Science"]

    x = float(ent1.get())

    if var2.get() == prog[0]:
        mu = 84
        sig = 5
    elif var2.get() == prog[1]:
        mu = 90
        sig = 4.5
    elif var2.get() == prog[2]:
        mu = 88
        sig = 5

    prob = 0.5*erf((x-mu)/sig)+0.5
    
    #interface configuration
    win = Tk()
    win.geometry("600x200")
    
    if x > 0 and x < 100:
        message = Label(win, text = "You have a " + str(round(100*prob, 1)) + "%" + " chance of getting an offer", font = "Bahnschrift 11")
        message.place(x = '50', y = '75')
    else:
        message = Label(win, text = "Please enter an average in bounds", font = "Bahnschrift 11")
        message.place(x = '50', y = '75')
