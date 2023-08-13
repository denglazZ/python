from tkinter import *
 
root = Tk()
root.geometry('600x600')

def click_left(event):
    x = event.x
    y = event.y
    print("x:", x)
    print("y:", y)
    if var.get()==0:
        r=1
    elif var.get()==1:
        r=20
    else:
        r=40
    canvas.create_oval(x-r,y-r,x+r,y+r)

def clean(event):
    canvas.delete('all')
    canvas.create_rectangle(5,5,480,320)


btn_1 = Button(root,text="Очистить")
btn_1.pack()
btn_1.place(x=100,y=10)
btn_1.bind("<Button-1>",clean)

var=IntVar()
var.set(0)
r_1=Radiobutton(text=" 1 ",variable=var,value=0)
r_1.pack()
r_2=Radiobutton(text="20",variable=var,value=1)
r_2.pack()
r_3=Radiobutton(text="40",variable=var,value=2)
r_3.pack()

canvas = Canvas(root,width=480,height=320)
canvas.pack()
canvas.place(x=100,y=200)
canvas.create_rectangle(5,5,480,320)
 
canvas.bind("<Button-1>",click_left)

root.mainloop()

