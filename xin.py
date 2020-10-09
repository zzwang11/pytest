import turtle, time

turtle.screensize(400, 300, "black")
turtle.pensize(3)
sizehh = 1


def curve():
    for ii in range(200):
        turtle.right(1)
        turtle.forward(1 * sizehh)


turtle.speed(0)
turtle.color("red", "pink")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65 * sizehh)
curve()
turtle.left(120)
curve()
turtle.forward(111.65 * sizehh)
turtle.end_fill()
turtle.hideturtle()

turtle.pencolor('black')
turtle.left(140)
turtle.forward(100*sizehh)
turtle.pencolor('red')
# turtle.goto(100, 0)
turtle.showturtle()
turtle.speed(0)
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65 * sizehh)
curve()
turtle.left(120)
curve()
turtle.forward(111.65 * sizehh)
turtle.end_fill()
turtle.hideturtle()
time.sleep(2)
