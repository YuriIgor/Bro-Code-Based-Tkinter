from tkinter import *

def submit():
    print(f"The level is {scale.get()}!")
    print(type(scale.get()))
    if (scale.get() > 50):
        print("You are on the happy side of life.")
    elif (scale.get() < 50):
        print("You are on the sad side of life.")

window = Tk()
window.title("Scale")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)
happy = PhotoImage(file="happy.png")
happy_label = Label(image=happy)
happy_label.pack(side=TOP)

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              tickinterval=10,
              showvalue=0,
              orient=VERTICAL,
              font=("Garamond", 20, "italic"),
              troughcolor="yellow",
              fg="orange",
              bg="black")
scale.set(50)
#scale.set(((scale["from"]-scale["to"])/2)+scale["to"])
scale.pack()

sad = PhotoImage(file="sad.png")
sad_label = Label(image=sad)
sad_label.pack()

button = Button(window,
                text="submit",
                command=submit)
button.pack(side=BOTTOM)



window.mainloop()