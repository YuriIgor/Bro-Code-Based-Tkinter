from tkinter import *
from Ball import *
import time

WIDTH = 500
HEIGHT = 500

window = Tk()
window.title("Multiple Animations")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 3, 2, "red")
tennis_ball = Ball(canvas, 0, 0, 40, 4, 3, "yellow")
football_ball = Ball(canvas, 0, 0, 110, 2, 1, "black")
basketball_ball = Ball(canvas, 0, 0, 150, 1, 0.5, "orange")
golf_ball = Ball(canvas, 0, 0, 25, 3.5, 2.6, "gray")



while True:
    volley_ball.move()
    tennis_ball.move()
    football_ball.move()
    basketball_ball.move()
    golf_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()