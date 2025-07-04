import random
import turtle
from turtle import Turtle, Screen
is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = turtle.textinput('Make your bet', 'Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'green', 'blue', 'magenta', 'yellow']
all_turtles = []
for i in range(6):
    locals()['tim' + str(i)] = Turtle('turtle')
    locals()['tim' + str(i)].color(colors[i-1])
    locals()['tim' + str(i)].penup()
    locals()['tim' + str(i)].goto(-240, 150-i*50)
    all_turtles.append(locals()['tim' + str(i)])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You`ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'You`ve lost! The {winning_color} turtle is the winner!')
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


print(user_bet)
screen.exitonclick()