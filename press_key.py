from tkinter import * 
from tkinter.ttk import *

def key_press(event): 
    key = event.char 
    print(key, 'is pressed') 
  
# creates tkinter window or root window 
root = Tk() 
root.geometry('200x100') 

a = Label(root,text="nhan phim bat ky")
a.pack()

# here we are binding keyboard 
# with the main window 
root.bind('<Key>', lambda a : key_press(a)) 
  
mainloop() 
