# Description: Label + Button + Entry + xử lý USER && PASSWORD
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2


def btn_addface_click():
	file=exec(open("0.py").read())						#Run file python <name>.py 	*
	print("Run file success ")

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

	def exit_click():									# Cú pháp Button phải đặt dưới vòng def exit_btn() thì button mới nhảy vào trong được
		cap.release()
		print("Clode Window slave success !")
		#root.quit()									# tắt hết tất cả cửa sổ
		root.destroy()									# chỉ tắt cửa sổ con
	
	def show_frame():
		ret, frame = cap.read()
		frame = cv2.flip(frame, 1)						# flip: hàm xoay ngược, lật ảnh , gồm có : -1, 0, 1  (link :https://techtutorialsx.com/2019/04/21/python-opencv-flipping-an-image/	)
		cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		lmain.place(x=40, y=30)
		lmain.after(10, show_frame)						# sau 0.01 giây

	btnLogin = Button(root, text="Start", font=("san-serif", 16, "bold"), fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", width=7, height=2 , command=show_frame)
	btnLogin.place(x = 210,y = 530)
	btnLogin = Button(root, text="EXIT", font=("san-serif", 16, "bold"), fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", width=7, height=2 , command=exit_click)
	btnLogin.place(x = 360,y = 530)

	lmain = Label(root)
	lmain.pack()

	root.bind('<Escape>', lambda e: root.destroy())		# Nhấn Nút ESC Để phá cửa sổ


def btnLogin_click():
	user = tbUser.get()
	passwd = tbPass.get()
#	if (user=="admin" & passwd=="123"):					# trong Python không thể so sánh 2 chuỗi str nên phải tách ra xử lý
	if (user =="admin"):
		if(passwd =="123"):
			tbUser.delete(0, END)						#xóa hiển thị đã nhập vào user
			tbPass.delete(0, END)						#xóa hiển thị đã nhập vào pass
			
			messagebox.showinfo("THÔNG BÁO", "Đăng nhập thành công.")
			#dllb1 = Label(formLogin, text = "Đăng nhập thành công", fg = "green" ,font = ("calibri", 11))	#dllb : delete Label1
			#dllb1.pack()
			#dllb1.after(1000 , dllb1.destroy)			#xóa Label sau 1 giây
			
			list = lg0,lg1,lb2,lb3,tbUser,tbPass,btnLogin	
			for i in list:									
				i.place_forget()						# xóa lg0,lg1,lb1,lb2,lb3,tbUser,tbPass,btnLogin
				#i.pack_forget()

			formLogin.geometry("600x400")
			
			lg1.place(x=235,y=20)						# đặt logo1
			
			btn_addface = Button(formLogin, text="Add Face", font=("san-serif", 16, "bold"),width=10, height=3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_addface_click).place(x = 10,y = 170)  	#.grid(row=3, column=0)#,   Dùng grid() nên sẽ không được dùng ||.pack()
			#btn_train.pack()
			btn_train = Button(formLogin, text="Train Face", font=("san-serif", 16, "bold"),width=10, height=3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", command=btn_train_click).place(x = 210,y = 170)  	#.grid(row=3, column=1)#,   Dùng grid() nên sẽ không được dùng ||.pack() 
			#btn_addface.pack()
			btn_recogn = Button(formLogin, text="Recognition", font=("san-serif", 16, "bold"),width=10, height=3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_recogn_click ).place(x = 410,y = 170)  #.grid(row=5, column=2)#,   Dùng grid() nên sẽ không được dùng ||.pack() 
			#btn_recogn.pack()
			
			formLogin.bind('<Escape>', lambda e: formLogin.quit())	# Nhấn Nút ESC Để Thoát										
			
		else:
			messagebox.showerror("THÔNG BÁO", "Đăng nhập thất bại.")
			dllb2 =	Label(formLogin, text = "Đăng nhập thất bại", fg = "red", bg="#F7F8FD" ,font = ("calibri", 11)) 	#dllb : delete Label2
			dllb2.place(x=121,y=470)
			dllb2.after(1000 , dllb2.destroy)			#xóa Label sau 1 giây
			
	else:
		messagebox.showerror("THÔNG BÁO", "Đăng nhập thất bại.")
		dllb3 = Label(formLogin, text = "Đăng nhập thất bại", fg = "red", bg="#F7F8FD" , font = ("calibri", 11))						#dllb : delete Label3
		dllb3.place(x=121,y=470)
		dllb3.after(1000 , dllb3.destroy)				#xóa Label sau 1 giây
	
	

formLogin = Tk()
formLogin.geometry("360x565") 
formLogin.title("Form đăng nhập")
formLogin.configure(bg='#F7F8FD')						#set up background color
#background_image = PhotoImage(file='white.png')
#background_label = Label(formLogin, image=background_image)
#background_label.place(x = 0, y = 0)					#relwidth=1, relheight=1

logo = Image.open("/home/tan/AI/giao dien Tkinter/logo face/iuh.png")
photo = ImageTk.PhotoImage(logo)
lg0 = Label(image=photo,bg="#F7F8FD")					#lg0: logo 0
lg0.place(x=25,y=5)

logo1 = Image.open("/home/tan/AI/giao dien Tkinter/logo face/logo9.png")
photo1 = ImageTk.PhotoImage(logo1)
lg1 = Label(image=photo1,bg="#F7F8FD")
lg1.place(x=120,y=145)

menubar = Menu(formLogin)								#lệnh gọi sử dụng Menu
file = Menu(menubar, tearoff=0)							# tearoff=0 : bắt đầu từ ví trí thứ 0 trong Menu
file.add_command(label="New")   
file.add_separator()									# dấu gặch ngăn cách [________]
file.add_command(label="Exit", command=formLogin.quit)  
menubar.add_cascade(label="File", menu=file)			# add_cascade : lệnh thêm vào list "File"

about = Menu(menubar, tearoff=0)
def about_click():
	messagebox.showinfo("About license", "This interface make by:\n + Nguyễn Đức Tấn 16026631\n + Nguyễn Thế Hiển 16031901  ")
about.add_command(label="About interface face recognition", command=about_click)  
menubar.add_cascade(label="About", menu=about)

menubar.add_command(label="Quit!", command=formLogin.quit)

# display the menu 
formLogin.config(menu=menubar) 							


#lb1 = Label(formLogin, text="Adminstator login form", font=("Times New Roman", 22,"bold","italic"), fg="red", bg="#F7F8FD")
#lb1.place(x=40,y=240)

lb2 = Label(formLogin, text="Tên đăng nhập ", font=("Arial",12), bg="#F7F8FD")
lb2.place(x=30,y=280)

#Entry: lệnh dùng để nhập vào
tbUser = Entry(formLogin, width=30, font=("Consolas", 12)) 			#tbUser : Textbox_user
tbUser.place(x=30,y=305)

lb3 = Label(formLogin, text="Mật Khẩu ", font=("Arial",12), bg="#F7F8FD")
lb3.place(x=30,y=335) 

#Entry: lệnh dùng để nhập vào
tbPass = Entry(formLogin, width=30, font=("Consolas", 12), show="*") #tbPass : Textbox_Pass
tbPass.place(x=30,y=360)

btnLogin = Button(formLogin, text="Đăng nhập", font=("san-serif", 16, "bold"), height = 1, width = 19, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange", command=btnLogin_click) # lệnh command dùng để truyền vào hàm btnLogin_click line 6 
btnLogin.place(x=28,y=420)

formLogin.bind('<Escape>', lambda e: formLogin.destroy())

formLogin.mainloop()
