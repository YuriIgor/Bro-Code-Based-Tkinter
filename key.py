from tkinter import *

def do_thing(event):
    print("Thing done.")
    label.config(text=event.keysym, font=("Garamond", 120))

window = Tk()
window.title("Key")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

label = Label(window, font=("Helvetica", 50))
label.pack()

window.bind("<Key>", do_thing)




window.mainloop()