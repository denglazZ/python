from tkinter import *


def painting(event):
    global colorfill
    x = event.x
    y = event.y
    r = 100
    cnv.create_rectangle(x - r, y - r, x+r, y+r, fill=colorfill, outline="white")


def button2():
    global colorfill
    colorfill = "green"

def button2():
    global colorfill
    colorfill = "green"

def button3():
    global colorfill
    colorfill = "blue"

colorfill = "black"
sc = Tk()
sc.geometry("600x1500")
sc.title("hello")
# канвас 1
cnv = Canvas(sc, width=1000, height=1000, bg="white")
cnv.pack()
cnv.place(x=200, y=50)
cnv.bind("<B1-Motion>", painting)
# кнопка 1
btn1 = Button(sc, background="blue", width=5, height=5, command=button3)
btn1.pack()
btn1.place(x=0, y=200)
# кнопка 2
btn2 = Button(sc, background="green", width=5, height=5, command=button2)
btn2.pack
btn2.place(x=100, y=200)
sc.mainloop()