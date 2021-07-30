from tkinter import *

def start_motor():
	print("starting motor...(%s)" % status)
	LEFT_click()

def LEFT_click():
	global jobid
	global counter
	if (0<counter):
		counter-=5
	print(counter)

	jobid = root.after(100, LEFT_click)

def RIGHT_click():
	global jobid
	global counter
	if (counter<180):
		counter+=5
	print(counter)

	jobid = root.after(100, RIGHT_click)

def stop_motor():
	global jobid
	root.after_cancel(jobid)
	print("stopping motor...")

jobid = None
counter=0
root = Tk()

#for status in ("UP","Down"):
button_up = Button(root, text="UP", width=5, height=2,bg="#1380C3")
button_up.pack(side=LEFT)
button_up.bind('<ButtonPress-1>', lambda event: LEFT_click())				# ButtonPress: nhấn nút
button_up.bind('<ButtonRelease-1>', lambda event: stop_motor())			# ButtonRelease: nhả nút

button_down = Button(root, text="Down", width=5, height=2,bg="#1380C3")
button_down.pack(side=LEFT)
button_down.bind('<ButtonPress-1>', lambda event: RIGHT_click())				# ButtonPress: nhấn nút
button_down.bind('<ButtonRelease-1>', lambda event: stop_motor())			# ButtonRelease: nhả nút

root.bind('<Escape>', lambda e: root.quit())							# Nhấn Nút ESC Thoát
root.mainloop()
