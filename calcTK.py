from tkinter import *
import re
import tkinter.font as font


class Calculator:
    def __init__(self, master):

        self.master = master
        master.title("OSU Calculator")

        # fonts
        self.screenFont = font.Font(weight="bold", size=40)
        self.myFont = font.Font(weight="bold", size=20)

        # create screen widget
        self.screen = Text(master, state="disabled", width=20, height=2,
                           background="#FF7F50", foreground="black",
                           font=self.screenFont,)

        # position screen in window
        self.screen.grid(row=0, column=0, columnspan=5, padx=15, pady=15)

        # initialize screen value as empty
        self.equation = ""

        # create buttons using method createButton
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"clear", None)

        # Dropdown menu
        self.options = [
            "Save History",
            "Save to File",
            "Calculation Log"
        ]
        variable = StringVar(master)
        variable.set(self.options[0])  # default value
        b4a = OptionMenu(master, variable, *self.options)
        b4a.config(font=self.myFont)

        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton("/")
        b8a = self.createButton("ENTER")

        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton("*")
        b12a = None  # place holder for button

        b13 = self.createButton(".")
        b14 = self.createButton(0)
        b15 = self.createButton("+")
        b16 = self.createButton("-")
        b16a = None  # place holder for button

        b17 = self.createButton("=", None, 34)

        # buttons stored in list
        buttons = [b1, b2, b3, b4, b4a, b5, b6, b7, b8, b8a, b9,
                   b10, b11, b12, b12a, b13, b14, b15, b16, b16a, b17, ]

        # intialize counter
        count = 0
        # arrange buttons with grid manager
        for row in range(1, 5):
            for column in range(5):
                # button = Button(self.master, command=self.click, width)
                if buttons[count] is not None:
                    buttons[count].grid(row=row, column=column)
                count += 1
        # arrange last button '=' at the bottom
        buttons[20].grid(row=5, column=0, columnspan=5)

    def createButton(self, val, write=True, width=8):
        # this function creates a button, and takes one compulsory argument, the value that should be on the button

        return Button(self.master, text=val, command=lambda:
                      self.click(val, write), width=width, font=self.myFont,
                      height=2, padx=1, pady=1,)

    def click(self, text, write):
        # this function handles what happens when you click a button
        # 'write' argument if True means the value 'val' should be written on screen, if None, should not be written on screen
        if write == None:

            # only evaluate code when there is an equation to be evaluated
            if text == "=" and self.equation:
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == u"clear":
                self.clear_screen()

        else:
            # add text to screen
            self.insert_screen(text)

    def clear_screen(self):
        # to clear screen
        # set equation to empty before deleting screen
        self.equation = ""
        self.screen.configure(state="normal")
        self.screen.delete("1.0", END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state="normal")
        self.screen.insert(END, value)
        # record every value inserted in screen
        self.equation += str(value)
        self.screen.configure(state="disabled")


root = Tk()
root.geometry("624x400")
root.resizable(0, 0)
Calculator(root)
root.mainloop()
