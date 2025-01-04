from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(filetypes = [("Text files", ".txt"),
                                                 ("HTML files", ".html"),
                                                 ("CSS files", ".css")])
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()
    
window = Tk()
window.title("Save")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

button = Button(window,
                text="Save me",
                command=save_file)
button.pack()

text = Text(window)
text.pack()


window.mainloop()