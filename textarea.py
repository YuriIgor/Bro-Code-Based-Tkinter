from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()
window.title("Textarea")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)
text = Text(window,
            padx=15,
            pady=15,
            bg="#67f5f0",
            fg="ivory",
            font=("Garamond", 35, "italic"),
            height=8,
            width=20)
text.pack()

button = Button(window,
                text="submit",
                command=submit)
button.pack()

window.mainloop()