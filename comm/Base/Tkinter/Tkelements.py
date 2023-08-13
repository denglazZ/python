from tkinter import *

def Btn_click(event):
    x=event.x
    y=event.y
    r=var_set.get()
    cnv.create_oval(x-r,y-r,x+r,y+r, fill = "black")
    print(f"x = {x}, y = {y}")

sc = Tk()
sc.geometry("400x500")
sc.configure(background="#66ff00")
sc.title("Sergio")

cnv = Canvas(sc, width=400, height=400)
cnv.pack()
cnv.bind("<Button-1>", Btn_click)
var_set=IntVar()
scl = Scale(sc,from_=1, to=10, length= 1000, orient=HORIZONTAL,variable=var_set)
scl.pack()
sc.mainloop()