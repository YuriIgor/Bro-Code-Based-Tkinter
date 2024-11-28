from tkinter import *

def submit():
    username = entry.get()
    print(f"Hi, {username}!")
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

window = Tk()
window.title("Entry")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

entry = Entry(window,
              font=("Garamond", 30, "italic"),
              fg="#00ff00",
              bg="black")
entry.insert(0, "Enter the Matrix.")
entry.pack(side=LEFT)
#You can also show only * or other characters. (show="*")

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)





window.mainloop()