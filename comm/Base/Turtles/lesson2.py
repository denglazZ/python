import turtle


def border():
    width, height = 300, 300
    mark.up()
    mark.goto(width // -2, height // 2)
    mark.down()
    i = 4
    while i > 0:
        mark.fd(width)
        mark.rt(90)
        mark.fd(height)
        mark.rt(90)
        i -= 1
    mark.write("GAME", font=("Consolas", 20, "normal"))


def move_right():
    x = player.xcor()
    x += 5
    player.setx(x)


def move_left():
    x = player.xcor()
    x -= 5
    player.setx(x)


def enemy_move():
    global enemy_speed
    x = enemy.xcor()
    y = enemy.ycor()
    if enemy.xcor() >= 100 or enemy.xcor() <= -100:
        enemy_speed *= -1
        y -= 10
    x += enemy_speed
    enemy.setx(x)
    enemy.sety(y)


enemy_speed = 5

screen = turtle.Screen()

mark = turtle.Turtle()
mark.speed(0)
mark.ht()

player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("green")
player.seth(90)
player.up()
player.goto(0, -100)

enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("triangle")
enemy.color("red")
enemy.seth(-90)
enemy.up()
enemy.goto(0, 100)

border()

screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.listen()

while 1:
    enemy_move()

screen.mainloop()