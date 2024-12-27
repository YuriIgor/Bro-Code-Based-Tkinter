from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\carol\\Desktop\\TkinterBro\\Tkfileopen",
                                           title="Escolha",
                                           filetypes = (("Textos", "*.txt"),
                                           ("Tudo", "*.*")))
    file = open(file_path, "r")
    print(file.read())
    file.close()

window = Tk()
window.title("Hey Ya")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

button = Button(window,
                text="Open",
                command=open_file)
button.pack()


window.mainloop()