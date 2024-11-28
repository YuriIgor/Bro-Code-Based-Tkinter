from tkinter import *

def display():
    if(x.get()==1):
        print("I like it.")
    else:
        print("The dogs are barking.")

window = Tk()

x = IntVar()

logo = PhotoImage(file="capri.png")
fur = PhotoImage(file="fur.png")
window.iconphoto(True, logo)

check_button = Checkbutton(window,
                           padx=15,
                           pady=15,
                           text="Hold onto my fur.",
                           font=("Garamond", 30, "bold"),
                           bg="black",
                           activebackground="black",
                           fg="green",
                           activeforeground="green",
                           image=fur,
                           compound="left",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display
                           )
check_button.pack()






window.mainloop()