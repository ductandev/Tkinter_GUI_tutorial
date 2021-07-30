import os, sys

if sys.version_info[0] == 3:
    from tkinter import *
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter.ttk import *
elif sys.version_info[0] == 2:
    print ("The Script is written for Python 3.6.4 might give issues with python 2.7, let the author know")
    print ("Note Python 2.7 CSV has a empty line between each result. couldn't find a fix for that")
    from Tkinter import *
    import tkMessageBox as messagebox
    import tkFileDialog as filedialog
    from ttk import Combobox

class temp:
    def __init__():
        top = Tk()
        lab = Label(top, text='UserFiled')
        en = Entry(top, width =25)
        but = Button(top, text='Submit',command = chooseFolder)
        lab.grid(row=0, column=0)
        en.grid(row=0, column=1)
        but.grid(row=0, column=2)
        top.mainloop()
    def chooseFolder():
        directory = filedialog.askdirectory()
        print(directory)
        newPath = os.path.join(directory, en.get())
        if not os.path.exists(newPath):
            os.chdir(directory)				# thay đổi thư mục làm việc hiện tại thành đường dẫn đã chỉ định
            os.mkdir(en.get())

obj = temp()
