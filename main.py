from turtle import Turtle, Screen
from random import *

duma_turtle = Turtle()
duma_turtle.shape('turtle')
duma_screen = Screen()
duma_screen.colormode(255)

# Drawing a square
# for duma in range(4):
#     duma_turtle.forward(100)
#     duma_turtle.left(90)

# # Drawing a dashed line 15 times
# for duma in range(15):
#     duma_turtle.forward(10)
#     duma_turtle.penup()
#     duma_turtle.forward(10)
#     duma_turtle.pendown()

# Drawing different shapes starting from triangle to nonagon
# for sides in range(3, 10):
#     duma_turtle.color(choice(colors))
#     sides_left_to_be_drawn = sides
#     while sides_left_to_be_drawn > 0:
#         duma_turtle.forward(100)
#         duma_turtle.left(180 - (180 * (sides - 2) / sides))
#         sides_left_to_be_drawn -= 1

# Random Walk - thicker lines, different color each time
# duma_turtle.pensize(10)
# duma_turtle.ht()
duma_turtle.speed(10)


def random_color():
    """Use RGB settings to determine color"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# for duma in range(200):
#     duma_turtle.pencolor(random_color())
#     direction = choice([90, 180, 270, 360])
#     duma_turtle.left(direction)
#     duma_turtle.forward(20)

# Draw a spirograph
def draw_spirograph(tilt_angle, radius):
    tilt_angle = tilt_angle
    new_tilt = 0
    for duma in range(int(360 / tilt_angle)):
        duma_turtle.pencolor(random_color())
        duma_turtle.circle(radius)
        new_tilt += tilt_angle
        duma_turtle.setheading(new_tilt)


draw_spirograph(10, 100)

duma_screen.exitonclick()
