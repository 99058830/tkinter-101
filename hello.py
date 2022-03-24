import tkinter as tk

window = tk.Tk()
window.title('Hello')
window.geometry("200x200")
window.configure(bg='grey')

hi = tk.Label(
    text='Hello Tkinter!',
    fg='red',
    bg='yellow',
    width=10,
    height=10,
)

hi.pack()

window.mainloop()