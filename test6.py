from tkinter import *
from functools import partial  

   
def call_result(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  
   
tk = Tk()
tk.geometry('400x200+100+200')  
tk.title('Calculator')  
   
number1 = StringVar()  
number2 = StringVar()  
  
labelNum1 = Label(tk, text="A").grid(row=1, column=0)  
labelNum2 = Label(tk, text="B").grid(row=2, column=0)  
  
labelResult = Label(tk)  
labelResult.grid(row=7, column=2)  
  
entryNum1 = Entry(tk, textvariable=number1).grid(row=1, column=2)  
entryNum2 = Entry(tk, textvariable=number2).grid(row=2, column=2)  
  
call_result = partial(call_result, labelResult, number1, number2)  
buttonCal = Button(tk, text="Calculate", command=call_result).grid(row=3, column=0)  
  
tk.mainloop()  
