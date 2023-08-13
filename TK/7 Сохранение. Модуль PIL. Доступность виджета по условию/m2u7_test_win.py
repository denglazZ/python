from tkinter import*
from random import*
from PIL import Image, ImageDraw

color_fill="black"
image_number = 0

def vis_scale(event):
    if var_radio.get()==2:
        scale_2.place(x=200,y=125)
        print(var_radio.get())
    else:
        scale_2.place_forget()


#возможен и такой варинат функции в супер дополнительном задании
def save(event):
    global image_number
    filename=str(image_number) 
    image1.save(filename+".png")
    image_number += 1

def paint_mouse(event):
    x = event.x
    y = event.y
    r=var_scale.get()
    dR=var_scale_2.get()
    
    if var_radio.get()==0:
        global color_fill
        color_fill="white"
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color_fill, outline="")
    elif ((var_radio.get()==1) and (var_radio_shape.get()==1)):
        canvas.create_rectangle(x+r,y+r,x-r,y-r,fill=color_fill,outline="")
        draw.rectangle((x+r,y+r,x-r,y-r),fill=color_fill)
    elif ((var_radio.get()==1) and (var_radio_shape.get()==2)):
        canvas.create_rectangle(x,y+r,x,y-r,fill=color_fill,outline="")
        draw.rectangle((x+r,y+r,x-r,y-r),fill=color_fill)
    elif ((var_radio.get()==2) and (var_radio_shape.get()==0)):
        for i in range(randint(3,dR)):
            canvas.create_oval(x+randint(-r,r),y+randint(-r,r),x-randint(-r,r),y-randint(-r,r),fill=color_fill, outline="black")
            draw.ellipse((x+randint(-r,r),y+randint(-r,r),x-randint(-r,r),y-randint(-r,r)),fill=color_fill,width=1,outline="black")
    elif ((var_radio.get()==2) and (var_radio_shape.get()==1)):

        for i in range(randint(3,dR)):
            canvas.create_rectangle(x+randint(-r,r),y+randint(-r,r),x-randint(-r,r),y-randint(-r,r),fill=color_fill, outline="black")
            draw.rectangle((x+randint(-r,r),y+randint(-r,r),x-randint(-r,r),y-randint(-r,r)),fill=color_fill,width=1,outline="black")
    else:
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color_fill, outline="")
        draw.ellipse((x-r,y-r,x+r,y+r),fill=color_fill,width=1,outline=color_fill)

def clean(event):
    canvas.delete('all')

def color_green(event):
    global color_fill
    color_fill="green"
    btn_2.configure(state="normal")
    btn_3.configure(state="disabled")
    btn_4.configure(state="disabled")
    btn_5.configure(state="disabled")


def color_red(event):
    global color_fill
    color_fill="red"
    btn_2.configure(state="disabled")
    btn_3.configure(state="normal")
    btn_4.configure(state="disabled")
    btn_5.configure(state="disabled")

def color_blue(event):
    global color_fill
    color_fill="blue"
    btn_2.configure(state="disabled")
    btn_3.configure(state="disabled")
    btn_4.configure(state="normal")
    btn_5.configure(state="disabled")

def color_black(event):
    global color_fill
    color_fill="black"
    btn_2.configure(state="disabled")
    btn_3.configure(state="disabled")
    btn_4.configure(state="disabled")
    btn_5.configure(state="normal")


root=Tk()
root.geometry('640x480')
root.configure(background="light gray")

image1 = Image.new('RGB', (640, 300), 'white')
draw = ImageDraw.Draw(image1)

canvas=Canvas(root,width=640,height=300)
canvas.pack()
canvas.place(x=0,y=170)

canvas.bind("<B1-Motion>",paint_mouse)
canvas.bind("<Button-1>",paint_mouse)

lab_1 = Label(root,text="Инструменты")
lab_1.configure(background='light gray')
lab_1.pack()
lab_1.place(x=10,y=5)

