from tkinter import *

def do_something(event):
    #print("Mouse coordinates: " + str(event.x) + "," + str(event.y)) <- THIS IS USEFUL AS FUCK
    print(f"Mouse coordinates: {str(event.x)}, {str(event.y)}.") #I like this syntax more.

window = Tk()
window.title("Mouse Events")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

#window.bind("<Button-1>", do_something) - Left mouse click.
#window.bind("<Button-2>", do_something) - Scroll wheel.
#window.bind("<Button-3>", do_something) - Right mouse click.
#window.bind("<ButtonRelease>", do_something)
#window.bind("<Enter>", do_something) - Displayed when entering the window.
#window.bind("<Leave>", do_something) - Displayed when leaving the window.
window.bind("<Motion>", do_something)




window.mainloop()