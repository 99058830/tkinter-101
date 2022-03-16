import tkinter

window = tkinter.Tk()

window.title('My first window')

colors = ['blue', 'red', 'yellow', 'green', 'pink', 'brown']
times = 6
size = 50
def update():
    global size
    global times
    size += 50
    times -= 1
    window.configure(bg=colors[times-1])
    window.geometry(f'{size}x{size}')
    if times != 0:print(times)
    else: 
        print('BIEM!')
        window.destroy()

window.geometry(f'{size}x{size}')
for x in range(6):
    window.after(2000 * (x), update)

window.mainloop()