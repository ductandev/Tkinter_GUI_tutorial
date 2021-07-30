from tkinter import *
from tkinter import messagebox

tk=Tk()
tk.title("Lập trình control canavas")

cas  = Canvas(tk, width=200,  height= 300, bg="blue")
cas.pack()
cas.create_polygon(10,10,10,30,50,30, fill="red")

def dichchuyen(event):
	if event.keysym == "Up":
		cas.move(1, 0, -30)
	elif event.keysym == "Down":
		cas.move(1, 0, 30)
	elif event.keysym == "Left":
		cas.move(1, -30, 0)
	elif event.keysym == "Right":
		cas.move(1, 30, 0)
	else:
		cas.move(1, 0, 0)

cas.bind_all('<KeyPress-Up>', dichchuyen)
cas.bind_all('<KeyPress-Down>', dichchuyen)
cas.bind_all('<KeyPress-Left>', dichchuyen)
cas.bind_all('<KeyPress-Right>', dichchuyen)

tk.mainloop()
