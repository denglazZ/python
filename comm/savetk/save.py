from tkinter import*
from random import *
import PIL
from PIL import Image, ImageDraw

color_fill="black"
image_number = 0

def save(event):
    global image_number
    filename=str(image_number)
    image1.save(filename+".png")
    image_number += 1

def paint_mouse(event):
    draw = ImageDraw.Draw(image1)
    x = event.x
    y = event.y
    r = 5
    canvas.create_rectangle(x + r, y + r, x - r, y - r, fill=color_fill, outline="")
    #draw.rectangle((x + r, y + r, x - r, y - r), width=10, fill = color_fill)
    #draw.polygon((x,y-5,x-5,y+5,x+5,y+5),fill=color_fill)
    #draw.ellipse((x-10,y-10,x+20,y+20), fill =color_fill, outline =color_fill)


root=Tk()
root.geometry('640x480')
root.configure(background="light gray")

image1 = Image.new('RGB', (640, 300), 'white')

canvas=Canvas(root,width=640,height=300)
canvas.pack()
canvas.place(x=0,y=170)

canvas.bind("<B1-Motion>",paint_mouse)
canvas.bind("<Button-1>",paint_mouse)

btn_6 = Button(root, text="Сохранить")
btn_6.configure(width=8,height=1)
btn_6.pack()
btn_6.place(x=520,y=140)
btn_6.bind("<Button-1>",save)

root.mainloop()