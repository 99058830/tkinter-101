from tkinter import *
import random

grabbelList = ['vishengel', 'bijl', 'houweel', 'schep', 'koevoet', 'schroevendraaier', 'lockpick', 'kniptang', 'schroef', 'spijker']

root = Tk()
root.title('Grabbelton')

def appear():
   global label
   grabbelRandom = (random.choice(grabbelList))
   if grabbelRandom in grabbelList:
      label.configure(text=f'Je hebt een {grabbelRandom}')
      grabbelList.remove(grabbelRandom)
      print(grabbelList)
      if len(grabbelList) == 0:
         label.configure(text=f'De grabbelton is leeg')
         button.configure(state = DISABLED)
   else:
      print('Error')

root.geometry("750x250")
button = Button(root)
button.configure(text='Grabbel!', command=appear)
button.pack(padx=20, pady=20)

label = Label(root)
label.configure(text='')
label.pack(padx=20, pady=20)
 
mainloop()