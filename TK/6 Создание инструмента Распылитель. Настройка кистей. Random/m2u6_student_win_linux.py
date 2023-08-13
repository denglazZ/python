from tkinter import*

color_fill="black"

def move_left(event):
    x = event.x
    y = event.y
    r=var_scale.get()
    if var_radio.get()==0:
        global color_fill
        color_fill="white"
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color_fill, outline="")
    else:
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color_fill, outline="")

def click_left(event):
    x = event.x
    y = event.y
    r=var_scale.get()
    if var_radio.get()==0:
        global color_fill
        color_fill="white"
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color_fill, outline="")
    else:
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

canvas=Canvas(root,width=480,height=300, bg = "White")
canvas.pack()
canvas.place(x=40,y=170)

canvas.bind("<B1-Motion>",move_left)
canvas.bind("<Button-1>",click_left)

var_radio=IntVar()
var_radio.set(1)
r_1=Radiobutton(text="Ластик",variable=var_radio,value=0)
r_1.configure(background='light gray')
r_1.pack()
r_1.place(x=10,y=30)

r_2=Radiobutton(text="Кисть",variable=var_radio,value=1)
r_2.configure(background='light gray')
r_2.pack()
r_2.place(x=10,y=50)


var_scale=IntVar()
scale = Scale(root,from_=3, to=200, length=150, orient=HORIZONTAL, resolution=5, variable=var_scale)
scale.pack()
scale.place(x=10,y=125)

btn_1 = Button(root, text="Очистить")
btn_1.configure(width=7,height=1)
btn_1.pack()
btn_1.place(x=520,y=30)
btn_1.bind("<Button-1>",clean)

btn_2 = Button(root, text="Зеленый")
btn_2.configure(background="green")
btn_2.pack()

btn_2.place(x=375,y=30)
btn_2.bind("<Button-1>",color_green)

btn_3 = Button(root, text="Красный")
btn_3.configure(background="red")
btn_3.pack()

btn_3.place(x=375,y=55)
btn_3.bind("<Button-1>",color_red)

btn_4 = Button(root, text="Синий")
btn_4.configure(background="blue")
btn_4.pack()

btn_4.place(x=445,y=30)
btn_4.bind("<Button-1>",color_blue)

btn_5 = Button(root, text="Черный")
btn_5.configure(background="gray")
btn_5.pack()

btn_5.place(x=445,y=55)
btn_5.bind("<Button-1>",color_black)

root.mainloop()