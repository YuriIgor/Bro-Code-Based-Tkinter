from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-5)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+5)

def move_left(event):
    label.place(x=label.winfo_x()-5, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+5, y=label.winfo_y())

window = Tk()
window.title("Moving")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)
race_car = PhotoImage(file="racecar.png")

window.geometry("500x500")

label = Label(window,
              image=race_car)
label.place(x=0, y=0)

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)



window.mainloop()