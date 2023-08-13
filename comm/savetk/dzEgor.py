from tkinter import *
from PIL import Image, ImageTk

def createroot(event):
    global pilImage
    pilImage = Image.open("../Base/Tkinter/0.png")


root = Tk()
root.geometry('1000x1000')
canvas = Canvas(root,width=999,height=999)
pilImage = Image.open("campus.png")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(400,400,image=image)
photo=PhotoImage(file="1.png")
#b.config(image=photo,width="400",height="400")
b=Button(root,justify = LEFT, bg="Green", width=5, height=5)
b.pack()
b.place(x=200, y = 150)
b.bind("<Button-1>", createroot)
b1=Button(root,justify = LEFT, bg="Red",width=5, height=5)
b1.pack()
b1.place(x=250, y = 150)
b1.bind("<Button-1>", createroot)
b2=Button(root,justify = LEFT, bg="Yellow",width=5, height=5)
b2.pack()
b2.place(x=300, y = 150)
b2.bind("<Button-1>", createroot)

canvas.pack()
root.mainloop()