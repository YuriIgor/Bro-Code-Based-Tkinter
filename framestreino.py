from tkinter import *

window = Tk()
window.title("Treino de Frames")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo) 

frame = Frame(window, bg="gold", bd=5, relief=RAISED)
frame.pack(side=BOTTOM)

Button(frame, text="Hey", font=("Garamand", 25, "bold"), width=5).pack(side=TOP)
Button(frame, text="Ho", font=("Garamand", 25, "bold"), width=5).pack(side=LEFT)
Button(frame, text="Let's", font=("Garamand", 25, "bold"), width=5).pack(side=LEFT)
Button(frame, text="Go", font=("Garamand", 25, "bold"), width=5).pack(side=LEFT)



window.mainloop()