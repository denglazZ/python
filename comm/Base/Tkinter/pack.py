from tkinter import *

def click(event):
    x = event.x
    y = event.y
    cnv.create_rectangle(x-100,y-100,x+100,y+100,fill="blue")
sc = Tk()
sc.geometry("2000x1500")
sc.title("hello")
cnv = Canvas(sc, width = 2000, height=1500, bg="green")
cnv.create_rectangle(90,90,90,90)
cnv.pack()
cnv.place(x=200,y=50)
cnv.bind("<Button - 1>", click)
sc.mainloop()