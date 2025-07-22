from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_Timer():
    global timer
    global reps

    # Safe cancel only if it's not None
    if timer is not None:
        try:
            screen.after_cancel(timer)
        except Exception as e:
            print("Cancel Error:", e)

    # Reset timer and UI
    timer = None
    reps = 0
    canvas.itemconfig(text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_Timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_Down(long_break)
        label.config(text="Long Break", fg=RED)
        label.update()
    elif reps % 2 == 0:
        count_Down(short_break)
        label.config(text="Short Break", fg=PINK)
        label.update()
    else:
        count_Down(work_sec)
        label.config(text="Work Time", fg=GREEN)
        label.update()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_Down(count):

    count_minute = math.floor(count/60)
    count_second = count % 60

    # DYNAMIC TYPING
    if count_second == 0:
        count_second = "00"

    elif count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig (text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = screen.after(1000, count_Down, count-1)
    else:

        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
        tick.config(text=mark)
        tick.update()
        start_Timer()



# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title('Pomodoro')
screen.config(padx=100, pady=50 , bg=YELLOW, highlightthickness=0)



# used for making a canvas like in a picture
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102,114, image=tomato_img)
text = canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# label
label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 40, 'bold'))
label.config(bg=YELLOW)
label.grid(column= 1, row= 0)


tick = Label(fg=GREEN, bg = YELLOW, font=(FONT_NAME, 15), highlightthickness=0)
tick.grid(column= 1,row= 3)

# button
start = Button(text='Start', bg=YELLOW, font=(FONT_NAME, 10), highlightthickness=0, command=start_Timer)
start.grid(column=0,row=2)

reset = Button(text='reset', bg=YELLOW, font=(FONT_NAME, 10), command=reset_Timer)
reset.grid(column=2,row=2)


screen.mainloop()