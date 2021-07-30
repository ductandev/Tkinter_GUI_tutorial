from tkinter import *
from tkinter import messagebox

def nutnhan_click():
	#lấy thuộc tính text của control bất kì: <tên control>.get()
	messagebox.showinfo("Thông Báo", "Day la 1 cai Text" )

win = Tk()
win.title("Lập trình control Button ")

lbName = Label(win, text="Nguyễn Đức Tấn")
lbName.pack()

nutnhan = Button(win, text="Nhấp vào tôi đi", font=("Consolas", 14, "bold"), fg="red", bg="#2bc4b8",width=20, height=3, command=nutnhan_click ) #background có thể viết tắt = bg
nutnhan.pack()

win.mainloop()
