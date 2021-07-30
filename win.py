from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import shutil 
import os

def btn_delete_click():
	deletedir = filedialog.askdirectory(initialdir = "/home/tan/AI/giao dien Tkinter/test/", title='Chọn thư mục để xóa') #deletedir: delete directory
	print(deletedir)
	if not deletedir:										# Nếu ko có deletedir
		print("Closed")
	else:
		#os.chdir("/home/tan/AI/giao dien Tkinter/test")	# thay đổi thư mục làm việc hiện tại thành đường dẫn đã chỉ định
		#now = os.getcwd()									
		#os.remove(): chỉ xóa được file, không thể xóa hoặc xóa một thư mục
		#os.rmdir() : được sử dụng để xóa hoặc xóa một thư mục trống
		shutil.rmtree(deletedir)# được sử dụng để xóa toàn bộ cây thư mục
		print("Delete folder ----- %s ----- successed"%deletedir)
	
def btn_exit_click():
	win.destroy()
	
def btn_ok_click():
	name = tbname.get()
	path = "/home/tan/AI/giao dien Tkinter/test/"+name
	if not name:												# Nếu ko có name
		messagebox.showerror("THÔNG BÁO", "Vui lòng nhập tên")
	elif name.find("  ")!= -1 or name==" " or name.find(" ")==0:
		messagebox.showerror("THÔNG BÁO", "Sai cú pháp vui lòng nhập lại")
	elif os.path.exists(path):
		messagebox.showerror("THÔNG BÁO", "Tên đã tồn tại vui lòng chọn tên khác")
	else:	
		#os.makedirs											# os.makedirs: tạo được nhiều thư mục 1 lúc như tạo thư mục mẹ rồi tạo tiếp thư mục con trong đó và nhiều hơn được nữa.
		os.mkdir(path)											# os.mkdir:  mặc định chỉ tạo được 1 thư mục 
		print("-------Running face data creation -------")
		file1 = exec(open("./test/dataset.py").read())
		print("Done")
		print("-----------------------------")
		btn_ok.place_forget()
		dllb5 = Label(win, text = "Đăng ký thành công", fg = "green" ,font = ("calibri", 12), bg="#F7F8FD")	#dllb : delete Label5
		dllb5.place(x=45,y=77)
		dllb5.after(2000 , dllb5.destroy)
		tbname.delete(0, END)
		btn_ok.place(x=174,y=100)

#win = Toplevel(formLogin)
win = Tk()
win.geometry("350x250")
win.title("registration form")
win.configure(bg='#F7F8FD')										#set up background color

lb4 = Label(win, text="Name:", font=("Arial",12), bg="#F7F8FD")
lb4.place(x=10,y=20)

tbname = Entry(win, width=18, font=("Consolas", 12)) 			#tbname : Textbox_name
tbname.place(x=10,y=50)

btn_delete = Button(win, text="Delete", font=("san-serif", 16, "bold"), width = 4, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", command=btn_delete_click)
btn_delete.place(x=5,y=100)

btn_exit = Button(win, text="Exit", font=("san-serif", 16, "bold"), width = 3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_exit_click)
btn_exit.place(x=97,y=100)

btn_ok = Button(win, text="OK", font=("san-serif", 16, "bold"), width = 3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_ok_click)
btn_ok.place(x=174,y=100)

win.bind('<Escape>', lambda e: win.destroy())

win.mainloop()									#### *** lưu ý: bấm quit 2 lần ko dc là chỗ này chưa xóa 

