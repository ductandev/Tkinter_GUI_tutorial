from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Lập trình Message box")

messagebox.showinfo("Học lập trình", "Lập trình tkinter cùng Tấn")
messagebox.showerror("11111111111", "111111111")
messagebox.showwarning("222222222", "2222222")
#showinfo: icon dấu chấm than
#showerror: icon dấu báo lỗi
#showwarning: icon dấu chấm than -> cảnh báo

win.mainloop()
