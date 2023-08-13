import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox

def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)

def file_save():
    name=asksaveasfile(mode='w',defaultextension=".txt")
    text2save=str(text.get(0.0,END))
    name.write(text2save)
    name.close

def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Error", message="Saving file error....")

def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name

    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def info():
    messagebox.showinfo("Information", "Simple Text editor\nby CoderLog")

root = tkinter.Tk()
root.title("Simple Text editor")
root.minsize(width=500, height=400)
root.maxsize(width=500, height=400)
text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)
text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="New", command= new_file)
fileMenu.add_command(label="Open", command= open_file)
fileMenu.add_command(label="Save", command = file_save)
fileMenu.add_command(label="Save as")
menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Information")
menuBar.add_cascade(label="Exit", command=root.quit)
menuBar.add_cascade()
root.config(menu=menuBar)
root.mainloop()
FILE_NAME = tkinter.NONE

