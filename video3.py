#This Python program is developed in order to open an internal camera and display the image within Tkinter window.

#importing modules required
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np

global last_frame
last_frame = np.zeros((480, 640, 3), dtype=np.uint8)	#(dài, rộng, 3)
cap = cv2.VideoCapture(0)

def show_frame():										# creating a function
	if not cap.isOpened():								# checks for the opening of camera
		print("-------------cant open the camera----------")
		root.quit()
		
	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)
	if ret is None:
		print("Major error!")
	elif ret:
		global last_frame
		last_frame = frame.copy()

	cv2image = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	show_video_label.image = imgtk
	show_video_label.configure(image=imgtk)
	show_video_label.after(10, show_frame)

if __name__ == '__main__':
	root = Tk()											# assigning root variable for Tkinter as tk
	show_video_label = Label(master=root)
	show_video_label.grid(column=0, rowspan=4, padx=5, pady=5)
	root.title("Sign Language Processor")				# you can give any title
	show_frame()
	root.bind('<Escape>', lambda e: root.quit())		# Nhấn Nút ESC Để Thoát
	root.mainloop()										# keeps the application in an infinite loop so it works continuosly
	#cap.release()
