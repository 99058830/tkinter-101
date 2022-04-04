from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Clicker v1")

global counter
counter = 0

def up():
    global counter
    counter += 1
    cButton2.config(text = counter)
    main()

def down():
    global counter
    counter -= 1
    cButton2.config(text = counter)
    main()

cButton1 = Button(text = 'Up', command = up, fg = "darkgreen", bg = "white")
cButton1.pack()

cButton2 = Button(text = counter, command = counter, fg = "darkgreen", bg = "white", state = DISABLED)
cButton2.pack()

cButton3 = Button(text = 'Down', command = down, fg = "darkgreen", bg = "white")
cButton3.pack()

def main():
    if counter == 0:
        root['bg'] = 'grey'
    elif counter < 0:
      root['bg'] = 'red'  
    elif counter > 0:
        root['bg'] = 'green'

main()

root.mainloop()