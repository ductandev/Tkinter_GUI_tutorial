from tkinter import *

def aa():
	list = b,c
	for i in list:
		i.pack_forget()
		print("n",i)
	#b.pack_forget()
	#c.pack_forget()
root = Tk()
root.geometry("250x250")

b = Button(root, text=("Delete me"), command=aa)#, command=lambda: b.pack_forget())
b.pack()

c = Label(root, text="hello world")
c.pack()

root.mainloop()
