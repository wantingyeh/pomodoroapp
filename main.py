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
reps = 0     # repetition (round)
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

## reset the clock to 00:00
## rest the checks
## reset the title and back to timer
## reset reps
def reset_timer():
    window.after_cancel(timer)  # reset the timer
    #timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title label: Timer
    timer_label.config(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
    # reset check
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1  # every round, rep + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:  # the 8th reps
        count_down(long_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 50), fg=RED, bg=YELLOW)
    elif reps % 2 == 0: # every 2nd/4th/6th
        count_down(short_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 50), fg =PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minute = math.floor(count / 60) # only put the largest hold number
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{str(count_second)}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:  #stop after 0
        global timer
        timer = window.after(1000, count_down, count-1)  #1000 --> ms, function name, variables
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2) # every 2 reps, should get a tick (as it completes a work round)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) #change the size of the window and the bg colour



# label: Timer
## fg= font colour, bg=background colour
timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# create a canvas with Canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #change the colour of the canvas bg, and the border
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)  # (x, y, image); x and y is the half of the original size
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# create button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# label: keep track

check_label = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()






