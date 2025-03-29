from tkinter import *

window = Tk()
window.title("Using Grid Manager")
window.geometry("400x200")


yscroll = Scrollbar(window)
yscroll.pack(side=RIGHT, fill=BOTH)

lstbox = Listbox(window)
lstbox.pack(fill=BOTH, expand=100)


yscroll.config(command=lstbox.yview)

for x in range(51):
    lstbox.insert(END, x)
lstbox.config(yscrollcommand=yscroll.set)
yscroll.config(command=lstbox.yview)
window.mainloop()