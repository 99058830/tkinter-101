from cProfile import label
from tkinter import *

root = Tk()
root.title('Clicker v1')

number = 0

def up():
    number + 1
    jaj.config(text = number) # Change text ofzo

def down():
    number - 1
    jaj["text"] = number

root.geometry("500x250")
b1 = Button(root, text='Up', command=up).place(x=200, y=100)
jaj = Label(text= number).pack(pady=30)
b2 = Button(root, text='Down', command=down).place(x=300, y=100)

mainloop()