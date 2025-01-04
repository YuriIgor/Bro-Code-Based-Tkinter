from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(filetypes = [
                                        ("Text files", ".txt"),
                                        ("HTML", ".html"),
                                        ("CSS", ".css")
                                    ])
    if file is None:
        return 
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()

window = Tk()
window.title("Shadows on the horizon")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)
button = Button(window,
                text="Hu, Ha",
                command=save_file)
button.pack()
text = Text(window,
            bg="black",
            fg="ivory")
text.pack()

window.mainloop()