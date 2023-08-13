from tkinter import *
def canvascreate():
    root2 = Tk()
    root2.geometry("100x100")
    root2.mainloop()
    canvas = Canvas(root2, width = 100, height = 100, bg = "green")
    canvas.pack()
root = Tk()
root.geometry("500x500")
btn_cnv = Button(root, width = 10, height = 10, text = "Канвас", command=canvascreate)
btn_cnv.pack()
root.mainloop()
