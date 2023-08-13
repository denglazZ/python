from tkinter import*
root=Tk()
root.geometry('800x800')

def kvadrat(event):
    canvas.create_rectangle(10,300,100,390,fill="red")

def oval(event):
    canvas.create_oval(150,300,240,390,fill="blue")

def polygon(event):
    canvas.create_polygon(300,390,350,300,400,390,fill="green")

btn_1 = Button(root,text="Квадрат")
btn_1.pack()
btn_1.place(x=100,y=10)
btn_1.bind("<Button-1>",kvadrat)

btn_2 = Button(root,text="Круг")
btn_2.pack()
btn_2.place(x=200,y=10)
btn_2.bind("<Button-1>",oval)

btn_3 = Button(root,text="Треугольник")
btn_3.pack()
btn_3.place(x=300,y=10)
btn_3.bind("<Button-1>",polygon)

canvas=Canvas(root,width=640,height=480)
canvas.pack()
canvas.place(x=100,y=100)
canvas.create_rectangle(5,5,640,480)

root.mainloop()



