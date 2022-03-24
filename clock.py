from tkinter import *
from time import strftime
 
root = Tk()
root.title('Klokje')
 
def time():
    string = strftime('%H:%M:%S %p')
    chopper = string[:-2]
    label.config(text = chopper)
    label.after(1000, time)
 
label = Label(root, font = ('Helvetica', 25), bg = 'yellow', fg = 'red')
label.pack(anchor = 'center')
time()
 
mainloop()