from tkinter import *
#import os

root = Tk()
root.geometry("500x600")
img = PhotoImage(file="landscape.png")
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
