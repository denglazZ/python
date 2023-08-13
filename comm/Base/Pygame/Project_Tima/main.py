import play
from time import sleep
player = play.new_image(image= r"~\Images\марио.jpg",x=-250,y=-100,size=10)

terra1 = play.new_line(x=-300,y=-200,thickness=20,length=200)

terra2 = play.new_line(x=-100,y=-100,thickness=20,length=100)


jump = False
collide = False
temp_y = 0
@play.repeat_forever
def player_go():
    global jump, collide
    if play.key_is_pressed("d"):
        player.x += 5
    if play.key_is_pressed("a"):
        player.x -= 5
    if player.is_touching(terra1):
        collide = True
    else:
        collide = False
    if play.key_is_pressed("w"):
        jump = True
        temp_y = player.y
    if temp_y + 150 > player.y:
        jump = False



@play.repeat_forever
def Jump_player():
    global jump
    if jump:
        player.y += 1





play.start_program()