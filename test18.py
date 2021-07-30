from tkinter import *  
  
def open():  
	top = Toplevel()  
	top.geometry("400x400")
	
	def exit_click():
		#top.quit()			# tắt hết tất cả cửa sổ
		top.destroy()		# chỉ tắt cửa sổ con
		#top.update()	

	btn_exit = Button(top, text = "Exit", command=exit_click)#Lưu ý: Cú pháp Button phải đặt dưới vòng def exit_btn() thì button mới nhảy vào trong được
	btn_exit.place(x=75,y=50)

root = Tk()  
root.geometry("200x200")   

btn = Button(root, text = "open", command = open)  
btn.place(x=75,y=50)  
  
root.mainloop()  
