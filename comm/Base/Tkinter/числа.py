from tkinter import *
from tkinter import ttk

sc = Tk()
sc.geometry("200x200")

def click():
    print(combo.current())

combo = ttk.Combobox(sc,values=["January","February","March","April"])
combo.pack()
btn = Button(sc, text = "print")
btn.pack()
btn.bind("<Button - 1>", click)
sc.mainloop()