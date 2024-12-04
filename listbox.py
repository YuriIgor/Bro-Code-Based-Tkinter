from tkinter import *

def submit():
 
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add_item():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()
window.title("Listbox")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Garamond", 30, "bold"),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Lasagna")
listbox.insert(4, "Bread")
listbox.insert(5, "Wine")

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack()

add_button = Button(window,
                       text="Add",
                       command=add_item)
add_button.pack()

delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack()




window.mainloop()