var_radio=IntVar()
var_radio.set(1)
r_1=Radiobutton(text="Ластик",variable=var_radio,value=0,command=vis_scale)
r_1=Radiobutton(text="Ластик",variable=var_radio,value=0)
r_1.configure(background='light gray')
r_1.pack()
# r_1.bind("<Button-1>",vis_scale)
r_1.place(x=10,y=30)

r_2=Radiobutton(text="Кисть",variable=var_radio,value=1)
r_2=Radiobutton(text="Кисть",variable=var_radio,value=1,command=vis_scale)
r_2.configure(background='light gray')
r_2.pack()
# r_2.bind("<Button-1>",vis_scale)
r_2.place(x=10,y=50)

r_3=Radiobutton(text="Распылитель",variable=var_radio,value=2)
r_3=Radiobutton(text="Распылитель",variable=var_radio,value=2,command=vis_scale)
r_3.configure(background='light gray')
r_3.pack()
# r_3.bind("<Button-1>",vis_scale)
r_3.place(x=10,y=70)

lab_2 = Label(root,text="Форма")
lab_2.configure(background='light gray')
lab_2.pack()
lab_2.place(x=200,y=5)

var_radio_shape=IntVar()
var_radio_shape.set(0)
r_4=Radiobutton(text="Круг",variable=var_radio_shape,value=0)
r_4.configure(background='light gray')
r_4.pack()
r_4.place(x=200,y=30)

r_5=Radiobutton(text="Прямоугольник",variable=var_radio_shape,value=1)
r_5.configure(background='light gray')
r_5.pack()
r_5.place(x=200,y=50)

r_6=Radiobutton(text="Линия",variable=var_radio_shape,value=2)
r_6.configure(background='light gray')
r_6.pack()
r_6.place(x=200,y=70)


lab_3 = Label(root,text="Размер/Распыление")
lab_3.configure(background='light gray')
lab_3.pack()
lab_3.place(x=10,y=100)

var_scale=IntVar()
scale = Scale(root,from_=3, to=200, length=150, orient=HORIZONTAL, resolution=5, variable=var_scale)
scale.pack()
scale.place(x=10,y=125)

lab_4 = Label(root,text="Интенсивность")
lab_4.configure(background='light gray')
lab_4.pack()
lab_4.place(x=200,y=100)

var_scale_2=IntVar()
scale_2 = Scale(root,from_=3, to=20, length=150, orient=HORIZONTAL, resolution=3, variable=var_scale_2)
scale_2.place_forget()

lab_5 = Label(root,text="Палитра цвета")
lab_5.configure(background='light gray')
lab_5.pack()
lab_5.place(x=370,y=5)

btn_1 = Button(root, text="Очистить")
btn_1.configure(width=7,height=1)
btn_1.pack()
btn_1.place(x=520,y=30)
btn_1.bind("<Button-1>",clean)

btn_2 = Button(root, text="Зеленый")
btn_2.configure(background="green",width=7,height=1)
btn_2.pack()

btn_2.place(x=375,y=30)
btn_2.bind("<Button-1>",color_green)

btn_3 = Button(root, text="Красный")
btn_3.configure(background="red",width=7,height=1)
btn_3.pack()

btn_3.place(x=375,y=55)
btn_3.bind("<Button-1>",color_red)

btn_4 = Button(root, text="Синий")
btn_4.configure(background="blue",width=7,height=1)
btn_4.pack()
btn_4.place(x=445,y=30)
btn_4.bind("<Button-1>",color_blue)

btn_5 = Button(root, text="Черный")
btn_5.configure(background="gray",width=7,height=1)
btn_5.pack()
btn_5.place(x=445,y=55)
btn_5.bind("<Button-1>",color_black)

btn_6 = Button(root, text="Сохранить")
btn_6.configure(width=8,height=1)
btn_6.pack()
btn_6.place(x=520,y=140)
btn_6.bind("<Button-1>",save)

root.mainloop()