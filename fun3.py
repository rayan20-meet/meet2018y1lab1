import turtle
turtle.goto(0,0)
DOWN = 1
LEFT = 2
RIGHT = 3
UP = 0
direction = None

def up():
    global direction
    direction = UP
    print("you pressed the up key.")
    on_move(10,20)

def down():
    global direction
    direction = DOWN
    print("you pressed the down key.")
    on_move(10,20)
def left():
    global direction
    direction = LEFT
    print("you pressed the left key.")
    on_move(10,20)

def right():
    global direction
    direction = RIGHT
    print("you pressed the right key.")
    on_move(10,20)
    
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.listen()

def on_move(x, y):
    turtlepos = turtle.position()
    turtlexpos = turtlepos[0]
    turtleypos = turtlepos[1]
    if direction==UP:
        turtle.goto(turtlexpos , turtleypos+y)
    if direction==DOWN:
        turtle.goto(turtlexpos , turtleypos-y)
    if direction==LEFT:
        turtle.goto(turtlexpos-x , turtleypos)
    if direction==RIGHT:
        turtle.goto(turtlexpos+x , turtleypos)    
