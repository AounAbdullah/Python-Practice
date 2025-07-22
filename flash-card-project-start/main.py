from tkinter import *
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"
# Importing csv file
df = pd.read_csv('data/french_words.csv')
to_learn = df.to_dict(orient='records')
timer = None
count = 3
card_word = {}

def words_wrong():
    global card_word
    try:
        with open('words_to_learn.csv', 'r') as file:
            df1 = pd.read_csv('words_to_learn.csv')
            new_words = df1.to_dict(orient='records')

    except:
        card_word = r.choice(to_learn)
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(card_background, image=front_image)
        canvas.itemconfig(card_Word, text=card_word['French'], fill='black')
        screen.after(3000, func=flipcard)


    else:
        card_word = r.choice(new_words)
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(card_background, image=front_image)
        canvas.itemconfig(card_Word, text=card_word['French'], fill='black')
        screen.after(3000, func=flipcard)

def words_right():
    global card_word
    try:
        with open('words_to_learn.csv', 'r') as file:
            df1 = pd.read_csv('words_to_learn.csv')
            new_words = df1.to_dict(orient='records')

    except:
        card_word = r.choice(to_learn)
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(card_background, image=front_image)
        canvas.itemconfig(card_Word, text=card_word['French'], fill='black')
        remaining_words = [word for word in to_learn if word != card_word]
        pd.DataFrame(remaining_words).to_csv("words_to_learn.csv", index=False)

        screen.after(3000, func=flipcard)


    else:
        card_word = r.choice(new_words)
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(card_background, image=front_image)
        canvas.itemconfig(card_Word, text=card_word['French'], fill='black')
        remaining_words = [word for word in new_words if word != card_word]
        pd.DataFrame(remaining_words).to_csv("words_to_learn.csv", index=False)
        screen.after(3000, func=flipcard)




def flipcard():
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_Word, text=card_word['English'], fill='white')


screen = Tk()
screen.config(bg=BACKGROUND_COLOR)

flip_timer = screen.after(3000,func=flipcard)

# Back canvas
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0, bd=0)
front_image = PhotoImage(file="flash-card-project-start/images/card_front.png")
back_image = PhotoImage(file="flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400,263,image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_Word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=(50, 0))  # Top padding only

# Buttons
Green = PhotoImage(file="flash-card-project-start/images/right.png")
Red = PhotoImage(file="flash-card-project-start/images/wrong.png")

right_button = Button(image=Green, highlightthickness=0, bd=0,command=words_right)
right_button.grid(column=1, row=1, pady=(20, 50))  # 20px spacing from canvas, 50px bottom

wrong_button = Button(image=Red, highlightthickness=0, bd=0, command=words_wrong)
wrong_button.grid(column=0, row=1, pady=(20, 50))

words_right()

screen.mainloop()