#Chương trình in ra hello word

from tkinter import *

#Tạo ra một form mới 
#<tên form> = Tk()
tk = Tk()

#Thiết lập tiêu đề form
#<tên form>.title(<tiêu đề>)
tk.title("Lập trình giao diện tkinter ")

#tạo và add control và form
#Tạo control: <tên control> = <Kiểu control>(<tên form>, <thuộc tính 1>, <thuộc tính 2>)
#Thêm control vào form: <tên control>.pack()
lb1 = Label(tk, text="Hello word. Welcome to tkinter library!", font=("Times New Roman", 14))
lb1.pack()

#dừng form lại xem kết quả
#<tên form>.mainloop()
tk.mainloop()
