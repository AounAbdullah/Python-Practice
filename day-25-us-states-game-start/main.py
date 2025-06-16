import turtle 
import pandas as pd

screen = turtle.Screen()
# screen.title('U.S State Game')
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


names = pd.read_csv('day-25-us-states-game-start/50_states.csv')

states = names['state'].to_list()


run = True
count = 0
while run:
    answer = screen.textinput(title=f'{count}States Correct', prompt="What's anoter state's name?")
    answer_State = answer.title()

    
    if answer_State in states:
        store_cor = names[names['state'] == answer_State]
        x_cor = store_cor.iloc[0]['x']
        y_cor = store_cor.iloc[0]['y']
        tim.goto(x_cor, y_cor)
        tim.write(answer_State)
        count += 1
        

    if count == 50:
        run = False
        
tim.goto(0,0)
tim.color('red')
tim.write("Your Text", font=("Arial", 20, "normal"))
turtle.mainloop() 

