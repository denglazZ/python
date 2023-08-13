from tkinter import *


def button1():
    cnv.create_rectangle(50, 50, 200, 200, fill="red")


def button2():
    sc2 = Tk()
    sc2.mainloop()


sc = Tk()
sc.geometry("600x1500")
sc.title("hello")
# канвас 1
cnv = Canvas(sc, width=300, height=200, bg="green")
cnv.pack()
cnv.place(x=200, y=50)
# кнопка 1
btn1 = Button(sc, background="black", width=5, height=5, command=button1)
btn1.pack()
btn1.place(x=0, y=200)
# кнопка 2
btn2 = Button(sc, background="green", width=5, height=5, command=button2)
btn2.pack
btn2.place(x=100, y=200)
sc.mainloop()