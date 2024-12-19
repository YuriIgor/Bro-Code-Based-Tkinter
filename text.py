from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)
    

window = Tk()
window.title("Text")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

text = Text(window,
            bg="black",
            fg="ivory",
            font=("garamond", 20, "bold"),
            padx=15,
            pady=15)
text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()




window.mainloop()