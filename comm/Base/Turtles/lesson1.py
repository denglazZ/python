import turtle

screen = turtle.Screen()  # графическое окно

pen = turtle.Turtle()     # графический объект
pen.width(5)
pen.color("green")
pen.shape("turtle")
for i in range(37):
    pen.forward(100)
    pen.left(+10)

screen.mainloop()