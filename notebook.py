#import tkinter and ttk modules
import tkinter
from tkinter import ttk

root = tkinter.Tk()

nb = ttk.Notebook(root)
nb.pack()

f1 = tkinter.Frame(nb)
f2 = tkinter.Frame(nb)
nb.add(f1, text="First tab")
nb.add(f2, text="Second tab")

nb.select(f2)
nb.enable_traversal()

#Enter the mainloop
root.mainloop()
