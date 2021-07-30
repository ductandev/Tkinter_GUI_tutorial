from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
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

def btn_clear_click():
	tbname.delete(0,END)
	tb_birthday.delete(0,END)
	tb_phone.delete(0,END)
	combo.current(0)
	
def btn_exit_click():
	win.destroy()
	
def btn_ok_click():
	name = tbname.get()
	birthday = tb_birthday.get()
	phone = tb_phone.get()
	dep = entry7.get()
	
	path = "/home/tan/AI/giao dien Tkinter/test/"+name
	if not name:												# Nếu ko có name
		messagebox.showerror("THÔNG BÁO", "Vui lòng nhập tên")
	elif name.find("  ")!= -1 or name==" " or name.find(" ")==0:
		messagebox.showerror("THÔNG BÁO", "Sai cú pháp vui lòng nhập lại !")
	elif os.path.exists(path):
		messagebox.showerror("THÔNG BÁO", "Tên đã tồn tại vui lòng chọn tên khác !")
	elif not birthday:
		messagebox.showerror("THÔNG BÁO", "Vui lòng nhập ngày sinh !")
	elif not phone:
		messagebox.showerror("THÔNG BÁO", "Vui lòng nhập số điện thoại !")
	elif not dep and dep=="":
		messagebox.showerror("THÔNG BÁO", "Vui lòng nhập chức vụ !")
	else:	
		#os.makedirs											# os.makedirs: tạo được nhiều thư mục 1 lúc như tạo thư mục mẹ rồi tạo tiếp thư mục con trong đó và nhiều hơn được nữa.
		os.mkdir(path)											# os.mkdir:  mặc định chỉ tạo được 1 thư mục 
		create_file=open(path+"/"+ name + ".txt", "w")
		create_file.write("Tên: "+ name + "\n")
		create_file.write("Ngày sinh: "+ birthday +"\n")
		create_file.write("Số điện thoại: "+ phone +"\n")
		create_file.write("Chức vụ: "+ dep)
		create_file.close()
		print("-------Running face data creation -------")
		file1 = exec(open("./test/dataset.py").read())
		print("Done")
		print("-----------------------------")
		btn_ok.place_forget()
		
		dllb5 = Label(win, text = "Đăng ký thành công", fg = "green" ,font = ("calibri", 12), bg="#F7F8FD")	#dllb : delete Label5
		dllb5.place(x=100,y=160)
		dllb5.after(2000 , dllb5.destroy)
		
		tbname.delete(0,END)
		tb_birthday.delete(0,END)
		tb_phone.delete(0,END)
		combo.current(0)
		
		btn_ok.place(x=252,y=200)

		with open(path+"/"+ name + ".txt", "r") as f:
			Label(win, text=f.read(), font=("Arial",12) , bg="#F7F8FD").pack()

#win = Toplevel(formLogin)
win = Tk()
win.geometry("340x250")
win.title("registration form")
win.configure(bg='#F7F8FD')										#set up background color

lb4 = Label(win, text="Tên:", font=("Arial",12), bg="#F7F8FD")
lb4.place(x=10,y=20)
tbname = Entry(win, width=18, font=("Consolas", 12)) 			#tbname : Textbox_name
tbname.place(x=120,y=20)

lb5 = Label(win, text="Ngày sinh:", font=("Arial",12), bg="#F7F8FD")
lb5.place(x=10,y=55)
tb_birthday = Entry(win, width=18, font=("Consolas", 12)) 		#tbname : Textbox_name
tb_birthday.place(x=120,y=55)

lb6 = Label(win, text="Số điện thoại:", font=("Arial",12), bg="#F7F8FD")
lb6.place(x=10,y=90)
tb_phone = Entry(win, width=18, font=("Consolas", 12)) 			#tbname : Textbox_name
tb_phone.place(x=120,y=90)

lb7 = Label(win, text="Chức vụ:", font=("Arial",12), bg="#F7F8FD")
lb7.place(x=10,y=125)
entry7=StringVar()
combo = ttk.Combobox(win, textvariable=entry7, width=12, font=("san-serif", 11, "bold"), state='readonly')
combo['values']=("","Giáo viên","Giám đốc","Trưởng Phòng","Phó Phòng","Quản lý","Nhân viên","Sinh viên")
combo.place(x=120,y=125)

btn_delete = Button(win, text="Delete", font=("san-serif", 16, "bold"), width = 4, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", command=btn_delete_click)
btn_delete.place(x=5,y=200)
	
btn_clear = Button(win, text="Clear", font=("san-serif", 16, "bold"), width = 3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_clear_click)
btn_clear.place(x=97,y=200)

btn_exit = Button(win, text="Exit", font=("san-serif", 16, "bold"), width = 3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_exit_click)
btn_exit.place(x=174,y=200)

btn_ok = Button(win, text="OK", font=("san-serif", 16, "bold"), width = 3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_ok_click)
btn_ok.place(x=252,y=200)

win.bind('<Escape>', lambda e: win.destroy())
win.resizable(False, False)										# không cho điều chỉnh kích thước cửa sổ, kéo ra kéo vào 
win.mainloop()													# *** lưu ý: bấm quit 2 lần ko dc là chỗ này chưa xóa 

