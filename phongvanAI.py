from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def btn_exit_click():
	print("Exit")
	formLogin.destroy()

def btn_choosefile():
	global count_toolbar
	
	filetypes = (('Data files', '*.data'),('Text files', '*.txt'),('Excel files', '*.csv'),('All files', '*.*'))
	filename = filedialog.askopenfilename( title='Select file', filetypes = filetypes)#initialdir='/home/tan/AI/giao dien Tkinter',
	print(filename)
	if not filename:									# Nếu ko có filename
		print("Closed")
	else:
		df = pd.read_csv(filename)
		# plt.plot(df)
		# plt.title("Wave")
		# plt.xlabel("Time[s]")
		# plt.ylabel("ECG [mV]")
		# plt.legend(["Raw ECG"])
		# plt.show()
		
		# the figure that will contain the plot
		fig = Figure(figsize = (5, 4),dpi = 100)
		
		# adding the subplot
		plot1 = fig.add_subplot(111)
		
		# plotting the graph
		plot1.plot(df)
		plot1.set_title("Wave")
		plot1.set_xlabel("Time[s]")
		plot1.set_ylabel("ECG [mV]")
		#plot1.legend(["Raw ECG"])

		# creating the Tkinter canvas
		# containing the Matplotlib figure
		canvas = FigureCanvasTkAgg(fig,master = formLogin)  
		canvas.draw()
		
		# placing the canvas on the Tkinter formLogin
		canvas.get_tk_widget().place(x=150,y=70)
		
		# creating the Matplotlib toolbar
		if (count_toolbar == 0):
			count_toolbar = 1								# make sure just disphay only 1 toolbar
			toolbar = NavigationToolbar2Tk(canvas, formLogin)
			toolbar.update()
		
		# placing the toolbar on the Tkinter formLogin
		canvas.get_tk_widget().place(x=150,y=70)

#MAIN
count_toolbar = 0											# variable for toolbar

#===========Create The FormLogin Window=================================================
formLogin = Tk()
formLogin.geometry("800x750+400+100")
formLogin.title("Wave display interface ")
formLogin.configure(bg='#F7F8FD')							# set up background color
#_______________________________________________________________________________________

#=================MENU==================================================================
menubar = Menu(formLogin)					# lệnh gọi sử dụng Menu

def about_click():
	messagebox.showinfo("About license", "This interface make by:\n + Nguyễn Đức Tấn ") 
	
menubar.add_command(label="About", command=about_click)
menubar.add_command(label="Quit!", command=formLogin.quit)
# display the menu 
formLogin.config(menu=menubar)
#________________________________________________________________________________________

#================LABEL===================================================================
labelframe1 = LabelFrame(formLogin, width=600, height=500)  
labelframe1.place(x=100,y=20)
#________________________________________________________________________________________

#================BUTTON==================================================================
btn_choosefile = Button(formLogin, text="Choose file", font=("san-serif", 16, "bold"),width=10, height=3, fg="white", bg="#1380C3",activeforeground = "white",activebackground = "orange",command=btn_choosefile)
btn_choosefile.place(x = 300,y = 600)

btn_exit = Button(formLogin, text="Exit", font=("san-serif", 16, "bold"),width=4, height=2, fg="white", bg="red",activeforeground = "white",activebackground = "orange",command = btn_exit_click)
btn_exit.place(x = 600,y = 632)
#________________________________________________________________________________________

formLogin.bind('<Escape>', lambda e: formLogin.quit())		# Nhấn Nút ESC Thoát
formLogin.bind('<q>'     , lambda e: formLogin.quit())		# Nhấn Nút q   Thoát
formLogin.resizable(False, False)				# không cho điều chỉnh kích thước cửa sổ, kéo ra kéo vào
formLogin.mainloop()
