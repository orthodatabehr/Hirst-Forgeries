from turtle import Turtle, Screen
import random as r

duma_turtle = Turtle()
duma_turtle.shape('turtle')
duma_screen = Screen()
duma_screen.colormode(255)
duma_turtle.speed(10)
duma_turtle.hideturtle()

# Initial Extract of colors from image of choice
# import colorgram as cg
#
# colors = cg.extract('Emerald.jpg', 30)
# color_rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_rgb.append(new_color)
#
# print(color_rgb)

color_list = [(0, 47, 1), (0, 107, 11), (2, 143, 43), (2, 210, 124), (17, 13, 2), (0, 251, 198), (12, 252, 194),
              (20, 3, 10), (24, 235, 160), (4, 6, 13), (53, 84, 19), (67, 76, 57), (0, 239, 249), (10, 236, 252)]
#
# # Drawing a 10x10 dot painting with size 20 dots spaced out by 50
duma_turtle.setheading(180)
duma_turtle.penup()
start_x = 200
start_y = -200

for dumatery in range(10):
    duma_turtle.setpos(start_x, start_y)
    start_y += 50
    for duma in range(10):
        duma_turtle.pendown()
        duma_turtle.dot(20, r.choice(color_list))
        duma_turtle.penup()
        duma_turtle.forward(50)

duma_screen.exitonclick()
