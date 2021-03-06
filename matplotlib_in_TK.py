from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
  
# plot function is created for 
# plotting the graph in 
# tkinter window
def plot():
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),dpi = 100)
	
    # list of squares
    y = [i**2 for i in range(101)]
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

window = Tk()
window.title('Plotting in Tkinter')
window.geometry("700x700")
  
plot_button = Button(master = window,  command = plot,height = 2, width = 10,text = "Plot")
plot_button.pack()

window.mainloop()
