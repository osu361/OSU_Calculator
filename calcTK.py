from tkinter import *
import tkinter.font as font
import re


class Calculator:
    def __init__(self, master):

        self.master = master
        master.title("OSU Calculator")

        # screen font
        self.screenFont = font.Font(weight="bold", size=40)

        # button font
        self.myFont = font.Font(weight="bold", size=20)

        # button font
        self.eqFont = font.Font(weight="bold", size=13)

        # create screen widget
        self.screen = Text(master, state="disabled", width=20, height=1,
                           background="#FF7F50", foreground="black",
                           font=self.screenFont,)

        # position screen in window
        self.screen.grid(row=0, column=0, columnspan=6, padx=10, pady=20)

        # initialize screen value as empty
        self.equation = ""

        # first row buttons
        b1 = self.createButton(u"clear", None)
        b2 = self.createButton('%')
        b3 = self.createButton(u"\u232B", None)  # not working yet
        b4 = self.createButton("/")

        # Dropdown menu first row
        self.options = ["Save History", "Save to File",
                        "Calculation Log", "Hamming Code"]
        variable = StringVar(master)
        variable.set(self.options[0])  # default value
        b5 = OptionMenu(master, variable, *self.options)
        b5.config(font=self.myFont)

        # 2nd row buttons
        b6 = self.createButton(7)
        b7 = self.createButton(8)
        b8 = self.createButton(9)
        b9 = self.createButton("*")
        b10 = self.createButton("RUN", None)

        # 3rd row buttons
        b11 = self.createButton(4)
        b12 = self.createButton(5)
        b13 = self.createButton(6)
        b14 = self.createButton("-")
        b15 = None  # place holder for button

        # 4th row buttons
        b16 = self.createButton(1)
        b17 = self.createButton(2)
        b18 = self.createButton(3)
        b19 = self.createButton("+")
        b20 = None  # place holder for button

        # 5th row buttonw
        b21 = self.createButton(".")
        b22 = self.createButton(0)
        b23 = self.createButton("<", None)
        b24 = self.createButton("=", None)
        b25 = None  # place holder for button

        # keyboard input ->still needs get function
        Label(self.master, text="Keyboard Input:",
              font=self.eqFont).grid(row=7)
        self.b26 = Entry(self.master, width=34, textvariable=self.equation)

        b27 = Button(self.master, text="CALC", command=lambda:
                     self.click("CALC", None), font=self.myFont,
                     height=2, padx=5, pady=1,)

        # store buttons in list
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12,
                   b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25]

        # arrange buttons with grid manager
        count = 0
        for row in range(1, 6):
            for column in range(5):
                if buttons[count] is not None:
                    buttons[count].grid(row=row, column=column)
                count += 1

        self.b26.grid(row=7, column=0, columnspan=5,
                      padx=1, pady=3)
        b27.grid(row=7, column=4)

    def createButton(self, val, write=True, width=8):
        # this function creates a button
        return Button(self.master, text=val, command=lambda:
                      self.click(val, write), width=width, font=self.myFont,
                      height=2, padx=5, pady=1,)

    def click(self, text, write):
        # this function handles what happens when you click a button
        # 'write' argument if True means the value 'val' should be written on
        # screen, if None, should not be written on screen

        if write == None:
            kbInput = self.b26.get()
            # only evaluate code when there is an equation to be evaluated
            if text == "=" and self.equation:
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)

            elif text == "CALC":
                print(kbInput)
                answer = str(eval(kbInput))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == u'\u232b':  # this needs to backspace not clear
                self.clear_screen()
            elif text == "clear":
                self.clear_screen()

        else:
            # add text to screen
            self.insert_screen(text)

    def clear_screen(self):
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
root.geometry("660x400")
root.resizable(0, 0)
Calculator(root)
root.mainloop()
