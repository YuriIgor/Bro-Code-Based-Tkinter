from tkinter import *

def move_up(event):
    canvas.move(my_image, 0, -10)

def move_down(event):
    canvas.move(my_image, 0, 10)

def move_left(event):
    canvas.move(my_image, -10, 0)

def move_right(event):
    canvas.move(my_image, 10, 0)

window = Tk()
window.title("Move on Canvas")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)
race_car = PhotoImage(file="racecar.png")

canvas = Canvas(window, width=500, height=500)
canvas.pack()
my_image = canvas.create_image(0, 0, image=race_car, anchor=NW)

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)




window.mainloop()
