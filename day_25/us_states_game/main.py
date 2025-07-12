import turtle

import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image ='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
correct_answers = []
while len(correct_answers) <= 50:
    answer_state = screen.textinput(title=f'{len(correct_answers)}/50 States Correct', prompt='What`s another state`s name?').title()
    selected_state = data[data.state == answer_state]
    if answer_state == 'Exit':
        missing_states = []
        for state in data.state:
            if state not in correct_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if not selected_state.empty:
        # print(selected_state)
        text=turtle.Turtle()
        text.hideturtle()
        text.penup()
        x = selected_state.x.item()
        y = selected_state.y.item()
        text.goto(x, y)
        text.write(answer_state.capitalize(),font=('Arial', 10, 'normal'))
        correct_answers.append(answer_state)

    # print(selected_state)



