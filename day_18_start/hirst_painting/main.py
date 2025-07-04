# import colorgram
import random
import turtle
from turtle import Turtle
# colors = colorgram.extract('hirst.png', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)
turtle.colormode(255)
rgb_list = [(203, 165, 107), (151, 73, 47), (52, 93, 125), (170, 153, 40), (222, 202, 136), (137, 31, 21), (132, 163, 185), (200, 91, 70), (48, 122, 88), (66, 47, 41), (14, 101, 72), (146, 178, 147), (235, 175, 165), (161, 142, 157), (108, 73, 77), (17, 86, 89), (184, 205, 173), (56, 46, 49), (38, 61, 75), (49, 65, 80), (148, 19, 22), (86, 145, 129), (184, 85, 89), (178, 191, 209), (107, 126, 152), (219, 176, 181)]

tim = Turtle()
i = 1
tim.speed('fastest')
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.pendown()

x = int(tim.pos()[0])

while i in range(11):
    for _ in range(11):
        tim.pendown()
        tim.dot(20, random.choice(rgb_list))
        tim.penup()
        tim.forward(50)
    tim.setx(x)
    tim.sety(int(tim.pos()[1]) + 50)
    i+=1


turtle.Screen()
turtle.onscreenclick()
