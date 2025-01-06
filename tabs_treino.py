from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Treino Tabs")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

notebook = ttk.Notebook()

tab_1 = Frame(notebook)
tab_2 = Frame(notebook)
tab_3 = Frame(notebook)

notebook.add(tab_1, text="Zelda")
notebook.add(tab_2, text="Mario")
notebook.add(tab_3, text="Metroid")
notebook.pack(expand=TRUE, fill="both")

Label(tab_1, text="Zelda isn't the protagonist.", width=60, height=30).pack()
Label(tab_2, text="It's him, Mario!", width=60, height=30).pack()
Label(tab_3, text="Samus is way too hot to be hidden under that armor.", width=60, height=30).pack()


window.mainloop()