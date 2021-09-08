# Importing Tkinter modules
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess


# Creating master Tkinter window
window = Tk()

# Creating object of PhotoImage class
icon = PhotoImage(file = 'PyIdle-Icon.png')

# Setting title of  window
window.title('PyIdle')

# Setting icon of  window
window.iconphoto(False, icon)

# Infinite loop can be terminated by keyboard or mouse interrupt
window.mainloop()