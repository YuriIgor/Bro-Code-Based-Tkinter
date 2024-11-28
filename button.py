from tkinter import *

count = 0 

def click():
    global count
    count += 1
    print(f"{count} Magic Happened!")

window = Tk()
window.title("Le button")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)
photo = PhotoImage(file="clickme.png")

button = Button(window,
                command=click,
                fg="#42f5e0",
                activeforeground="#42f5e0",
                bg="black",
                activebackground="black",
                text="Magic Happens!",
                font=("Arial", 40, "bold"),
                relief=RAISED,
                state=ACTIVE,
                image=photo,
                compound="top")
button.pack()


window.mainloop()