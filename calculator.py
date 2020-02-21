# Python program to  create a simple GUI
# calculator using Tkinter
# References:
# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
# https://medium.com/@adeyinkaadegbenro/project-build-a-python-gui-calculator-fc92bddb744d

# import everything from tkinter module
from tkinter import *

import tkinter.font as font  # added this
from math import *
# import texteditor

# A global constant of sorts. The number of columns in the calculator
NUM_COLUMNS = 4
BTN_BG_COLOR = "black"
BTN_TXT_COLOR = "gray"
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
            strVal = format("%8g" % (result))
        except:
            result = "error"
        return strVal


class UnitConversion:

    # Convert from lbs to kg
    def toKg(self, expression):
        conversionFactor = 0.453592
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g" % (result))
        except:
            result = "error"
        return strVal

    # Convert from kg to lbs
    def toLbs(self, expression):
        conversionFactor = 2.20462
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g" % (result))
        except:
            result = "error"
        return strVal

    # Convert from from meters to feet
    def toFt(self, expression):
        conversionFactor = 3.28084
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g" % (result))
        except:
            result = "error"
        return strVal

    # Convert from from feet to meters
    def toM(self, expression):
        conversionFactor = 0.3048
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g" % (result))
        except:
            result = "error"
        return strVal

    # Convert from from kilometers to miles
    def toMi(self, expression):
        conversionFactor = 0.621371
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g" % (result))
        except:
            result = "error"
        return strVal

    # Convert from from miles to kilometers
    def toKm(self, expression):
        conversionFactor = 1.60934
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g" % (result))
        except:
            result = "error"
        return strVal

    # convert Celsius to Fahrenheit
    def toFdeg(self, expression):
        try:
            res = (float(expression) * 1.8) + 32
            strVal = format("%8g" % (res))
        except:
            res = "error"
        return strVal

    # convert Fahrenheit to Celsius
    def toCdeg(self, expression):
        try:
            res = (float(expression) - 32) * (5/9)
            strVal = format("%8g" % (res))
        except:
            res = "error"
        return strVal

    # convert Gallon to Liter
    def toLiter(self, expression):
        try:
            res = float(expression) * 3.78541
            strVal = format("%8g" % (res))
        except:
            res = "error"
        return strVal

    # convert Liter to Gallon
    def toGal(self, expression):
        try:
            res = float(expression) / 3.78541
            strVal = format("%8g" % (res))
        except:
            res = "error"
        return strVal

    # convert Inch to Centimeter
    def toCm(self, expression):
        try:
            res = float(expression) * 2.54
            strVal = format("%8g" % (res))
        except:
            res = "error"
        return strVal

    # convert Centimeter to
    def toIn(self, expression):
        try:
            res = float(expression) / 2.54
            strVal = format("%8g" % (res))
        except:
            res = "error"
        return strVal


