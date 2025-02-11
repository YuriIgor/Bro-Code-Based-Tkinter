from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download < GB):
        time.sleep(0.05)
        bar["value"]+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed.")
        window.update_idletasks()

window = Tk()
window.title("Progress Bar")
logo = PhotoImage(file="capri.png")
window.iconphoto(True, logo)

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10, padx=10)

percent_label = Label(window, textvariable=percent).pack()
tasks_label = Label(window, textvariable=text).pack()


button = Button(window, text="Time", command=start).pack()



window.mainloop()