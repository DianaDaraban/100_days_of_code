import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')
# for i in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)

# for i in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

colors = ['grey','red', 'yellow', 'blue', 'green', 'black', 'purple', 'orange']
direction=[0,90,180,270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed('fastest')

# for i in range(3,11):
#     for _ in range(i):
#         timmy_the_turtle.color(colors[i-3])
#         timmy_the_turtle.right(360/i)
#         timmy_the_turtle.forward(100)


for _ in range(200):
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(direction))










screen = Screen()
screen.exitonclick()