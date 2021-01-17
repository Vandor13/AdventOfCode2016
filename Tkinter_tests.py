from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

window = Tk()

window.title("Welcome to my first GUI app")
window.geometry("700x400")

label = Label(window, text="Hello")  # , font=("Arial Bold", 50))
label.grid(column=1, row=0)

text_box = Entry(window, width=10)
text_box.grid(column=1, row=2)
text_box.focus()

combo = Combobox(window)
combo["values"] = ("The Thunderdome", "The Voice", "your doom!")
combo.current(1)
combo.grid(column=1, row=4)


def clicked():
    response = "Welcome to " + combo.get()
    # if check_state.get():
    #     response = response.upper()
    label.configure(text=response)
    text_box.config(state="disabled")


def check_clicked():
    response = label.cget("text")
    if check_state.get():
        response = response.upper()
    else:
        response = response.lower()
    label.configure(text=response)


check_state = IntVar()
check_button = Checkbutton(window, text="All Caps?", var=check_state, command=check_clicked)
check_button.grid(column=1, row=6)

button = Button(window, text="Click Me", command=clicked)
button.grid(column=1, row=8)

selected = IntVar()
radio_button_1 = Radiobutton(window, text="Info", value=1, var=selected)
radio_button_2 = Radiobutton(window, text="warning", value=2, var=selected)
radio_button_3 = Radiobutton(window, text="error", value=3, var=selected)
radio_button_4 = Radiobutton(window, text="ask question", value=4, var=selected)
radio_button_5 = Radiobutton(window, text="ask yes no", value=5, var=selected)
radio_button_6 = Radiobutton(window, text="ask yes no cancel", value=6, var=selected)
radio_button_7 = Radiobutton(window, text="ask ok cancel", value=7, var=selected)
radio_button_8 = Radiobutton(window, text="ask retry cancel", value=8, var=selected)

radio_button_1.grid(column=1, row=10)
radio_button_2.grid(column=1, row=11)
radio_button_3.grid(column=1, row=12)
radio_button_4.grid(column=1, row=13)
radio_button_5.grid(column=1, row=14)
radio_button_6.grid(column=1, row=15)
radio_button_7.grid(column=1, row=16)
radio_button_8.grid(column=1, row=17)




def clicked2():
    print(selected.get())
    # txt.delete(1.0, END)
    choice = selected.get()
    if choice == 1:
        messagebox.showinfo("Message title", "Message content")
    elif choice == 2:
        messagebox.showwarning("Message title", "Message content")
    elif choice == 3:
        messagebox.showerror("Message title", "Message content")
    elif choice == 4:
        res = messagebox.askquestion('Message title', 'Message content')
    elif choice == 5:
        res = messagebox.askyesno('Message title', 'Message content')
    elif choice == 6:
        res = messagebox.askyesnocancel('Message title', 'Message content')
    elif choice == 7:
        res = messagebox.askokcancel('Message title', 'Message content')
    elif choice == 8:
        res = messagebox.askretrycancel('Message title', 'Message content')


button = Button(window, text="Radio Things", command=clicked2)
button.grid(column=1, row=18)

# spin = Spinbox(window, from_=0, to=100, width=5)
var = IntVar()

var.set(8)
spin = Spinbox(window, values=(3, 8, 11), width=5, textvariable=var)

spin.grid(column=0,row=19)

window.mainloop()



