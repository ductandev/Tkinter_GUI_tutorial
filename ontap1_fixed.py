# Description: Label + Button + Entry + xử lý USER && PASSWORD
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import time
import shutil 
import os


def btn_train_click():
	file=open("aa.txt", "a")							#Mở File 		
	file.write ("abcd\n")								#Ghi vào file
	file.close()										#Đóng file
	print ("Write file success ")

def btn_recogn_click():
	width, height = 600, 400
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)			#thiết lập chiều rộng fame camera
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)			#thiết lập chiều dài fame camera

	root = Toplevel(formLogin)
	root.title("Video Recognition tkiner")
	root.geometry("1000x600")
	root.config(menu=menubar)							# hiển thị thanh Menu

	def exit_click():									# Cú pháp Button phải đặt dưới vòng def thì button mới nhảy vào trong được
		cap.release()									#tắt camera
		print("Clode Window slave success !")
		btn_recogn.place(x = 410,y = 170)				# đặt lại nút nhấn đã tắt line 66
		root.destroy()									# chỉ tắt cửa sổ con
		#root.quit()									# tắt hết tất cả cửa sổ
	
	def show_frame():									# Vì Tkinter không hỗ trợ hàm imshow giống như opencv nên phải show qua nhiều giai đoạn thông qua label.
		if not cap.isOpened():                          #checks for the opening of camera
			print("\n---------------cant open the camera-------------------\n")
			root.destroy()								# ở đây ko nên dùng root.quit() vì nó sẽ đóng tất cả ko chừa lại gì

		ret, frame = cap.read()							# Đọc frame từ camrera
		frame = cv2.flip(frame, 1)						# flip: hàm xoay ngược, lật ảnh , gồm có : -1, 0, 1  (link :https://techtutorialsx.com/2019/04/21/python-opencv-flipping-an-image/	)
		if cap.isOpened():
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)# Lọc ảnh từ BGR sang RBGA, ở dạng mảng
			img = Image.fromarray(cv2image)				# Image.fromarray: Tạo ra hình ảnh từ một đối tượng mảng (sử dụng giao thức đệm).
			imgtk = ImageTk.PhotoImage(image=img)		# ImageTk.PhotoImage: Load hình lên ('từ')
			show_video_label.image = imgtk				# dòng này có ý nghĩ là:	show_video_label = Label(image=imgtk)
			show_video_label.configure(image=imgtk)		# configure: hiển thị hình ảnh lên giao diện Tk // like set up background color, image
			show_video_label.place(x=40, y=30)			# đặt ở vị trí
			show_video_label.after(10, show_frame)		# sau 0.01 giây, show từng frame ảnh ==> vòng lặp
			btn_start.destroy()
			#------------------------------------------------------------------------------------------------------------		
			# Ví dụ:
					#from PIL import Image, ImageTk

					#image = Image.open("lenna.jpg")
					#photo = ImageTk.PhotoImage(image)
					#label = Label(image=photo)
					#label.image = photo 									# keep a reference! #giữ tham chiếu
					#label.pack()
			#------------------------------------------------------------------------------------------------------------		
	btn_start = Button(root, text="Start", font=("san-serif", 16, "bold"), fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", width=7, height=2, command=show_frame)
	btn_start.place(x = 210,y = 530)
	btn_exit = Button(root, text="EXIT", font=("san-serif", 16, "bold"), fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", width=7, height=2 , command=exit_click)
	btn_exit.place(x = 360,y = 530)

	show_video_label = Label(root)
	show_video_label.pack()
	
	btn_recogn.place_forget()												# tắt nút Recognition
	
	root.bind('<Escape>', lambda e: root.destroy())							# Nhấn Nút ESC Để phá cửa sổ

def btn_addface_click():
	list = lg1, btn_addface, btn_train, btn_recogn							# Quên lg1 đi có thể hiện lại bằng lệnh: lg1.place(x=120,y=145)
	for i in list:									
		i.place_forget()
	#------------------------------------------------------------------------------------------------------------------
	def btnLogin_click():
		user = tbUser.get()
		passwd = tbPass.get()
		#if (user=="admin" & passwd=="123"):								# trong Python không thể so sánh 2 chuỗi str nên phải tách ra xử lý
		if (user =="admin"):
			if(passwd =="123"):
				tbUser.delete(0, END)										#xóa hiển thị đã nhập vào user
				tbPass.delete(0, END)										#xóa hiển thị đã nhập vào pass
				
				messagebox.showinfo("THÔNG BÁO", "Đăng nhập thành công.")
				dllb1 = Label(formLogin, text = "Đăng nhập thành công", fg = "green" ,font = ("calibri", 11))	#dllb : delete Label1
				#dllb1.pack()
				#dllb1.after(1000 , dllb1.destroy)							#xóa Label sau 1 giây
				
				list1 = lg0,lg1,lb2,lb3,tbUser,tbPass,btnLogin	
				for i in list1:									
					i.place_forget()										# xóa lg0,lg1,lb1,lb2,lb3,tbUser,tbPass,btnLogin
					#i.pack_forget()

				formLogin.geometry("600x400")
				
				lg1.place(x=235,y=20)										# đặt logo1
				
				#btn_addface.place(x = 10,y = 170)
				btn_train.place(x = 210,y = 170)
				btn_recogn.place(x = 410,y = 170)
				
				formLogin.bind('<Escape>', lambda e: formLogin.quit())		# Nhấn Nút ESC Để Thoát
				#------------------------------------------------------------------------------------------------------------
				
				#file=exec(open("xx.py").read())							#Run file python <name>.py 	*
				#print("Run file 1 success ")

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
						print("Delete folder ----- %s ----- successed\n"%deletedir)

				def btn_exit_click():
					win.destroy()
					btn_addface.place(x = 10,y = 170)

				def btn_ok_click():
					name = tbname.get()
					path = "/home/tan/AI/giao dien Tkinter/test/"+name
					if not name:											# Nếu ko có name
						messagebox.showerror("THÔNG BÁO", "Vui lòng nhập tên")
					elif name.find("  ")!= -1 or name==" " or name.find(" ")==0:
						messagebox.showerror("THÔNG BÁO", "Sai cú pháp vui lòng nhập lại")
					elif os.path.exists(path):
						messagebox.showerror("THÔNG BÁO", "Tên đã tồn tại vui lòng chọn tên khác")
					else:
						#os.makedirs										# os.makedirs: tạo được nhiều thư mục 1 lúc như tạo thư mục mẹ rồi tạo tiếp thư mục con trong đó và nhiều hơn được nữa.
						os.mkdir(path)										# os.mkdir: mặc định chỉ tạo được 1 thư mục 
						print("-------Running face data creation-------")
						file1 = exec(open("./test/dataset.py").read())
						print("Done")
						print("-----------------------------")
						
						btn_ok.place_forget()
						dllb5 = Label(win, text = "Đăng ký thành công", fg = "green" ,font = ("calibri", 12), bg="#F7F8FD")	#dllb : delete Label5
						dllb5.place(x=45,y=77)
						dllb5.after(2000 , dllb5.destroy)
						tbname.delete(0, END)
						btn_ok.place(x=174,y=100)
				
				win = Toplevel(formLogin)
				win.geometry("250x150")
				win.title("Form đăng ký")
				win.configure(bg='#F7F8FD')									#set up background color

				lb4 = Label(win, text="Name:", font=("Arial",12), bg="#F7F8FD")
				lb4.place(x=10,y=20)

				tbname = Entry(win, width=18, font=("Consolas", 12)) 		#tbname : Textbox_name
				tbname.place(x=10,y=50)

				btn_delete = Button(win, text="Delete", font=("san-serif", 16, "bold"), width = 4, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", command=btn_delete_click)
				btn_delete.place(x=5,y=100)

				btn_exit = Button(win, text="Exit", font=("san-serif", 16, "bold"), width = 3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_exit_click)
				btn_exit.place(x=97,y=100)

				btn_ok = Button(win, text="OK", font=("san-serif", 16, "bold"), width = 3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_ok_click)
				btn_ok.place(x=174,y=100)

				win.bind('<Escape>', lambda e: win.destroy())

				#------------------------------------------------------------------------------------------------------------
				
			else:
				messagebox.showerror("THÔNG BÁO", "Đăng nhập thất bại.")
				dllb2 =	Label(formLogin, text = "Đăng nhập thất bại", fg = "red", bg="#F7F8FD" ,font = ("calibri", 11)) 	#dllb : delete Label2
				dllb2.place(x=121,y=470)
				dllb2.after(1000 , dllb2.destroy)							#xóa Label sau 1 giây
				
		else:
			messagebox.showerror("THÔNG BÁO", "Đăng nhập thất bại.")
			dllb3 = Label(formLogin, text = "Đăng nhập thất bại", fg = "red", bg="#F7F8FD" , font = ("calibri", 11))		#dllb : delete Label3
			dllb3.place(x=121,y=470)
			dllb3.after(1000 , dllb3.destroy)								#xóa Label sau 1 giây
	#--------------------------------------------------------------------------------------------------------------------

	formLogin.geometry("360x565") 
	formLogin.title("Form đăng nhập ")
	#formLogin.configure(bg='#F7F8FD')										#set up background color

	lg0.place(x=25,y=5) 
	
	lg1.place(x=120,y=145)													# Đặt vị trí

	#lb1 = Label(formLogin, text="Adminstator login form", font=("Times New Roman", 22,"bold","italic"), fg="red", bg="#F7F8FD")
	#lb1.place(x=40,y=240)

	lb2 = Label(formLogin, text="Tên đăng nhập ", font=("Arial",12), bg="#F7F8FD")
	lb2.place(x=30,y=280)

	#Entry: lệnh dùng để nhập vào
	tbUser = Entry(formLogin, width=30, font=("Consolas", 12)) 				#tbUser : Textbox_user
	tbUser.place(x=30,y=305)

	lb3 = Label(formLogin, text="Mật Khẩu ", font=("Arial",12), bg="#F7F8FD")
	lb3.place(x=30,y=335) 

	#Entry: lệnh dùng để nhập vào
	tbPass = Entry(formLogin, width=30, font=("Consolas", 12), show="*")	#tbPass : Textbox_Pass
	tbPass.place(x=30,y=360)

	btnLogin = Button(formLogin, text="Đăng nhập", font=("san-serif", 16, "bold"), height = 1, width = 19, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", command=btnLogin_click)
	btnLogin.place(x=28,y=420)

	formLogin.bind('<Escape>', lambda e: formLogin.destroy())


formLogin = Tk()
formLogin.geometry("600x405")
formLogin.title("Face recognition interface")
formLogin.configure(bg='#F7F8FD')											#set up background color

logo = Image.open("/home/tan/AI/giao dien Tkinter/logo face/iuh.png")
photo = ImageTk.PhotoImage(logo)
lg0 = Label(image=photo,bg="#F7F8FD")										#lg0: logo 0

logo1 = Image.open("/home/tan/AI/giao dien Tkinter/logo face/logo9.png")
photo1 = ImageTk.PhotoImage(logo1)											# Load hình lên
lg1 = Label(image=photo1,bg="#F7F8FD")										# Truyền lên Label 
lg1.place(x=235,y=20)														# Đặt vị trí

menubar = Menu(formLogin)													#lệnh gọi sử dụng Menu
file = Menu(menubar, tearoff=0)												# tearoff=0 : bắt đầu từ ví trí thứ 0 trong Menu
file.add_command(label="New")   
file.add_separator()														# dấu gặch ngăn cách [________]
file.add_command(label="Exit", command=formLogin.quit)  
menubar.add_cascade(label="File", menu=file)								# add_cascade : lệnh thêm vào list "File"

about = Menu(menubar, tearoff=0)
def about_click():
	messagebox.showinfo("About license", "This interface make by:\n + Nguyễn Đức Tấn 16026631\n + Nguyễn Thế Hiển 16031901  ")
about.add_command(label="About interface face recognition", command=about_click)  
menubar.add_cascade(label="About", menu=about)

menubar.add_command(label="Quit!", command=formLogin.quit)
# display the menu 
formLogin.config(menu=menubar)

btn_addface = Button(formLogin, text="Add Face", font=("san-serif", 16, "bold"),width=10, height=3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_addface_click)
btn_addface.place(x = 10,y = 170)
btn_train = Button(formLogin, text="Train Face", font=("san-serif", 16, "bold"),width=10, height=3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", command=btn_train_click)
btn_train.place(x = 210,y = 170) 
btn_recogn = Button(formLogin, text="Recognition", font=("san-serif", 16, "bold"),width=10, height=3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_recogn_click)
btn_recogn.place(x = 410,y = 170)

formLogin.bind('<Escape>', lambda e: formLogin.quit())						# Nhấn Nút ESC Thoát

formLogin.mainloop()
