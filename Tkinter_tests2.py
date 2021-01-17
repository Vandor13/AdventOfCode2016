from tkinter import *
from tkinter import filedialog

window = Tk()

window.title("Welcome to my first GUI app")
window.geometry("700x400")


def create_new():
    print("Created new")


menu = Menu(window)
# menu.add_command(label="File")
new_item = Menu(menu, tearoff=0)
new_item.add_command(label="New", command=create_new)
new_item.add_command(label="Open")
new_item.add_separator()
new_item.add_command(label="Edit")
menu.add_cascade(label="File", menu=new_item)
menu.add_cascade(label="Project", menu=new_item)
window.config(menu=menu)


def clicked():
    # file = filedialog.askopenfilename()
    # file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    directory = filedialog.askdirectory()
    file = filedialog.askopenfilename(initialdir=directory + "/InputData")
    print(directory)
    # print(file)


button = Button(window, text="Choose file", command=clicked)
button.grid(column=1, row=0)

window.mainloop()



