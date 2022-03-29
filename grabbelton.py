from tkinter import *
import random

grabbels = ['vishengel', 'bijl', 'houweel', 'schep', 'koevoet', 'schroevendraaier', 'lockpick', 'kniptang', 'schroef', 'spijker']

root = Tk()
root.title('Grabbelton')

def new_window():
   new = Toplevel()
   new.geometry("750x250")
   new.title("New Window")
   new.button = Button(new)
   new.button.configure(text='Sluiten')
   grabbelen = (random.choice(grabbels))
   Label(new, text=f"Je hebt een {grabbelen}").pack(pady=30)

root.geometry("750x250")
button = Button(root)
button.configure(text='Grabbel!', command=new_window)
button.pack(padx=20, pady=20)
 
mainloop()