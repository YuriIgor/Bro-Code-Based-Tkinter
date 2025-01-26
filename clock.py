from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()
window.title("Relógio")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

time_label = Label(window, font=("garamond", 50), fg="#0000ff", bg="#000000")
time_label.pack()

day_label = Label(window, font=("garamond", 30), fg="#0000ff", bg="#000000", width=15)
day_label.pack()

date_label = Label(window, font=("garamond", 30), fg="#0000ff", bg="#000000", width=15)
date_label.pack()

update()

window.mainloop()