from tkinter import *
from tkinter import messagebox

def click():
    if messagebox.askyesno(title="Question", message="To shine and to love?"):
        good_answer = Label(window,
                            text="Destroy Soul Edge!",
                            font=("Garamond", 40, "italic"),
                            bg="black",
                            activebackground="black",
                            fg="ivory",
                            activeforeground="ivory",
                            padx=10,
                            pady=10)
        good_answer.pack()
    else:
        bad_answer = Label(window,
                           text="Filthy Evil Scum!",
                           font=("Garamond", 40, "bold"),
                           bg="black",
                           activebackground="black",
                           fg="ivory",
                           activeforeground="ivory",
                           padx=10,
                           pady=10)
        bad_answer.pack()

    
   
    

window = Tk()
window.title("Message box practise")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

button = Button(window,
                text="Click me, pal",
                font=("arial", 25),
                command=click)
button.pack()



window.mainloop()