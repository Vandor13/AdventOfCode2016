from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import scrolledtext

EXAMPLE_DATA = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""


class SignalNoise:
    def __init__(self):
        self.window = Tk()
        self.label = Label(self.window, text="")
        self.messages = list(EXAMPLE_DATA.split("\n"))
        self.part = IntVar()
        self.part.set(1)
        self.decoded_message = ""
        self.prepare_gui()
        self.no_chars = 0

    def calculate_message(self):
        self.no_chars = len(self.messages[0].strip("\n"))
        letter_amounts = []
        for _ in range(self.no_chars):
            letter_amounts.append(dict())
        for message in self.messages:
            for i in range(self.no_chars):
                letter = message[i]
                if letter in letter_amounts[i].keys():
                    letter_amounts[i][letter] = letter_amounts[i][letter] + 1
                else:
                    letter_amounts[i][letter] = 1
        self.decoded_message = ""
        for i in range(self.no_chars):
            if self.part.get() == 1:
                most_letter = max(letter_amounts[i].keys(),
                                  key=lambda letter_element: letter_amounts[i][letter_element])
                self.decoded_message = self.decoded_message + most_letter
            else:
                least_letter = min(letter_amounts[i].keys(),
                                   key=lambda letter_element: letter_amounts[i][letter_element])
                self.decoded_message = self.decoded_message + least_letter
        result_text = "Here is the Code: " + self.decoded_message
        self.label.configure(text=result_text)

    def prepare_gui(self):
        self.window.title("Day 6: Signals and Noise")
        self.window.geometry("700x400")

        txt = scrolledtext.ScrolledText(self.window, width=40, height=10)
        txt.insert(INSERT, EXAMPLE_DATA)

        txt.grid(column=0, row=0)

        button = Button(self.window, text="Calculate Message", command=self.calculate_message)
        button.grid(column=0, row=4)

        self.label.grid(column=0, row=5)

        radio_button_1 = Radiobutton(self.window, text="Part 1", value=1, var=self.part)
        radio_button_2 = Radiobutton(self.window, text="Part 2", value=2, var=self.part)
        radio_button_1.grid(column=0, row=2)
        radio_button_2.grid(column=0, row=3)

        def load_file():
            filename = filedialog.askopenfilename()
            with open(filename, "r") as file:
                self.messages = file.readlines()
            txt.delete("1.0", END)
            for message in self.messages:
                txt.insert(INSERT, message)

        part_label = Label(self.window, text="Select part:")
        part_label.grid(column=0, row=1)



        menu = Menu(self.window)
        # menu.add_command(label="File")
        new_item = Menu(menu, tearoff=0)
        new_item.add_command(label="Open", command=load_file)
        menu.add_cascade(label="File", menu=new_item)
        self.window.config(menu=menu)

        self.window.mainloop()


signal_noise = SignalNoise()
