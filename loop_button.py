import tkinter as tk
def click(data):
    print("clickevent", data)
 
def other():
    app = tk.Tk()
    frame = tk.Frame(app)
    frame.pack()
 
    buttons = []
    for x in range(10):
        b = tk.Button(frame, text='Button ' + str(x), command=lambda: click(x))
        b.pack()
        buttons.append(b)
 
    app.mainloop()
 
other()
