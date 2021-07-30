import cv2
from PIL import Image
from PIL import ImageTk
import threading
import tkinter as tk


def button1tkclicked(videolooptkstop):
    threading.Thread(target=videoLoop, args=(videolooptkstop,)).start()


def button2tkclicked(videolooptkstop):
    videolooptkstop[0] = True
    threading.Thread(target=videoLoop, args=(videolooptkstop,)).close()

def videoLoop(mirror=False):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAPtkPROPtkFRAMEtkWIDTH, 400)
    cap.set(cv2.CAPtkPROPtkFRAMEtkHEIGHT, 400)

    while True:
        ret, totkdraw = cap.read()
        if mirror is True:
            totkdraw = totkdraw[:, ::-1]

        image = cv2.cvtColor(totkdraw, cv2.COLORtkBGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        panel = tk.Label(image=image)
        panel.image = image
        panel.place(x=50, y=50)

        # check switcher value
        if videolooptkstop[0]:
            # if switcher tells to stop then we switch it again and stop videoloop
            videolooptkstop[0] = False
            panel.destroy()
            break


# videolooptkstop is a simple switcher between ON and OFF modes
videolooptkstop = [False]

root = tk.Tk()
root.geometry("800x700+0+0")

button1 = tk.Button(root, text="start", bg="#fff", font=("", 14),command=lambda: button1tkclicked(videolooptkstop))
button1.place(x=400, y=450, width=80, height=80)

button2 = tk.Button(root, text="stop", bg="#fff", font=("", 14),command=lambda: button2tkclicked(videolooptkstop))
button2.place(x=400, y=560, width=80, height=80)

root.mainloop()
