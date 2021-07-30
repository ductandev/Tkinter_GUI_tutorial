from threading import Thread
from tkinter import *    

def start_motor(event):
    global running
    print("starting motor...")
    running = True

def stop_motor(event):
    global running
    running = False
    print("stopping motor...")

def move_forward():
    while True: # Thread will run infinitely in the background
        if running:
            print("Car is moving forward...")

running = False
root = Tk()

button = Button(root, text ="forward")
button.pack(side=LEFT)
button.bind('<ButtonPress-1>',start_motor)
button.bind('<ButtonRelease-1>',stop_motor)

# Create and start the new thread
t = Thread(target = move_forward, args = ())
t.start()

root.mainloop()
