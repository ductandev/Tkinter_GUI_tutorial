from tkinter import *


def input():
    uInput = uEntry.get()
    print(uInput)
    return


window = Tk()
window.title("Enter your username and Password")

Label(window, text="Username").grid(row=0)
Label(window, text="Password").grid(row=1)

uEntry = Entry(window, fg="White", bg="Black")
uEntry.grid(row=0, column=1)
pEntry = Entry(window, fg="White", bg="Black")
pEntry.grid(row=1, column=1)
eButton = Button(window, text="Enter input", command=input).grid(row=2, column=1)


window.mainloop()
