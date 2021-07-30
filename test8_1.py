from tkinter import *  
  
top = Tk()  
top.geometry("300x350")  
  
lbl = Label(top,text = "A list of favourite countries...")  
lbl.pack() 
 
listbox = Listbox(top)  
listbox.insert(1,"India")  
listbox.insert(2, "USA")  
listbox.insert(3, "Japan")  
listbox.insert(4, "Austrelia")  
listbox.pack()
#this button will delete the selected item from the list   
  
btn = Button(top, text = "delete", command = lambda listbox=listbox: listbox.delete(ANCHOR))  
btn.pack()   

top.mainloop()  
