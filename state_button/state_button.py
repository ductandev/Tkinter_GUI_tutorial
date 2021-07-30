from tkinter import *  
root = Tk()
global hold_down

def button_hold(event):
    hold_down = True
    while hold_down: 
        print('test statement')

def stop_motor(event):
    hold_down = False
    print('button released')

button = Button(root, text ="forward")
button.pack(side=LEFT)
root.bind('<Button-1>',button_hold)
root.bind('<ButtonRelease-1>',stop_motor)
root.mainloop()
