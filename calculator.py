# Python program to  create a simple GUI
# calculator using Tkinter
# References:
# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
# https://medium.com/@adeyinkaadegbenro/project-build-a-python-gui-calculator-fc92bddb744d

# import everything from tkinter module
from tkinter import *

import tkinter.font as font  # added this
from math import *

# A global constant of sorts. The number of columns in the calculator
NUM_COLUMNS = 4
BTN_BG_COLOR = "black"
BTN_TXT_COLOR = "light gray"
CALC_BG_COLOR = "black"
OPERATOR_LIST = {"urnary": ["log"], "binary": ["+", "-", "*", "/"]}


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
            result = log10(floatValue)
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
        self.display_text = ""

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

        # variables to save user entered operands/operator
        self.operands = [None, None]
        self.operator = None
        # Flag used to prohibit user from using two decimals in one number
        self.is_decimal = [False, False]

        self.clear_stack = False

        # Variables used to save answer
        self.saved_answer = None
        self.previous_answer = None

        self.equation.set('0')

        self.buttonList = [

            Button(self.master, text='save', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.saveAnswer(), width=7, height=1),
            Button(self.master, text='load', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.loadAnswer(), width=7, height=1),
            Button(self.master, text='clr save', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.clearAnswer(), width=7, height=1),
            Button(self.master, text=u"\u232B", fg=BTN_TXT_COLOR,
                   bg=BTN_BG_COLOR, command=self.clear, width=7, height=1),

            Button(self.master, text=' ( ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('('), width=7, height=1),
            Button(self.master, text=' ) ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(')'), width=7, height=1),
            Button(self.master, text=' UNDO ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.setFlag('UNDO'), width=7, height=1),
            Button(self.master, text=' REDO ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.setFlag('REDO'), width=7, height=1),

            Button(self.master, text=' 7 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('7'), width=7, height=1),
            Button(self.master, text=' 8 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('8'), width=7, height=1),
            Button(self.master, text=' 9 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('9'), width=7, height=1),
            Button(self.master, text=u"\u00F7", fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("/"), width=7, height=1),

            Button(self.master, text=' 4 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('4'), width=7, height=1),
            Button(self.master, text=' 5 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('5'), width=7, height=1),
            Button(self.master, text=' 6 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('6'), width=7, height=1),
            Button(self.master, text=' * ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("*"), width=7, height=1),

            Button(self.master, text=' 1 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('1'), width=7, height=1),
            Button(self.master, text=' 2 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('2'), width=7, height=1),
            Button(self.master, text=' 3 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('3'), width=7, height=1),
            Button(self.master, text=' - ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("-"), width=7, height=1),

            Button(self.master, text=' . ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("."), width=7, height=1),
            Button(self.master, text=' 0 ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('0'), width=7, height=1),
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
        self.numRows = self.lengthOfbuttonList // self.numColumns + 1

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

        for i in range(index, self.lengthOfbuttonList - 1):
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

    # Function to update expression
    # in the text entry box
    def press(self, num: str):
        # point out the global expression variable
        # global expression

        # Refactoring for building operands
        is_operand_data = num.isnumeric() or num == "negative"
        is_operand_data = is_operand_data or num == "."

        if is_operand_data:
            if self.operator is None:
                self.set_operand(0, num)
            else:
                self.set_operand(1, num)

        elif num in OPERATOR_LIST["urnary"]:
            self.eval_existing_expression("urnary", num)

        elif num in OPERATOR_LIST["binary"]:
            self.eval_existing_expression("binary", num)

        else:
            self.displayError()

        self.build_display_text()

        """
        # concatenation of string
        self.expression += str(num)

        # update the expression by using set method
        self.equation.set(self.expression)
        """

    def build_display_text(self):
        if self.operands[0] is not None:
            self.display_text = self.operands[0]
            if self.operator is not None:
                self.display_text += self.operator
                if self.operands[1] is not None:
                    self.display_text += self.operands[1]
            self.equation.set(self.display_text)
        elif self.previous_answer is not None:
            self.display_text = self.previous_answer
            self.equation.set(self.display_text)
        else:
            self.displayError()

    def eval_existing_expression(self, operator_type, operator):
        if self.operands[1] is not None:
            # TODO load OP[0] operator and OP[1] flag for second add
            self.equalpress(operator_type != "binary")
            self.operands[0] = self.previous_answer

        if self.operands[0] is None and self.previous_answer is not None:
            self.operands[0] = self.previous_answer

        if self.operands[0] is not None:
            # TODO load operator
            if operator_type == "urnary":
                # TODO and if not flag load OP[0]
                self.equalpress()
            else:
                self.set_operator(operator)
        else:
            self.displayError()

    def set_operand(self, idx, num):

        if num != "." or not self.is_decimal[idx]:
            if self.operands[idx] is None:
                # TODO Load/update current val of operand
                self.operands[idx] = num
            else:
                if num == "negative":
                    if self.operands[idx][0] == '-':
                        self.operands[idx] = self.operands[idx][1:]
                    else:
                        self.operands[idx] = "-" + self.operands[idx]
                else:
                    self.operands[idx] += num
        else:
            self.displayError("invalid key")

    def set_operator(self, operator):
        self.operator = operator

    # Function to evaluate the final expression
    def equalpress(self, ignore_flag=False):
        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.

        # Put that code inside the try block
        # which may generate the error
        #self.expression_field = self.fixZeros(self.expression_field.get())

        # removes leading zeros
        expFiltered = self.fixZeros(self.expression_field.get())
        try:

            # global expression

            # eval function evaluate the expression
            # and str function convert the result
            # into string

            if self.Flag == "log" and not ignore_flag:  # example of implementing a function
                #total = self.my_math.log10(self.expression_field.get())
                total = self.my_math.log10(expFiltered)
                self.Flag = ""
            else:
                # eval takes a string expression and evaluates it
                #total = self.my_math.basic(self.expression_field.get())
                total = self.my_math.basic(expFiltered)

            self.equation.set(total)

            self.previous_answer = total  # save result of operation to previous answer variable
            self.operands[0] = self.previous_answer

            # initialze the expression variable
            # by empty string
            # self.expression = total
            self.operands[0] = None
            self.operator = None
            self.operands[1] = None

        # if error is generate then handle
        # by the except block
        except:
            self.displayError()

    # Function to clear the contents
    # of text entry box

    def clear(self):
        # global expression
        self.operands[0] = None
        self.operands[1] = None
        self.operator = None
        self.clear_stack = not self.clear_stack  # logic for stack size

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
    def displayError(self, msg=" error "):
        self.equation.set(" error ")
        self.expression = ""

    def enterKey(self, event):
        self.equalpress()

    # removes leading zeros
    def fixZeros(self, s):
        s = list(s)
        i = 0
        while i < len(s):
            if i == 0:
                if s[i] is '0' and s[i+1].isdigit():
                    s.pop(i)
                    i -= 1
            elif i == len(s)-1:
                break
            elif s[i] is '0' and not s[i-1].isdigit() and s[i+1].isdigit():
                s.pop(i)
                i -= 1
            i += 1

        return "".join(s)

        # Driver code
if __name__ == "__main__":
    # create a GUI window
    root = Tk()
    root.geometry("300x300")
    my_gui = Calculator(root)
    root.mainloop()
