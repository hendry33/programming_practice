import turtle


def star(n):
    for i in range(n):
        turtle.forward(150)
        turtle.left(180-180/n)
star(7)
turtle.done()