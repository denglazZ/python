from tkinter import *
'''
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

python_lang = IntVar()
python_checkbutton = Checkbutton(text="Python", variable=python_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10)
python_checkbutton.grid(row=0, column=0, sticky=W)

javascript_lang = IntVar()
javascript_checkbutton = Checkbutton(text="JavaScript", variable=javascript_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
javascript_checkbutton.grid(row=1, column=0, sticky=W)

root.mainloop()

from tkinter import *
color_fill = "black"
coins = 10
def clean(event):
    canvas.delete('all')
def mouse_move(event):
    global color_fill, coins
    coins -= 1
    print(coins)
    x = event.x
    y = event.y
    r = var_scale.get()
    if (coins > 0):
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color_fill, outline="")


root = Tk()
root.geometry("600x600")
var_scale=IntVar()
scale = Scale(root,from_=0, to=200, length=200, orient=HORIZONTAL, variable=var_scale)
scale.pack()
canvas = Canvas(root, width=500, height=500, background="Grey")
canvas.pack()
canvas.bind("<Button - 1>",mouse_move)
btncln = Button(root,width=10,height=10, text="Очистить")
btncln.pack()
btncln.bind("<Button-1>", clean)
root.mainloop()
'''
sc = Tk()
sc.geometry("600x600")
def mouse_coordinate(event):
    x = event.x
    y = event.y
    r = var_scale.get()
    print("x", x)
    print("y", y)
canvas = Canvas(sc, width=600, height=600, background="Grey")
canvas.pack()
canvas.bind("<Button-1>",mouse_coordinate)
var_scale=IntVar()
scale = Scale(sc,from_=0, to=200, length=200, orient=HORIZONTAL, variable=var_scale)
scale.pack()
canvas.create_line(40,240,280,400,fill="Cyan")
canvas.create_polygon(40,240,160,160,280,240,fill="saddle brown")
canvas.create_oval(140,180,180,220,fill="light cyan")
sc.mainloop()