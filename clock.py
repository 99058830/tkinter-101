from tkinter import *
from time import strftime
 
root = Tk()
root.title('Klokje')
 
def time():
    string = strftime('%H:%M:%S %p')
    chopper = string[:-2] # removes chars AM or PM
    label.config(text = chopper)
    label.after(1000, time) # callback na 1000
 
label = Label(root, font = ('Helvetica', 25), bg = 'yellow', fg = 'red') # style
label.pack(anchor = 'center') # center label
time()
 
mainloop()