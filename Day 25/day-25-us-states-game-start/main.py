import turtle 
import pandas as pd

# preparing the screen
screen = turtle.Screen()
screen.title('U.S State Game')
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# creating turtle to write states name
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

# reading a csv file
names = pd.read_csv('day-25-us-states-game-start/50_states.csv')

# converting states column to list 
states = names['state'].to_list()


run = True
count = 0
guessed_states = []
while run:
    answer = screen.textinput(title=f'{count}/50 States Correct', prompt="What's anoter state's name?")
    answer_State = answer.title()

    if answer_State == 'Exit':
        break

    if answer_State in states:
        guessed_states.append(answer_State)
        store_cor = names[names['state'] == answer_State]
        x_cor = store_cor.iloc[0]['x']
        y_cor = store_cor.iloc[0]['y']
        tim.goto(x_cor, y_cor)
        tim.write(answer_State)
        count += 1
        

    if count == 50:
        run = False

# generating a csv file
learn_States = []
for state in states:
    if state not in guessed_states:
        learn_States.append(state)

dictionary = {'name': learn_States}
df = pd.DataFrame(dictionary)
df.to_csv('Learn_States.csv')