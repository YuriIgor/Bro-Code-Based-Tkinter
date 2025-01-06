from tkinter import *

def open_file():
    print("The file has been opened.")

def save_file():
    print("The file has been saved.")

def cut_thing():
    print("The file has been sliced.")

def copy_thing():
    print("Copied.")

def paste_thing():
    print("Pasted.")

window = Tk()
window.title("Menubar")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

open_image = PhotoImage(file="opened.png")
save_image = PhotoImage(file="saved.png")
exit_image = PhotoImage(file="exited.png")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font=("Garamond", 20))
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, image=open_image, compound="left")
file_menu.add_command(label="Save", command=save_file, image=save_image, compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, image=exit_image, compound="left")

edit_menu = Menu(menu_bar, tearoff=0, font=("Garamond", 20))
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_thing)
edit_menu.add_command(label="Copy", command=copy_thing)
edit_menu.add_command(label="Paste", command=paste_thing)




window.mainloop()