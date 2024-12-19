from tkinter import *
from tkinter import colorchooser

def click():
    #window.config(bg=colorchooser.askcolor()[1])
    color = colorchooser.askcolor()
    print(color)
    hex_color = color[1]
    window.config(bg=hex_color)
    window.mainloop()
    
window = Tk()
window.title("Colours")
window.geometry("420x420")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

button = Button(window,
                text="Hey",
                command=click)
button.pack()



window.mainloop()