from tkinter import*

color_fill="black"

def move_left(event):
    x = event.x
    y = event.y
    if var.get()==0:
        r=5
    elif var.get()==1:
        r=20
    else:
        r=40
    global color_fill
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=color_fill, outline="")

def clean(event):
    canvas.delete('all')

def color_green(event):
    global color_fill
    color_fill="green"


def color_red(event):
    global color_fill
    color_fill="red"

def color_blue(event):
    global color_fill
    color_fill="blue"

def color_black(event):
    global color_fill
    color_fill="black"

root=Tk()
root.geometry('640x480')
root.configure(background="light gray")

btn_1 = Button(root, text="Очистить")
btn_1.pack()

btn_1.place(x=10,y=10)
btn_1.bind("<Button-1>",clean)

btn_2 = Button(root, text="Зеленый")
btn_2.configure(background="green")
btn_2.pack()

btn_2.place(x=10,y=100)
btn_2.bind("<Button-1>",color_green)

btn_3 = Button(root, text="Красный")
btn_3.configure(background="red")
btn_3.pack()

btn_3.place(x=10,y=130)
btn_3.bind("<Button-1>",color_red)

btn_4 = Button(root, text="Синий")
btn_4.configure(background="blue")
btn_4.pack()

btn_4.place(x=10,y=160)
btn_4.bind("<Button-1>",color_blue)

btn_5 = Button(root, text="Черный")
btn_5.configure(background="gray")
btn_5.pack()

btn_5.place(x=10,y=190)
btn_5.bind("<Button-1>",color_black)


var=IntVar()
var.set(0)
r_1=Radiobutton(text=" 5 ",variable=var,value=0)
r_1.configure(background='light gray')
r_1.pack()

r_2=Radiobutton(text="20",variable=var,value=1)
r_2.configure(background='light gray')
r_2.pack()

r_3=Radiobutton(text="40",variable=var,value=2)
r_3.configure(background='light gray')
r_3.pack()

canvas=Canvas(root,width=480,height=320)
canvas.pack()
canvas.place(x=80,y=100)

canvas.bind("<B1-Motion>",move_left)

root.mainloop()