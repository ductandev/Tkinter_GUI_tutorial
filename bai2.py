# Chương trình nhãn Label
from tkinter import *

win = Tk()
win.title("Lập trình control tkinter ")

lbName = Label(win, text="Nguyễn Đức Tấn", font=("Arial", 14, "bold", "italic", "underline"), fg="red", background="#2bc4b8" ) #background có thể viết tắt = bg
lbName.pack()

win.mainloop()
