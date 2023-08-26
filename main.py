from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = '✔'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer() -> None:
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='0:00')
    timer_label.config(text='Timer', fg=GREEN)
    global reps
    reps = 0
    checkmarks.config(text='')
    start_button.config(state='normal')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer() -> None:
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps < 9:
        start_button.config(state='disabled')
        if reps % 2 == 1:
            count_down(work_secs)
            timer_label.config(text='Work', font=(FONT_NAME, 35, 'bold'), fg=GREEN)
        elif reps == 8:
            count_down(long_break)
            timer_label.config(text='Break', font=(FONT_NAME, 35, 'bold'), fg=RED)
        else:
            count_down(short_break)
            timer_label.config(text='Break', font=(FONT_NAME, 35, 'bold'), fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count: int) -> None:
    mins: int = count // 60
    secs: int = count % 60

    canvas.itemconfig(timer_text, text=f'{mins}:{secs:02}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        marks = ''
        for _ in range(reps // 2):
            marks += CHECKMARK
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.minsize(width=400, height=450)
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 10, 'bold'), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 10, 'bold'), command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
checkmarks.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 28, 'bold'), fill='white')
canvas.grid(row=1, column=1)


window.mainloop()
