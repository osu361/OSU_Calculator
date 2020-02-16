# Python program to  create a simple GUI
# calculator using Tkinter
# References:
# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
# https://medium.com/@adeyinkaadegbenro/project-build-a-python-gui-calculator-fc92bddb744d

# import everything from tkinter module
from tkinter import *
import math
import tkinter.font as font  # added this


# A global constant of sorts. The number of columns in the calculator
NUM_COLUMNS = 4
BTN_BG_COLOR = "red"
BTN_TXT_COLOR = "black"
CALC_BG_COLOR = "light green"

# EXAMPLE: class helloworld


class HelloWorld:
    def __init__(self):
        self.message = "Hello World!"

    def printMessage(self, equation):
        equation.set(self.message)


class Mathematics:
    def basic(self, expression):
        return str(eval(expression))

    def log10(self, expression):
        try:
            floatValue = float(expression)
            result = math.log10(floatValue)
        except:
            result = "error"
        return str(result)


class Calculator:
    def __init__(self, master):
        self.master = master
        # set the background colour of GUI window
        self.master.configure(background=CALC_BG_COLOR)

        # screen font 30
        self.screenFont = font.Font(weight="bold", size=30)  # added this

        # button font 20
        self.buttonFont = font.Font(weight="bold", size=20)  # added this

        # use object instance to access math functions in the Mathematics class
        self.my_math = Mathematics()

        # EXAMPLE: Create a HelloWorld class object to call the HelloWorld class functions
        self.my_hello = HelloWorld()

        # set the title of GUI window
        self.master.title("Calculator")

        # set the configuration of GUI window
        # According to Geeks for Geeks the below geomtry declaration is not necessary and imposes predefined
        # size limits which would introduce the need for hard coding
        # https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
        # reference: https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
        # self.master.geometry("265x125")
        # self.master.geometry("400x300")

        self.numColumns = NUM_COLUMNS  # use this to change the number of columns

        # example for adding other functionality
        self.Flag = ""

        # will hold the expression entered by the user
        self.expression = ""

        # for more information on tkinter variables see:
        # https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/

        # StringVar() is the variable class
        # we create an instance of this class
        # this holds a variable in a class from ktinker
        self.equation = StringVar()

        # create the text entry box for
        # showing the expression .
        self.expression_field = Entry(
            self.master, textvariable=self.equation, font=self.screenFont)

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        self.expression_field.grid(columnspan=self.numColumns, ipadx=70)

        # variables to save most recent result and user selected answer to save
        self.saved_answer = None
        self.previous_answer = 0

        self.equation.set('')

        self.buttonList = [

            Button(self.master, text='save', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.saveAnswer(), width=7, height=1),
            Button(self.master, text='load', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.loadAnswer(), width=7, height=1),
            Button(self.master, text='clr save', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.clearAnswer(), width=7, height=1),
            Button(self.master, text=u"\u232B", fg=BTN_TXT_COLOR,
                   bg=BTN_BG_COLOR, command=self.clear, width=7, height=1),

            Button(self.master, text=' 7 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(7), width=7, height=1),
            Button(self.master, text=' 8 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(8), width=7, height=1),
            Button(self.master, text=' 9 ',  fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(9), width=7, height=1),
            Button(self.master, text=u"\u00F7", fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("/"), width=7, height=1),

            Button(self.master, text=' 4 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(4), width=7, height=1),
            Button(self.master, text=' 5 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(5), width=7, height=1),
            Button(self.master, text=' 6 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(6), width=7, height=1),
            Button(self.master, text=' * ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("*"), width=7, height=1),

            Button(self.master, text=' 1 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(1), width=7, height=1),
            Button(self.master, text=' 2 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(2), width=7, height=1),
            Button(self.master, text=' 3 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(3), width=7, height=1),
            Button(self.master, text=' - ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("-"), width=7, height=1),

            Button(self.master, text=' . ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("."), width=7, height=1),
            Button(self.master, text=' 0 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(0), width=7, height=1),
            Button(self.master, text='log', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.setFlag("log"), width=7, height=1),
            Button(self.master, text=' + ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("+"), width=7, height=1),

            # EXAMPLE:  add helloworld button
            Button(self.master, text='HW', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.my_hello.printMessage(self.equation),
                   width=7, height=1),

            Button(self.master, text=' = ', fg=BTN_TXT_COLOR,
                   bg=BTN_BG_COLOR, command=self.equalpress, width=28, height=1,
                   font=self.buttonFont),
        ]

        self.lengthOfbuttonList = len(self.buttonList)

        # row number starts from 1 since row 0 is for the display
        self.numRows = self.lengthOfbuttonList//self.numColumns + 1

        index = 0
        for row in range(1, self.numRows):
            Grid.rowconfigure(self.master, row, weight=1)  # sticky
            for column in range(self.numColumns):
                Grid.columnconfigure(self.master, column, weight=1)  # sticky
                self.buttonList[index].grid(
                    row=row, column=column, sticky=(N, S, E, W))  # sticky
                # print("row= ",row, " column= ", column)
                index += 1

        row += 1
        column = 0
        Grid.rowconfigure(self.master, row, weight=1)  # sticky

        for i in range(index, self.lengthOfbuttonList-1):
            self.buttonList[index].grid(
                row=row, column=column, sticky=(N, S, E, W))  # sticky
            # print("row= ",row, " column= ", column)
            index += 1
            column += 1

        # assign the "=" button to it own row at the bottom of the calculator
        row += 1
        Grid.rowconfigure(self.master, row, weight=1)  # sticky

        self.buttonList[index].grid(
            row=row, column=0, columnspan=self.numColumns, sticky=(N, S, E, W))

        # listen for enter key
        self.master.bind('<Return>', self.enterKey)

    def setFlag(self, flag):
        self.Flag = flag
        self.press(flag)

    # Function to update expressiom
    # in the text entry box
    def press(self, num):
        # point out the global expression variable
        # global expression

        # concatenation of string
        self.expression += str(num)

        # update the expression by using set method
        self.equation.set(self.expression)

    # Function to evaluate the final expression
    def equalpress(self):
        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.

        # Put that code inside the try block
        # which may generate the error
        try:

            # global expression

            # eval function evaluate the expression
            # and str function convert the result
            # into string

            if (self.Flag == "log"):  # example of implementing a function
                startIndex = len("log")
                total = self.my_math.log10(self.expression)
                self.expression = self.expression[startIndex:]
            else:
                # eval takes a string expression and evaluates it
                total = self.my_math.basic(self.expression_field.get())

            self.equation.set(total)

            self.previous_answer = eval(total)  # save result of operation to previous answer variable

            # initialze the expression variable
            # by empty string
            self.expression = ""
            self.Flag = ""

        # if error is generate then handle
        # by the except block
        except:
            self.displayError()

    # Function to clear the contents
    # of text entry box

    def clear(self):
        # global expression
        self.expression = ""
        self.Flag = ""
        self.equation.set("")

    # Function to save the previous answer for later use
    def saveAnswer(self):
        self.saved_answer = self.previous_answer

    # Function to load a previously saved answer, displays an error if no saved answer exists
    def loadAnswer(self):
        if self.saved_answer is None:
            self.displayError()
        else:
            self.expression = str(self.saved_answer)
            self.equation.set(self.expression)

    # function to erase the previously saved answer
    def clearAnswer(self):
        self.saved_answer = None

    # function to display error to the screen if the user tries to perform illegal operations
    def displayError(self):
        self.equation.set(" error ")
        self.expression = ""

    def enterKey(self, event):
        self.equalpress()


# Driver code
if __name__ == "__main__":
    # create a GUI window
    root = Tk()
    root.geometry("300x300")
    my_gui = Calculator(root)
    root.mainloop()
