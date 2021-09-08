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

filePath = ''

def runCode():
    global filePath
    if filePath == '':
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="You did not save the file, Please save the file first.")
        msg.pack()
        return
    command = f'python {filePath}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    consoleResult, error = process.communicate()
    console.insert('1.0',consoleResult)
    console.insert('1.0',error)
     
""" Allowing the user to select a file to open. """
def openFile():
    # Using module to display a file open dialog and store the selected file path to filepath.
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    if not path:
        return
    # Clearing the current contents of textEditor using delete() method
    textEditor.delete("1.0", END)
    with open(path, 'r') as file:
        code = file.read()
        textEditor.delete('1.0', END)
        # Assigning the string code to textEditor using insert() method
        textEditor.insert('1.0', code)
        global filePath
        filePath = path

"""Saving the current file as a new file."""
def saveFile():
    global filePath
    if filePath =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = filePath    
    # Creating a new file at the selected file path
    with open(path, 'w') as file:
        code = textEditor.get('1.0', END)
        # Writing code to the output file
        file.write(code)

# Defining and Configurating textEditor
textEditor = Text()
textEditor.config(background='#3d3736', foreground='#c4d1c2', insertbackground='white')
textEditor.pack()

# Defining and Configurating Console
console = Text(height=7)
console.config(background='#3d3736', foreground='#2acc14')
console.pack()
 
menuBar = Menu(window)

fileBar = Menu(menuBar, tearoff=0)
fileBar.add_command(label='Open', command = openFile)
fileBar.add_command(label='Save', command = saveFile)
fileBar.add_command(label='SaveAs', command = saveFile)
menuBar.add_cascade(label='File', menu = fileBar)

runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='Run', command = runCode)
menuBar.add_cascade(label='Run', menu = runBar)

editBar = Menu(menuBar, tearoff=0)  
editBar.add_command(label="Undo")  
  
editBar.add_separator()  
  
editBar.add_command(label="Cut")  
editBar.add_command(label="Copy")  
editBar.add_command(label="Paste")  
editBar.add_command(label="Delete")  
editBar.add_command(label="Select All")  
menuBar.add_cascade(label="Edit", menu=editBar)  

helpBar = Menu(menuBar, tearoff=0)  
helpBar.add_command(label="About")  
menuBar.add_cascade(label="Help", menu=helpBar)  

menuBar.add_command(label='Exit', command = exit)

window.config(menu=menuBar)

# Infinite loop can be terminated by keyboard or mouse interrupt
window.mainloop()