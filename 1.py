from tkinter import *

root = Tk()
root.geometry("250x200")

def clear():
	list = root.grid_slaves()
	for l in list:
		l.destroy()
		
		print("\n",l)

	Label(root,text="Hello word").pack()
	root.geometry("350x400")

Label(root,text='Hello World!').grid(row=0)
Button(root,text='Clear',command=clear).grid(row=1)

root.mainloop()
