from tkinter import *
color_fill = "black"
coins = 10

def clean(event):
    canvas.delete('all')

def forward(event):
    print("forward")

def back(event):
    print("back")

def mouse_move(event):
    global color_fill, coins
    print(coins)
    x = event.x
    y = event.y
    r = var_scale.get()
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=color_fill, outline="")
points = []
root = Tk()
root.geometry("600x600")
var_scale=IntVar()
scale = Scale(root,from_=50, to=200, length=200, orient=HORIZONTAL, variable=var_scale)
scale.pack()
canvas = Canvas(root, width=500, height=500, background="Grey")
canvas.pack()
canvas.bind("<Button-1>",mouse_move)
btncln = Button(root,width=10,height=10, text="Очистить")
btncln.pack()
btncln.bind("<Button-1>", clean)
root.mainloop()