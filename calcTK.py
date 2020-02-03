from tkinter import *
import tkinter.font as font
import re


class Calculator:
    def __init__(self, master):

        self.master = master
        master.title("OSU Calculator")

        # screen font
        self.screenFont = font.Font(weight="bold", size=40)

        # button font 20
        self.myFont = font.Font(weight="bold", size=20)

        # button font 13
        self.eqFont = font.Font(weight="bold", size=13)

        # create screen widget
        self.screen = Text(master, state="disabled", width=19, height=1,
                           background="#D73F09", foreground="black",
                           font=self.screenFont, pady=10)

        # position screen in window
        # make grid spaces dynamic in size
        for i in range(8):
            Grid.rowconfigure(root, i, weight=1)

        for i in range(4):
            Grid.columnconfigure(root, i, weight=1)

        self.screen.grid(row=0, column=0, columnspan=4,
                         padx=1, pady=20, sticky=N+S+E+W)

        # initialize screen value as empty
        self.equation = ""

        # ------------------------main buttons (20)------------------------------

        # 1st row buttons
        b1 = self.createButton(u"CLEAR", None).grid(
            row=1, column=0, sticky=(N, S, E, W))
        b2 = self.createButton('%').grid(row=1, column=1, sticky=(N, S, E, W))
        b3 = self.createButton(u"\u232B", None).grid(
            row=1, column=2, sticky=(N, S, E, W))
        b4 = self.createButton("/").grid(row=1, column=3, sticky=(N, S, E, W))

        # 2nd row buttons
        b5 = self.createButton(7).grid(row=2, column=0, sticky=(N, S, E, W))
        b6 = self.createButton(8).grid(row=2, column=1, sticky=(N, S, E, W))
        b7 = self.createButton(9).grid(row=2, column=2, sticky=(N, S, E, W))
        b8 = self.createButton("*").grid(row=2, column=3, sticky=(N, S, E, W))

        # 3rd row buttons
        b9 = self.createButton(4).grid(row=3, column=0, sticky=(N, S, E, W))
        b10 = self.createButton(5).grid(row=3, column=1, sticky=(N, S, E, W))
        b11 = self.createButton(6).grid(row=3, column=2, sticky=(N, S, E, W))
        b12 = self.createButton("-").grid(row=3, column=3, sticky=(N, S, E, W))

        # 4th row buttons
        b13 = self.createButton(1).grid(row=4, column=0, sticky=(N, S, E, W))
        b14 = self.createButton(2).grid(row=4, column=1, sticky=(N, S, E, W))
        b15 = self.createButton(3).grid(row=4, column=2, sticky=(N, S, E, W))
        b16 = self.createButton("+").grid(row=4, column=3, sticky=(N, S, E, W))

        # 5th row buttons
        b17 = self.createButton(".").grid(row=5, column=0, sticky=(N, S, E, W))
        b18 = self.createButton(0).grid(row=5, column=1, sticky=(N, S, E, W))
        b19 = self.createButton("<", None).grid(
            row=5, column=2, sticky=(N, S, E, W))
        b20 = self.createButton("=", None).grid(
            row=5, column=3, sticky=(N, S, E, W))

        # -----------------dropdown menu and keyboard input----------------------
        # 6th row dropdown menu
        Label(self.master, text="Function:", font=self.eqFont).grid(
            row=7)
        self.options = ["BasicCalc", "SaveHist", "Save2File",
                        "CalcLog", "Hamming"]
        variable = StringVar(master)
        variable.set(self.options[0])  # default value
        b26 = OptionMenu(master, variable, *self.options)
        b26.config(font=self.eqFont)
        b26.grid(row=7, column=1, sticky=(N, S, E, W))

        # 7th row keyboard input

        # create keyboard input box and place on grid
        self.b27 = Entry(self.master, width=26,
                         textvariable=self.equation, font=self.myFont)
        self.b27.grid(row=8, column=0, columnspan=5,
                      padx=1, pady=3, sticky=(N, S, E, W))

        # create ENTER button and place on grid
        b28 = Button(self.master, text="ENTER", command=lambda:
                     self.click("ENTER", None), font=self.myFont,
                     height=2, padx=5, pady=1,)
        b28.grid(row=8, column=3, sticky=(N, S, E, W))

    # ----------------------------functions ------------------------------------

    # this functions creates a button for them main grid buttons
    def createButton(self, val, write=True, width=10):

        # click reads string assigned to button and uses eval to solve equation
        return Button(self.master, text=val, command=lambda:
                      self.click(val, write), width=width, font=self.myFont,
                      height=2, padx=5, pady=1,)

    # this function handles what happens when you click a button
    def click(self, text, write):
        if write == None:

            # only evaluate code when there is an equation to be evaluated
            if text == "=" and self.equation:
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)

            # calculates input from keyboard input box
            elif text == "ENTER":
                print(self.b27.get())
                answer = str(eval(self.b27.get()))  # get and eval kbinput
                self.clear_screen()
                self.insert_screen(answer, newline=True)

            # backspace
            elif text == u'\u232b':  # this needs to backspace not clear
                self.clear_screen()

            # clear screen
            elif text == "CLEAR":
                self.clear_screen()

        else:
            # add text to screen
            self.insert_screen(text)

    def clear_screen(self):
        self.equation = ""
        self.screen.configure(state="normal")
        self.screen.delete("1.0", END)

    # record and display on screen
    def insert_screen(self, value, newline=False):
        self.screen.configure(state="normal")
        self.screen.insert(END, value)
        self.equation += str(value)
        self.screen.configure(state="disabled")


# --------------------------------main-------------------------------------------
root = Tk()
root.geometry("320x455")  # set window size
Calculator(root)
root.mainloop()
