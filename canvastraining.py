from tkinter import *

window = Tk()
window.title("Canvas Training")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

canvas = Canvas(window, height=800, width=900, bg="black")

canvas.create_line(100, 300, 300, 300, fill="green", width=2)
canvas.create_line(100, 300, 100, 100, fill="green", width=2)
canvas.create_line(100, 100, 300, 100, fill="green", width=2)
canvas.create_line(300, 100, 300, 300, fill="green", width=2)
canvas.create_line(150, 200, 150, 400, fill="green", width=2)
canvas.create_line(150, 400, 350, 400, fill="green", width=2)
canvas.create_line(350, 400, 350, 200, fill="green", width=2)
canvas.create_line(350, 200, 150, 200, fill="green", width=2)
canvas.create_line(100, 100, 150, 200, fill="green", width=2)
canvas.create_line(300, 100, 350, 200, fill="green", width=2)
canvas.create_line(100, 300, 150, 400, fill="green", width=2)
canvas.create_line(300, 300, 350, 400, fill="green", width=2)




canvas.pack()



window.mainloop()