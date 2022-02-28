from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("yellow")

t1 = Turtle()
t1.pencolor('blue')

t2 = Turtle()
t2.pencolor('pink')

def pattern(turtle, increment, angle):
    turtle.speed('fast')
    turtle.width(5)
    length = 10

    while length < 500:
        turtle.forward(length)
        turtle.right(angle)
        length += increment
        yield 0

generator1 = pattern(t1, 3, 89)
generator2 = pattern(t2, 4, -89)

while next(generator1, 1) + next(generator2, 1) < 2:
    pass

screen.exitonclick()