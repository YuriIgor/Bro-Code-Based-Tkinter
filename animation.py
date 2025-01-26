from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
XVELOCITY = 4
YVELOCITY = 3

window = Tk()
window.title("Animation")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

stars = PhotoImage(file="stars.png")
back_image = canvas.create_image(0, 0, image=stars, anchor=NW)
small_logo = PhotoImage(file="capri_small.png")
the_image = canvas.create_image(0, 0, image=small_logo, anchor=NW)

image_width = small_logo.width()
image_height = small_logo.height()

while True:
    coordinates = canvas.coords(the_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        XVELOCITY = XVELOCITY * -1
    elif(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        YVELOCITY = YVELOCITY * -1
    canvas.move(the_image, XVELOCITY, YVELOCITY)
    window.update()
    time.sleep(0.01)


window.mainloop()