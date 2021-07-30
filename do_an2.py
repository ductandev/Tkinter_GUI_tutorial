from tkinter import *
import cv2
from PIL import Image, ImageTk

def show_frame():									# Vì Tkinter không hỗ trợ hàm imshow giống như opencv nên phải show qua nhiều giai đoạn thông qua label.
	ret, frame = cap.read()							# Đọc frame từ camrera
	frame = cv2.flip(frame, 1)						# flip: hàm xoay ngược, lật ảnh , gồm có : -1, 0, 1  (link :https://techtutorialsx.com/2019/04/21/python-opencv-flipping-an-image/	)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)# Lọc ảnh từ BGR sang RBGA, ở dạng mảng
	img = Image.fromarray(cv2image)					# Image.fromarray: Tạo ra hình ảnh từ một đối tượng mảng (sử dụng giao thức đệm).
	imgtk = ImageTk.PhotoImage(image=img)			# ImageTk.PhotoImage: Load hình lên ('từ')
	show_video_label.image = imgtk					# dòng này có ý nghĩ là:	show_video_label = Label(image=imgtk)
	show_video_label.configure(image=imgtk)			# configure: hiển thị hình ảnh lên giao diện Tk // like set up background color, image
	show_video_label.after(10, show_frame)			# sau 0.01 giây, show từng frame ảnh

def btn_up_click():									# UP
	global jobid
	print("UP")
	#jobid = root.after(100, btn_up_click)

def btn_down_click():								# DOWN
	global jobid
	print("DOWN")
	#jobid = root.after(100, btn_down_click)
	
def btn_left_click():								# LEFT
	print("LEFT")
	
def btn_right_click():								# RIGHT
	print("RIGHT")

def btn_stop_click():								# STOP
	global jobid
	root.after_cancel(jobid)
	print("Stop")

def btn_exit_click():								# Exit
	print("Exit")
	root.destroy()

jobid = None
width, height = 600, 400
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.geometry("1200x550+100+70")
root.title("Giao Diện Điều Khiển Xe")
root.configure(bg='#F7F8FD')										#set up background color

background_image = PhotoImage(file="landscape.png")					#set up background root tab	

panel = Label(root, image = background_image)						# show background on Label root
panel.pack(side = "bottom", fill = "both", expand = "yes")

labelframe1 = LabelFrame(root, width=380, height=120,bg="#F7F8FD")  # Vẽ Khung
labelframe1.place(x=35,y=25)

lb1 = Label(root, text=" Đề tài: Nhận dạng chai nhựa\n Nguyễn Đức Tấn - 16026631\n Nguyễn Thế Hiển - 16031901", font=("Times New Roman", 22,"bold","italic"), fg="red", bg="#F7F8FD")
lb1.place(x=40,y=30)

btn_up = Button(root, text="UP", font=("san-serif", 16, "bold"), width=5, height=2, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange")#,command=btn_up_click)
btn_up.place(x = 170,y = 220)						# UP
btn_up.bind('<ButtonPress-1>', lambda event: btn_up_click())				# ButtonPress: nhấn nút
btn_up.bind('<ButtonRelease-1>', lambda event: btn_stop_click())			# ButtonRelease: nhả nút

btn_down = Button(root, text="Down", font=("san-serif", 16, "bold"),width=5, height=2, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange")#, command=btn_down_click)
btn_down.place(x = 170,y = 370) 					# DOWN
btn_down.bind('<ButtonPress-1>', lambda event: btn_down_click())			# ButtonPress: nhấn nút
btn_down.bind('<ButtonRelease-1>', lambda event: btn_stop_click())			# ButtonRelease: nhả nút

btn_left = Button(root, text="Left", font=("san-serif", 16, "bold"),width=5, height=2, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange")#,command=btn_left_click)
btn_left.place(x = 60,y = 295)						# LEFT

btn_right = Button(root, text="Right", font=("san-serif", 16, "bold"),width=5, height=2, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange")#,command=btn_right_click)
btn_right.place(x = 280,y = 295)					# RIGHT

btn_stop = Button(root, text="Stop", font=("san-serif", 16, "bold"),width=5, height=2, fg="white", bg="red",activeforeground = "white",activebackground = "orange")#,command=btn_stop_click)
btn_stop.place(x = 170,y = 295)					# STOP

btn_exit = Button(root, text="Exit", font=("san-serif", 16, "bold"),width=5, height=2, fg="white", bg="red",activeforeground = "white",activebackground = "orange",command=btn_exit_click)
btn_exit.place(x = 380,y = 440)						# Exit

show_video_label = Label(root)						# Label Camrera			
show_video_label.place(x = 490,y = 20)
show_frame()

def key_press(event):
	key = event.char
	#print(key, 'is pressed') 						# Hiển thị nút đã nhấn 
	if (key == 'w'):
		btn_up_click()
	if (key == 's'):
		btn_down_click()
#	if (key == 'a'):
#		btn_left_click()
#	if (key == 'd'):
#		btn_right_click()
	if (key == ' '):
		btn_stop_click()
		
def key_press1(event1):
	key1 = event1.char
	if (key1 == 'a'):
		btn_left_click()
	if (key1 == 'd'):
		btn_right_click()

root.bind('<Key>', lambda a : key_press(a))
root.bind('<Key>', lambda b : key_press1(b))
	
root.bind('<Escape>', lambda e: root.quit())		# Nhấn Nút ESC Thoát
root.resizable(False, False)						# không cho điều chỉnh kích thước cửa sổ
root.mainloop()										# vòng lặp để hiện giao diện, nếu ko có chương trình sẽ chạy 1 lần rồi tắt


