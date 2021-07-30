from tkinter import *

def create():
	top = Toplevel()
	top.title("Main Panel")
	top.geometry('500x500+100+450')
	
	msg = Message(top, text="Show on Sub-panel",width=100)
	msg.pack()
	
	def exit_btn():
		top.destroy()
		top.update()
	
	btn = Button(top,text='EXIT',command=exit_btn)	# Cú pháp Button phải đặt dưới vòng def exit_btn() thì button mới nhảy vào trong được
	btn.pack()

root = Tk()
root.geometry('300x400+100+50')

Button(root, text="Click me,Create a sub-panel", command=create).pack()
mainloop()
