from tkinter import *

transport = ["Boat", "Car", "Train"]

def choice():
    if (x.get() == 0):
        print("Boat party!")
    elif (x.get() == 1):
        print("Caraoke!")
    elif (x.get() == 2):
        print("Chug chug ho!")

window = Tk()
window.title("Treino Finale Radio")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)
boat_image = PhotoImage(file="boat.png")
car_image = PhotoImage(file="car.png")
train_image = PhotoImage(file="train.png")
transport_images = [boat_image, car_image, train_image]

x = IntVar()

for index in range(len(transport)):
    radiobutton = Radiobutton(window,
                              padx=25,
                              bg="ivory",
                              activebackground="ivory",
                              text=transport[index],
                              font=("Impact", 20, "bold"),
                              image = transport_images[index],
                              compound="left",
                              variable=x,
                              value=index,
                              width=300,
                              command=choice)
    radiobutton.pack(anchor=W)




window.mainloop()