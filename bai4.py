from tkinter import *

win = Tk()
win.title("Lập trình control tkinter ")

nutnhan = Button(win, text="Nhấp vào tôi đi", font=("Consolas", 14, "bold"), fg="red", bg="#2bc4b8", width=20, height=4 ) #background có thể viết tắt = bg
nutnhan.pack()

win.mainloop()
