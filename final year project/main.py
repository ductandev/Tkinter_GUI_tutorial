from tkinter import *
import pandas as pd
import tkinter as tk
from playsound import playsound
from PIL import Image, ImageTk
import numpy as np
from tkinter import ttk
import sqlite3
import cv2
from PIL import Image
import os
import xlsxwriter
from datetime import date
from tkinter import messagebox
import sys
import random


#=====================Create Database=============================================
def createdb():
    conn = sqlite3.connect('saveddata.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT , passs TEXT,sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
    conn.commit()
    conn.close()
createdb()
#======================Adding new admin in database===============================
def saveadmin():
	name_err = name_entry.get()
	pass_err = pass_entry.get()
	if name_err == "":
		messagebox.showinfo("Invalid input","Username can't be Empty")
	elif pass_err == "":
		messagebox.showinfo("Invalid input","Password can't be Empty")
	else:
		conn=sqlite3.connect("saveddata.db")
		c=conn.cursor()
		c.execute("INSERT INTO users(name,passs) VALUES(?,?) ",(name_entry.get(),pass_entry.get()))
		conn.commit()
		messagebox.showinfo("Information","New User has been Added")
#========================FetchingdataofAdminfromdatabase==========================
def loggin():
	while True:
		a=name2_entry.get()
		b=pass2_entry.get()
		with sqlite3.connect("saveddata.db") as db:
			cursor=db.cursor()
		find_user= ("SELECT * FROM users WHERE name = ? AND passs = ?")
		cursor.execute(find_user,[(a),(b)])
		results=cursor.fetchall()
		if results:
			for i in results:
				window.destroy()
#==================Window2+CreateFrame+f1============Animation also================================================
				window2=Tk()
				f1=Frame(window2)
				f2=Frame(window2)
				f3=Frame(window2)
				f4=Frame(window2)
				def swap(frame):
					frame.tkraise()
				for frame in(f1,f2,f3,f4):
					frame.place(x=0,y=0,width=400,height=400)
				window2.geometry("400x400+420+170")
				window2.resizable(False, False)
				label3=Label(f1,text="Admin Panel",font=("arial",20,"bold"),bg="grey16",fg="white",relief=SUNKEN)
				label3.pack(side=TOP,fill=X)

				label4=Label(f2,text="Facial Recognition Attendance System",font=("arial",10,"bold"),bg="grey16",fg="white")
				label4.pack(side=BOTTOM,fill=X)
				statusbar=Label(f1,text="Facial Recognition Attendance System",font=("arial",8,"bold"),bg="grey16",fg="white",relief=SUNKEN,anchor=W)
				statusbar.pack(side=BOTTOM,fill=X)

				class AnimatedGIF(Label, object):
					def __init__(self, master, path, forever=True):
						self._master = master
						self._loc = 0
						self._forever = forever
						self._is_running = False
						im = Image.open(path)
						self._frames = []
						i = 0
						try:
							while True:
								photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
								self._frames.append(photoframe)
								i += 1
								im.seek(i)
						except EOFError: pass
						self._last_index = len(self._frames) - 1
						try:
							self._delay = im.info['duration']
						except:
							self._delay = 100
						self._callback_id = None
						super(AnimatedGIF, self).__init__(master, image=self._frames[0])
					def start_animation(self, frame=None):
						if self._is_running: return
						if frame is not None:
							self._loc = 0
							self.configure(image=self._frames[frame])
						self._master.after(self._delay, self._animate_GIF)
						self._is_running = True
					def stop_animation(self):
						if not self._is_running: return
						if self._callback_id is not None:
							self.after_cancel(self._callback_id)
							self._callback_id = None
						self._is_running = False
					def _animate_GIF(self):
						self._loc += 1
						self.configure(image=self._frames[self._loc])
						if self._loc == self._last_index:
							if self._forever:
								self._loc = 0
								self._callback_id = self._master.after(self._delay, self._animate_GIF)
							else:
								self._callback_id = None
								self._is_running = False
						else:
							self._callback_id = self._master.after(self._delay, self._animate_GIF)
					def pack(self, start_animation=True, **kwargs):
						if start_animation:
							self.start_animation()
						super(AnimatedGIF, self).pack(**kwargs)
					def grid(self, start_animation=True, **kwargs):
						if start_animation:
							self.start_animation()
						super(AnimatedGIF, self).grid(**kwargs)
					def place(self, start_animation=True, **kwargs):
						if start_animation:
							self.start_animation()
						super(AnimatedGIF, self).place(**kwargs)
					def pack_forget(self, **kwargs):
						self.stop_animation()
						super(AnimatedGIF, self).pack_forget(**kwargs)
					def grid_forget(self, **kwargs):
						self.stop_animation()
						super(AnimatedGIF, self).grid_forget(**kwargs)
					def place_forget(self, **kwargs):
						self.stop_animation()
						super(AnimatedGIF, self).place_forget(**kwargs)
				if __name__ == "__main__":
					l = AnimatedGIF(f1, "./Resources/giff.gif")
					l.pack()
				
				


				label4=Label(f3,text="Facial Recognition Attendance System",font=("arial",10,"bold"),bg="grey16",fg="white")
				label4.pack(side=BOTTOM,fill=X)
#================================Trian System===========================================================


				def trainsystem():
					recognizer = cv2.face.LBPHFaceRecognizer_create()
					path = 'dataset'
					if not os.path.exists('./recognizer'):
						os.makedirs('./recognizer')
					def getImagesWithID(path):
						imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
						faces = []
						IDs = []
						for imagePath in imagePaths:
							faceImg = Image.open(imagePath).convert('L')
							faceNp = np.array(faceImg,'uint8')
							ID = int(os.path.split(imagePath)[-1].split('.')[1])
							faces.append(faceNp)
							IDs.append(ID)
							cv2.imshow("training",faceNp)
							cv2.waitKey(10)
						return np.array(IDs), faces
					Ids, faces = getImagesWithID(path)
					recognizer.train(faces,Ids)
					recognizer.save('recognizer/trainingData.yml')
					statusbar['text']='System Trained....'
					cv2.destroyAllWindows()
#==============================Detector/Attendence======================================================

				def markattendance():
					if not os.path.exists('./Attendance'):
							os.makedirs('./Attendance')
					statusbar['text']='Attendance Marked....'
					conn = sqlite3.connect('saveddata.db')
					c = conn.cursor()
					fname = "recognizer/trainingData.yml"
					if not os.path.isfile(fname):
					  print("Please train the data first")
					  exit(0)
					face_cascade = cv2.CascadeClassifier('./Resources/haarcascade_frontalface_default.xml')
					cap = cv2.VideoCapture(0)
					recognizer = cv2.face.LBPHFaceRecognizer_create()
					recognizer.read(fname)
					while True:
					  ret, img = cap.read()
					  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
					  for (x,y,w,h) in faces:
					    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
					    ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
					    c.execute("select name from employees where id = (?);", (ids,))
					    result = c.fetchall()
					    name = result[0][0]
					    rname=str(name)
					    if conf < 50:
					      cv2.putText(img, name, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
					      cv2.putText(img,'Hit Enter if you are '+name,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
					    else:
					      cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
					  cv2.imshow('Face Recognizer',img)
					  k = cv2.waitKey(30) & 0xff
					  if k == 13:
					  	#c.execute("UPDATE employees set status='present' WHERE id=(?);",(ids,))
					  	c.execute("SELECT * FROM employees")
					  	employee_result = c.fetchall()
					  	stat=str(employee_result)
					  	time=str(date.today())
					  	df=pd.DataFrame(employee_result, columns=['id', 'Name', 'Department', 'Contact','Status'])
					  	datatoexcel = pd.ExcelWriter("./Attendance/Employee Attendance"+time+".xlsx", engine='xlsxwriter')
					  	df.to_excel(datatoexcel, index= False, sheet_name = "Sheet1")
					  	worksheet = datatoexcel.sheets['Sheet1']
					  	#df.assign(E="")
					  	#header_list=['F']
					  	#df = df.reindex(columns = header_list)
					  	worksheet.set_column('A:A', 8)
					  	worksheet.set_column('B:B', 20)
					  	worksheet.set_column('C:C', 25)
					  	worksheet.set_column('D:D', 20)
					  	worksheet.set_column('E:E', 20)
					  	worksheet.set_column('F:F', 20)
					  	df.loc[stat, 'Status'] = 'present'
					  	#df.at[0,'status']= 'present'
					  	#df.set_value(stat, 'E','present')
					  	#df.set_value(rname, 'status','present')
					  	datatoexcel.save()
					  	playsound('./Resources/sound2.mp3')
					  	break
					cap.release()
					conn.commit()
					conn.close()
					cv2.destroyAllWindows()

#================================Frame2=================================================================

				label5=Label(f2,text="Employee Management",font=("arial",20,"bold"),bg="grey16",fg="white")
				label5.pack(side=TOP,fill=X)

				label6=Label(f2,text="Name",font=("arial",10,"bold"))
				label6.place(x=70,y=70)
				entry6=StringVar()
				entry6=ttk.Entry(f2,textvariable=entry6)
				entry6.place(x=170,y=70)
				entry6.focus()

				label7=Label(f2,text="Department",font=("arial",10,"bold"))
				label7.place(x=70,y=100)
				entry7=StringVar()
				combo=ttk.Combobox(f2,textvariable=entry7,width=15,font=("arial",10,"bold"),state='readonly')
				combo['values']=("BSInformationTech","BSChemistry","BSPhysics","BSMathematics","B.EDHons","MAEnglish","BBA")
				combo.place(x=170,y=100)
				label8=Label(f2,text="ContactNo",font=("arial",10,"bold"))
				label8.place(x=70,y=150)
				entry8=StringVar()
				entry8=ttk.Entry(f2,textvariable=entry8)
				entry8.place(x=170,y=150)

				btn1w2=ttk.Button(f1,text="Manage Employee",command=lambda:swap(f2))
				btn1w2.place(x=255, y=60,width=150,height=30)

				btn2w2=ttk.Button(f1,text="Trian System",command=trainsystem)
				btn2w2.place(x=255, y=115,width=150,height=30)

				btn3w2=ttk.Button(f1,text="Mark Attendance",command=markattendance)
				btn3w2.place(x=255, y=170,width=150,height=30)

#======================Record_images_with_database======================================

				def capture_images():
					conn = sqlite3.connect('saveddata.db')
					c = conn.cursor()
					sql = """;
					CREATE TABLE IF NOT EXISTS employees (
								id integer unique primary key autoincrement,
								name text,dept text,contactno text,Status text
					);
					"""
					c.executescript(sql)
					if not os.path.exists('./dataset'):
						os.makedirs('./dataset')
					uname=entry6.get()
					up1=uname.upper()
					dep=entry7.get()
					cont=entry8.get()
					if uname=="":
						messagebox.showerror("Error","Please Enter Employee Name")
					elif dep=="":
						messagebox.showerror("Error","Please Select Department")
					elif cont=="":
						messagebox.showerror("Error","Please Enter Contact no")
					else:
						c.execute('INSERT INTO employees (name,dept,contactno) VALUES (?,?,?)', (up1,dep,cont))
						uid = c.lastrowid
						face_classifier=cv2.CascadeClassifier("./Resources/haarcascade_frontalface_default.xml")

						def face_extractor(img):
							gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
							faces=face_classifier.detectMultiScale(gray,1.2,7)
							if faces is():
								return None
							for(x,y,w,h) in faces:
								cropped_face=img[y:y+h,x:x+w]
							return cropped_face
						cap=cv2.VideoCapture(0)
						count=0
						while True:
							ret,frame=cap.read()
							if face_extractor(frame) is not None:
								count+=1
								face=cv2.resize(face_extractor(frame),(400,400))
								face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
								file_name_path="dataset/"+up1+"."+str(uid)+"."+str(count)+".jpg"
								cv2.imwrite(file_name_path,face)
								cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
								cv2.imshow("Face Cropper",face)
							else:
								print("face not found")
								pass
							if cv2.waitKey(1)==13 or count==70:
								break
						cap.release()
						conn.commit()
						conn.close()
						statusbar['text']='Employee has been Added....'
						cv2.destroyAllWindows
						messagebox.showinfo("Information","Images has been collected")


				btn5w2=ttk.Button(f2,text="Capture and Save",command=capture_images)
				btn5w2.place(x=170, y=240,width=130,height=30)

				btn4w2=ttk.Button(f2,text="Back	",command=lambda:swap(f1))
				btn4w2.place(x=3, y=40,width=50,height=30)
				def swap2(frame):
					frame.tkraise()

				btn7w2=ttk.Button(f3,text="Back",command=lambda:swap(f1))
				btn7w2.place(x=3, y=40,width=50,height=30)

				btn6w2=ttk.Button(f1,text="View Employee's Data",command=lambda:swap2(f3))
				btn6w2.place(x=255, y=225,width=150,height=30)

#=========================Window2Frame4DevelopersPage=========================================

				label10=Label(f4,text="Developers",font=("arial",20,"bold"),bg="grey16",fg="white")
				label10.pack(side=TOP,fill=X)
				label11=Label(f4,text="A Project By Code Eater's",font=("arial",10,"bold"),bg="grey16",fg="white")
				label11.pack(side=BOTTOM,fill=X)

				label10=Label(f4,text=" Information Will be Added Soon!",font=("arial",12,"bold"))
				label10.place(x=75,y=150)

				def swap4(frame):
					frame.tkraise()
					statusbar['text']='Facial Recognition Attendance System'

				btn4w2=ttk.Button(f4,text="Back	",command=lambda:swap4(f1))
				btn4w2.place(x=3, y=40,width=50,height=30)


				def swap3(frame):
					frame.tkraise()	


				btn9w2=ttk.Button(f1,text="Developers",command=lambda:swap3(f4))
				btn9w2.place(x=255, y=280,width=150,height=30)


				def quit():
					window2.destroy()


				btn9w2=ttk.Button(f1,text="Exit",command=quit)
				btn9w2.place(x=255, y=335,width=150,height=30)


#===========================FETCHDATABASEINLISTVIEW=========================================	


				def fetch():
					conn = sqlite3.connect("saveddata.db")
					cur = conn.cursor()
					cur.execute("SELECT * FROM employees")
					rows = cur.fetchall()
					for row in rows:
						List_Table.insert("", tk.END, values=row)
					conn.close()
#==========================DeleteRecordfromDatabase=========================================
				def dell():
					conn = sqlite3.connect("saveddata.db")
					cur = conn.cursor()
					cur.execute("DELETE FROM employees where id=?;",(ids,))
					conn.commit()
					conn.close()



				btn8w2=ttk.Button(f3,text="View Record",command=fetch)
				btn8w2.place(x=10, y=320,width=130,height=30)

				btn9w2=ttk.Button(f3,text="Delete Selected",command=dell)
				btn9w2.place(x=250, y=320,width=130,height=30)


#================================Frame3LISTVIEW==========================================


				label8=Label(f3,text="Employee Records",font=("arial",20,"bold"),bg="grey16",fg="white")
				label8.pack(side=TOP,fill=X)

				Detail_Frame=Frame(f3,bd=4,relief=RIDGE,bg="purple")
				Detail_Frame.place(x=8,y=100,width=385,height=200)
				scroll_x=Scrollbar(Detail_Frame,orient=HORIZONTAL)
				scroll_y=Scrollbar(Detail_Frame,orient=VERTICAL)
				List_Table=ttk.Treeview(Detail_Frame,columns=("1","2","3","4","5"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
				scroll_x.pack(side=BOTTOM,fill=X)
				scroll_y.pack(side=RIGHT,fill=Y)
				scroll_x.config(command=List_Table.xview)
				scroll_y.config(command=List_Table.yview)
				List_Table.heading("1",text="ID")
				List_Table.heading("2",text="Name")
				List_Table.heading("3",text="Department")
				List_Table.heading("4",text="Contact No")
				List_Table.heading("5",text="Status")
				List_Table['show']='headings'
				List_Table.column("1",width=20)
				List_Table.column("2",width=100)
				List_Table.column("3",width=100)
				List_Table.column("4",width=100)
				List_Table.column("5",width=100)
				List_Table.pack(fill=BOTH,expand=1)

				f1.tkraise()
				window2.mainloop()

			break
		else:
			messagebox.showerror("Error","invalid username or password")
			break



#======================MainLoginScreen============================================
window=Tk()
window.title("Login Panel")
Label1=Label(window,text="Login Panel",font=("arial",20,"bold"),bg="grey19",fg="white")
Label1.pack(side=TOP,fill=X)
Label2=Label(window,text="Project by Code Eater's",font=("arial",10,"bold"),bg="grey19",fg="white")
Label2.pack(side=BOTTOM,fill=X)
#====================LoginandSignupTabs====================================
nb=ttk.Notebook(window)
tab1=ttk.Frame(nb)
tab2=ttk.Frame(nb)
nb.add(tab1,text="Login")
nb.add(tab2,text="Sign_up")
nb.pack(expand=True,fill="both")
#=============Logintab=========================================
name2_label=Label(tab1,text="Name",font=("arial",10,"bold"))
name2_label.place(x=10,y=10)
name2_entry=StringVar()
name2_entry=ttk.Entry(tab1,textvariable=name2_entry)
name2_entry.place(x=90,y=10)
name2_entry.focus()

pass2_label=Label(tab1,text="Password",font=("arial",10,"bold"))
pass2_label.place(x=10,y=40)
pass2_entry=StringVar()
pass2_entry=ttk.Entry(tab1,textvariable=pass2_entry,show="*")
pass2_entry.place(x=90,y=40)


#=====================SignupTab===============================
name_label=Label(tab2,text="Name",font=("arial",10,"bold"))
name_label.place(x=10,y=10)
name_entry=StringVar()
name_entry=ttk.Entry(tab2,textvariable=name_entry)
name_entry.place(x=90,y=10)
name_entry.focus()
pass_label=Label(tab2,text="Password",font=("arial",10,"bold"))
pass_label.place(x=10,y=40)
pass_entry=StringVar()
pass_entry=ttk.Entry(tab2,textvariable=pass_entry,show="*")
pass_entry.place(x=90,y=40)

def clear():
	name_entry.delete(0,END)
	pass_entry.delete(0,END)
#===============AddUserButtons==============================================
btn1=ttk.Button(tab2,text="Add User",command=saveadmin)
btn1.place(x=50,y=80)
btn2=ttk.Button(tab2,text="Clear",command=clear)
btn2.place(x=140,y=80)
#================LoginButtonMainwindow1======================================
btn3=ttk.Button(tab1,text="Login",width=20,command=loggin)
btn3.place(x=87,y=80)


window.geometry("400x400+420+170")
window.resizable(False, False)
window.mainloop()