from tkinter import *

def start_motor(status):
    print("starting motor...(%s)" % status)
    move(status)

def move(status):
    global jobid
    print("Moving (%s)" % status)
    jobid = root.after(100, move, status)

def stop_motor():
    global jobid
    root.after_cancel(jobid)
    print("stopping motor...")

jobid = None

root = Tk()

for status in ("UP","Down"):	
    button = Button(root, text=status, width=5, height=2,bg="#1380C3")
    button.pack(side=LEFT)

    button.bind('<ButtonPress-1>', lambda event, status=status: start_motor(status))	# ButtonPress: nhấn nút
    button.bind('<ButtonRelease-1>', lambda event: stop_motor())			# ButtonRelease: nhả nút

root.bind('<Escape>', lambda e: root.quit())						# Nhấn Nút ESC Thoát
root.mainloop()
