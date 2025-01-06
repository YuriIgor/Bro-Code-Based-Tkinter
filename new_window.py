from tkinter import *

def create_window():
    #new_window = Toplevel()
    new_window = Tk()
    old_window.destroy()
    #Button(new_window, text="Create yet another Window", command=create_window).pack()

old_window = Tk()
old_window.title("New Windows")
logo = PhotoImage(file="capri.png")
old_window.iconphoto(True, logo) 

Button(old_window, text="Create new Window", command=create_window).pack()




old_window.mainloop()