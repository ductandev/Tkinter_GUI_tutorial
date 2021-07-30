from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("150x150")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")
   B1 = Button(top, text = "Say Hello", command = hello, state=DISABLED)
   B1.place(x = 30,y = 40)
B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 30,y = 40)

top.mainloop()
