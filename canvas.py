from tkinter import *
from tkinter import messagebox

tk=Tk()
tk.title("Lập trình control canavas")

cvFist  = Canvas(tk, width=200,  height= 300, bg="blue")
#cvFist.create_line(x1,y1,x2,y2, fill="red")
#cvFist.create_line(5,20,199,299, fill="red")
# Vòng lặp for
for i in range (300):
		cvFist.create_line(100,5,40,i)
cvFist.pack()

tk.mainloop()
