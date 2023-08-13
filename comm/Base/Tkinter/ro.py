from tkinter import *
from PIL import Image, ImageTk
def createroot():
    root = Tk()
    root.geometry('1000x1000')
    canvas = Canvas(root,width=999,height=999)
    pilImage = Image.open("campus.png")
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(400,400,image=image)
    photo=PhotoImage(file="1.png")
    canvas.pack()
    root.mainloop()
sc = Tk()
sc.geometry("600x600")
btn = Button(sc, width=10, height=10, command=createroot)
btn.pack()
sc.mainloop()