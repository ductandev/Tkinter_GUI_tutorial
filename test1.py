from tkinter import *  

tk = Tk()  

redbutton = Button(tk, text = "Red", fg = "red")  
redbutton.pack( side = LEFT)  

blackbutton = Button(tk, text = "Black", fg = "black")  
blackbutton.pack( side = RIGHT )  

bluebutton = Button(tk, text = "Blue", fg = "blue")  
bluebutton.pack( side = TOP )  

greenbutton = Button(tk, text = "Green", fg = "green")  
greenbutton.pack( side = BOTTOM)  

tk.mainloop()  

