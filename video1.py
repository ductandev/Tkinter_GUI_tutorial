from tkinter import *
import cv2
from PIL import Image, ImageTk

def exit_click():									# Cú pháp Button phải đặt dưới vòng def exit_btn() thì button mới nhảy vào trong được
	print("Clode Window slave success !")
	cap.release()
	#root.quit()									# tắt hết tất cả cửa sổ
	root.destroy()									# chỉ tắt cửa sổ con


def show_frame():									# Vì Tkinter không hỗ trợ hàm imshow giống như opencv nên phải show qua nhiều giai đoạn thông qua label.
	ret, frame = cap.read()							# Đọc frame từ camrera
	frame = cv2.flip(frame, 1)						# flip: hàm xoay ngược, lật ảnh , gồm có : -1, 0, 1  (link :https://techtutorialsx.com/2019/04/21/python-opencv-flipping-an-image/	)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)# Lọc ảnh từ BGR sang RBGA, ở dạng mảng
	img = Image.fromarray(cv2image)					# Image.fromarray: Tạo ra hình ảnh từ một đối tượng mảng (sử dụng giao thức đệm).
	imgtk = ImageTk.PhotoImage(image=img)			# ImageTk.PhotoImage: Load hình lên ('từ')
	show_video_label.image = imgtk					# dòng này có ý nghĩ là:	show_video_label = Label(image=imgtk)
	show_video_label.configure(image=imgtk)			# configure: hiển thị hình ảnh lên giao diện Tk // like set up background color, image
	show_video_label.place(x=40, y=30)				# đặt ở vị trí
	show_video_label.after(10, show_frame)			# sau 0.01 giây, show từng frame ảnh

width, height = 600, 400
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)			#thiết lập chiều rộng fame camera
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)			#thiết lập chiều dài fame camera

root = Tk()
root.title("Video Recognition tkiner")
root.geometry("1000x600")

btnLogin = Button(root, text="Start", font=("san-serif", 16, "bold"), fg="white", bg="red", width=7, height=2 , command=show_frame)
btnLogin.place(x = 210,y = 530)
btnLogin = Button(root, text="EXIT", font=("san-serif", 16, "bold"), fg="white", bg="red", width=7, height=2 , command=exit_click)
btnLogin.place(x = 360,y = 530)

show_video_label = Label(root)
show_video_label.pack()

root.bind('<Escape>', lambda e: root.quit())		# Nhấn Nút ESC Để Thoát =)) ******** thứ tìm kiếm đấy rồi
#show_frame()
root.mainloop()

