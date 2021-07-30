from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")      
messagebox.showinfo("information","Information")  							# show info
messagebox.showwarning("warning","Warning") 								# show warning
messagebox.showerror("error","Error")										# show error
messagebox.askquestion("Confirm","Are you sure?")							# ask question Yes / No
messagebox.askokcancel("Redirect","Redirecting you to www.javatpoint.com")	# ask Ok  / Cancel
messagebox.askyesno("Application","Got It?") 								# ask Yes / No
messagebox.askretrycancel("Application","try again?")  						# ask Try / cancel
  
top.mainloop()  
