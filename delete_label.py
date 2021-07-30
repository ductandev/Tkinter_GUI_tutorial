# dùng để đóng Label hoặc cửa sổ sau n giây
import tkinter as tk

root = tk.Tk()
root.geometry("+250+250")

lb1 = tk.Label(root, text='Text on the screen', font=('Times New Roman','80'), fg='black', bg='white')
lb1.pack()

root.overrideredirect(True) 	# làm biến mất thanh ( - [] x )	
root.wm_attributes("-topmost", True)

root.after(1000 , root.destroy)

root.mainloop()