class Calculator:
    def __init__(self, master):
        self.master = master
        # set the background colour of GUI window
        self.master.configure(background=CALC_BG_COLOR)

        # screen font 30
        self.screenFont = font.Font(weight="bold", size=30)  # added this

        # button font 20
        self.buttonFont = font.Font(weight="bold", size=20)  # added this

        # Calculation log font 12
        self.buttonFont2 = font.Font(weight="bold", size=12)

        # use object instance to access math functions in the Mathematics class
        self.my_math = Mathematics()

        # EXAMPLE: Create a HelloWorld class object to call the HelloWorld class functions
        self.my_hello = HelloWorld()

        # Creat a Conversion class object to call the Conversion class functions
        self.my_unitConvert = UnitConversion()

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
        self.expFiltered = ""  # holds value with zeros removed

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
        Grid.rowconfigure(self.master, 1, weight=1)
        self.expression_field.grid(
            columnspan=self.numColumns, ipadx=70, sticky=(N, S, E, W))

        # variables to save user entered operands/operator
        self.operands = [None, None]
        self.e_operands = [None, None]
        self.operator = None
        # Flag used to prohibit user from using two decimals in one number
        self.is_decimal = [False, False]

        self.clear_stack = False

        # Variables used to save answer
        self.saved_answer = None
        self.previous_answer = None

        self.equation.set('0')
        # history of all calculations for session
        self.history = []

        self.calculationLog()

        Grid.rowconfigure(self.master, 1, weight=1)
        # Label(self.master, text="calculation log").grid(row=1, column=0,
        #                                                 columnspan=2, sticky=(N, S, E, W))
        Button(self.master, text='<--use', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
               command=self.useLog, width=7, height=1).grid(
            row=1, column=2, sticky=(N, S, E, W))

        Button(self.master, text='hist', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
               command=self.showHistory, width=7, height=1).grid(
            row=1, column=3, sticky=(N, S, E, W))

        # buttons for unit conversion:
        kg_button = "\u2b62" + " kg"
        lbs_button = "\u2b62" + " lbs"
        ft_button = "\u2b62" + " ft"
        m_button = "\u2b62" + " m"
        mi_button = "\u2b62" + " mi"
        km_button = "\u2b62" + " km"

        cDeg_button = "\u2b62 \u00B0" + "C"
        fDeg_button = "\u2b62 \u00B0" + "F"
        liter_button = "\u2b62" + " L"
        gal_button = "\u2b62" + " gal"
        in_button = "\u2b62" + " in"
        cm_button = "\u2b62" + " cm"

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

            Button(self.master, text=' ( ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('('), width=7, height=1),
            Button(self.master, text=' ) ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press(')'), width=7, height=1),
            Button(self.master, text=' UNDO ',  fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
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
            Button(self.master, text='E', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press('E'), width=7, height=1),
            Button(self.master, text=' + ', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("+"), width=7, height=1),

            Button(self.master, text='log', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.setFlag("log"), width=7, height=1),

            Button(self.master, text=kg_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Kg"), width=7, height=1),
            Button(self.master, text=lbs_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Lbs"), width=7, height=1),
            Button(self.master, text=ft_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Ft"), width=7, height=1),
            Button(self.master, text=m_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("M"), width=7, height=1),
            Button(self.master, text=mi_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Mi"), width=7, height=1),
            Button(self.master, text=km_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Km"), width=7, height=1),

            Button(self.master, text=cDeg_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("cDeg"), width=7, height=1),
            Button(self.master, text=fDeg_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("fDeg"), width=7, height=1),
            Button(self.master, text=liter_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("liter"), width=7, height=1),
            Button(self.master, text=gal_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("gal"), width=7, height=1),
            Button(self.master, text=cm_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("cm"), width=7, height=1),
            Button(self.master, text=in_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("in"), width=7, height=1),

            Button(self.master, text='+/-', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.press("negative"),
                   width=7, height=1),

            # EXAMPLE:  add helloworld button
            # Button(self.master, text='HW', fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
            #        command=lambda: self.my_hello.printMessage(self.equation),
            #        width=7, height=1),

            Button(self.master, text=' = ', fg=BTN_TXT_COLOR,
                   bg=BTN_BG_COLOR, command=self.equalpress, width=28, height=1,
                   font=self.buttonFont),
        ]

        self.lengthOfbuttonList = len(self.buttonList)

        # row number starts from 1 since row 0 is for the display
        self.numRows = self.lengthOfbuttonList // self.numColumns + 2

        index = 0
        for row in range(2, self.numRows):
            Grid.rowconfigure(self.master, row, weight=1)  # sticky
            for column in range(self.numColumns):
                Grid.columnconfigure(self.master, column, weight=1)  # sticky
                self.buttonList[index].grid(
                    row=row, column=column, sticky=(N, S, E, W))  # sticky
                # print("row= ",row, " column= ", column)
                index += 1
        print("after row-cols full index = ", index)
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

        print("length of button list = ", self.lengthOfbuttonList)
        print("index= ", index)
        self.buttonList[self.lengthOfbuttonList-1].grid(
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
        # TODO convert E button to operator and add sign button to enable #E-# functionality
        is_operand_data = is_operand_data or num == "E"

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
            if self.e_operands[0] is not None:
                self.display_text += "E" + self.e_operands[0]

            if self.operator is not None:
                self.display_text += self.operator
                if self.operands[1] is not None:
                    self.display_text += self.operands[1]
                    if self.e_operands[1] is not None:
                        self.display_text += "E" + self.e_operands[1]

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
            if self.operands[idx] is None:  # TODO op[0] == 0
                # TODO Load/update current val of operand
                self.operands[idx] = num
            else:
                if num == "negative":
                    if self.e_operands[idx] is not None:
                        if self.e_operands[idx][0] == '-':
                            self.e_operands[idx] = self.e_operands[idx][1:]
                        else:
                            self.e_operands[idx] = "-" + self.e_operands[idx]
                    else:
                        if self.operands[idx][0] == '-':
                            self.operands[idx] = self.operands[idx][1:]
                        else:
                            self.operands[idx] = "-" + self.operands[idx]
                elif num == "E":
                    add_E_to_operand = len(
                        self.operands[idx]) > 0 and self.operands[idx][0].isnumeric()
                    add_E_to_operand = add_E_to_operand or len(
                        self.operands[idx]) > 1 and self.operands[idx][0] == "-"
                    add_E_to_operand = add_E_to_operand and self.e_index < 0

                    if add_E_to_operand:
                        self.e_operands[idx] = "0"
                else:
                    if self.e_operands[idx] is not None:
                        if self.e_operands[idx][0] == "0":
                            self.e_operands[idx] = num
                        elif self.e_operands[idx][0] == "-" and (len(self.e_operands[idx][0]) == 1 or self.e_operands[idx][1] == "0"):
                            self.e_operands[idx] = self.e_operands[idx][0] + num
                        else:
                            self.e_operands[idx] += num
                    else:
                        if self.operands[idx][0] == "0":
                            self.operands[idx] = num
                        elif self.operands[idx][0] == "-" and (len(self.operands[idx][0]) == 1 or self.operands[idx][1] == "0"):
                            self.operands[idx] = self.operands[idx][0] + num
                        else:
                            self.operands[idx] += num
        else:
            self.displayError("invalid key")

    def set_operator(self, operator):
        self.operator = operator
        self.e_index = -1

    # Function to evaluate the final expression
    def equalpress(self, ignore_flag=False):
        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.

        # Put that code inside the try block
        # which may generate the error
        #self.expression_field = self.fixZeros(self.expression_field.get())

        # removes leading zeros
        self.expFiltered = self.fixZeros(self.expression_field.get())
        try:

            # global expression

            # eval function evaluate the expression
            # and str function convert the result
            # into string

            if self.Flag == "log" and not ignore_flag:  # example of implementing a function
                #total = self.my_math.log10(self.expression_field.get())
                total = self.my_math.log10(self.expFiltered)
                self.expFiltered = self.expFiltered + self.Flag
                self.Flag = ""
            else:
                # eval takes a string expression and evaluates it
                #total = self.my_math.basic(self.expression_field.get())
                total = self.my_math.basic(self.expFiltered)
                floatValue = float(total)
                strVal = format("%8g" % (floatValue))
                total = strVal.strip()

            self.equation.set(total)

            # save equations and answers to self.history list
            self.saveHistory()
            self.calculationLog()

            self.previous_answer = total  # save result of operation to previous answer variable
            self.operands[0] = self.previous_answer

            # initialze the expression variable
            # by empty string
            self.operands[0] = None
            self.e_operands[0] = None
            self.operator = None
            self.operands[1] = None
            self.e_operands[1] = None

        # if error is generate then handle
        # by the except block
        except:
            self.displayError()

    # Function to clear the contents
    # of text entry box

    def unitConvert(self, buttonName):

        try:
            if (buttonName == "Kg"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toKg(self.expression)
                self.equation.set(result + " (kg)")
                self.saveHistory()
                self.calculationLog()

            elif (buttonName == "Lbs"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toLbs(self.expression)
                self.equation.set(result + " (lbs)")
                self.saveHistory()
                self.calculationLog()

            elif (buttonName == "Ft"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toFt(self.expression)
                self.equation.set(result + " (ft)")
            elif (buttonName == "M"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toM(self.expression)
                self.equation.set(result + " (m)")
            elif (buttonName == "Mi"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toMi(self.expression)
                self.equation.set(result + " (mi)")
            elif (buttonName == "Km"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toKm(self.expression)
                self.equation.set(result + " (km)")

            elif (buttonName == "fDeg"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toFdeg(self.expression)
                self.equation.set(result + " (\u2b62 \u00B0" + "F)")
            elif (buttonName == "cDeg"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toCdeg(self.expression)
                self.equation.set(result + " (\u2b62 \u00B0" + "C)")

            elif (buttonName == "liter"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toLiter(self.expression)
                self.equation.set(result + " (L)")
            elif (buttonName == "gal"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toGal(self.expression)
                self.equation.set(result + " (gal)")

            elif (buttonName == "cm"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toCm(self.expression)
                self.equation.set(result + " (cm)")
            elif (buttonName == "in"):
                self.expression = self.my_math.basic(
                    self.expression_field.get())
                result = self.my_unitConvert.toIn(self.expression)
                self.equation.set(result + " (in)")

            # self.equation.set(result)

            self.previous_answer = result  # save result of operation to previous answer variable
            self.operands[0] = self.previous_answer

            # initialze the expression variable
            # by empty string
            self.expression = ""
            self.Flag = ""
            self.operator = None
            self.operands[1] = None
        except:
            self.displayError()

    def clear(self):
        # global expression
        self.operands[0] = None
        self.operands[1] = None
        self.e_operands[0] = None
        self.e_operands[1] = None
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
        while True:
            if i == 0:
                if s[i] == '0' and s[i+1].isdigit():
                    s.pop(i)
                    i -= 1
            elif i == len(s)-1 or len(s) < 3:
                break
            elif s[i] == '0' and not s[i-1].isdigit() and s[i+1].isdigit():
                s.pop(i)
                i -= 1
            i += 1

        return "".join(s)

    # save expression and answer to self.history
    def saveHistory(self):
        if self.expFiltered != self.equation.get():
            self.history.append(self.expFiltered + "=" + self.equation.get())

    # write self.history to file

    def history2Txt(self):
        # create output file
        out_file = open("calc_history.txt", "w")

        # add elements in self.history to .txt file
        for i in range(len(self.history)):
            out_file.write(self.history[i] + '.\n')
        out_file.close()

    # opens calc_history.txt file using the systems default editor
    def showHistory(self):
        # write self.history to file
        self.history2Txt()

        # uses texteditor function to open file with default editor
        texteditor.open(filename='calc_history.txt')

    def calculationLog(self, *args):
        if not self.history:
            self.options = ['Calculation Log']
        else:
            self.options = self.history
        self.variable = StringVar(self.master)
        self.variable.set(self.options[-1])  # default value
        b5 = OptionMenu(self.master, self.variable, *self.options)
        b5.config(font=self.buttonFont2, width=10)
        b5.grid(row=1, column=0, columnspan=2, sticky=(N, S, E, W))

    def useLog(self):
        self.clear()
        eq = self.variable.get().split('=')[1]
        self.expression = eq
        self.equation.set(eq)
        self.equalpress()


# Driver code
if __name__ == "__main__":
    # create a GUI window
    root = Tk()
    root.geometry("300x300")
    my_gui = Calculator(root)
    root.mainloop()
