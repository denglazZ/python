from tkinter import*
root=Tk()
canvas = Canvas(root,width=640,height=480)
canvas.pack()

#дом
canvas.create_rectangle(40,240,280,400,fill="bisque")
canvas.create_polygon(40,240,160,160,280,240,fill="saddle brown")
canvas.create_oval(140,180,180,220,fill="light cyan")

#canvas.create_line(40,240,160,160)
#canvas.create_line(160,160,280,240)

#машина
canvas.create_rectangle(320,320,460,400,fill="saddle brown")
canvas.create_rectangle(460,240,540,400,fill="blue")
canvas.create_rectangle(540,320,600,400,fill="blue")
canvas.create_rectangle(480,260,520,300,fill="light cyan")
canvas.create_oval(330,370,390,430,fill="gray")
canvas.create_oval(340,380,380,420,fill="black")
canvas.create_oval(530,370,590,430,fill="gray")
canvas.create_oval(540,380,580,420,fill="black")


root.mainloop()




