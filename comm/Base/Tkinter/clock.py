import time
from tkinter import *

def Clock():
    global x1,y1
    canvas.delete("all")
    canvas.create_line(250, 250, x1, y1)
    x1 += 10
    y1 -= 10
    time.sleep(1)
sc = Tk()
sc.geometry("500x500")
x1 = 400
y1 = 400
canvas = Canvas(sc,width=500,height=500)
while(True):
    Clock()
    canvas.pack()
    sc.mainloop()



canvas.pack()
sc.mainloop()
