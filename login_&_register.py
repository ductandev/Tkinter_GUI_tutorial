from tkinter import *

def register_user():

	username_info = username.get()
	password_info = password.get()

	file=open(username_info+".txt", "w")
	file.write (username_info+"\n")
	file.write (password_info)
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(screenl, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def register():
	global screenl
	screenl = Toplevel (screen)		# Mở thêm Tab mới, Tab cũ vẫn còn
	screenl.title("Register")
	screenl.geometry ("300x250")

	global username
	global password
	global username_entry
	global password_entry
	username = StringVar()
	password = StringVar()

	Label(screenl, text = "Please enter details below").pack()
	Label(screenl, text = "").pack()
	Label(screenl, text = "Username * ").pack()
	username_entry = Entry(screenl, textvariable = username)
	username_entry.pack()
	Label(screenl, text = "Password * ").pack()
	password_entry = Entry(screenl, textvariable = password)
	password_entry.pack()
	Label(screenl, text = "").pack()
	Button(screenl, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    print ("Login session started")
    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = 300, height = "2", font = ("Calibri", 13)).pack()
    Label(text= "").pack()	#khoảng cách dòng
    Button(text = "Login", width = 30, height = "2", command = login).pack()
    Label(text= "").pack()	#khoảng cách dòng
    Button(text = "Register", width = 30, height = "2", command = register).pack()
    
    screen.mainloop()

main_screen()

