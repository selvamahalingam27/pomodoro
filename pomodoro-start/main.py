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
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(timer_new_label, text="00:00")
    timer_label.config(text="TIMER")
    checkmark_label.config(text="")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_to_sec = WORK_MIN * 60
    short_break_to_sec = SHORT_BREAK_MIN * 60
    long_to_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        create_countdown(long_to_sec)
        timer_label.config(text="TAKE A LONG BREAK !!", fg="purple")
    elif REPS % 2 == 0:
        create_countdown(short_break_to_sec)
        timer_label.config(text="BREAK !!", fg="green")
    else:
        create_countdown(work_to_sec)
        timer_label.config(text="WORK !!", fg="red")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def create_countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_new_label , text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, create_countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(REPS / 2)
        for _ in range(work_session):
            mark += "✔️"
            checkmark_label.config(text = mark)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

timer_label = Label(text="WORK", font=(FONT_NAME,35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, background= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png",)
canvas.create_image(100, 112, image=tomato_img)
timer_new_label = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


start_button = Button(text="START", font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg="purple", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="RESET", font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg="purple", highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=3)



checkmark_label = Label(fg="green", bg=YELLOW)
checkmark_label.grid(row=4, column=2)



window.mainloop()

