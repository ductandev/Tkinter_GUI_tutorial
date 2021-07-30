from tkinter import *
from PIL import Image, ImageTk

def callback():
    print("click!")

root = Tk()
root.geometry("250x250")

width = 100
height = 100
img = Image.open("landscape.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)

b = Button(root,image=photoImg, command=callback)
b.pack(anchor=CENTER, expand=True)

c = Label(root, text="click me")
c.place(x=100, y=200)

root.bind('<Escape>', lambda e: root.quit())		# Nhấn Nút ESC Để Thoát
mainloop()
