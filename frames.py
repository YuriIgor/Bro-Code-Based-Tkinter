from tkinter import *

window = Tk()
window.title("Frame")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

frame = Frame(window, bg="blue", bd=5, relief=RAISED)
frame.pack(side=BOTTOM)
#frame.place(x=100, y=100)

Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)




window.mainloop()