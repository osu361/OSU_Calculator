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
            result = log10(floatValue)
            strVal = format("%8g"% (result))
        except:
            result = "error"
        return strVal

class UnitConversion:

    # Convert from lbs to kg
    def toKg(self, expression):
        conversionFactor= 0.453592
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g"% (result))
        except:
            result = "error"
        return strVal

    # Convert from kg to lbs
    def toLbs(self, expression):
        conversionFactor= 2.20462
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g"% (result))
        except:
            result = "error"
        return strVal 

    # Convert from from meters to feet
    def toFt(self, expression):
        conversionFactor= 3.28084
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g"% (result))
        except:
            result = "error"
        return strVal 

    # Convert from from feet to meters
    def toM(self, expression):
        conversionFactor= 0.3048
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g"% (result))
        except:
            result = "error"
        return strVal

    # Convert from from kilometers to miles
    def toMi(self, expression):
        conversionFactor= 0.621371
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g"% (result))
        except:
            result = "error"
        return strVal

    # Convert from from miles to kilometers
    def toKm(self, expression):
        conversionFactor= 1.60934
        try:
            floatValue = float(expression)
            result = conversionFactor*floatValue
            strVal = format("%8g"% (result))
        except:
            result = "error"
        return strVal 
    
    # def funcname(self, parameter_list):
    #     pass
        


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
        self.operands = [None, None]
        self.operator = None
        self.is_decimal = [False, False]

        self.clear_stack = False

        self.saved_answer = None
        self.previous_answer = None

        #buttons for unit conversion:
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
            Button(self.master, text=' 9 ',  fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
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

            Button(self.master, text= kg_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Kg"), width=7, height=1),
            Button(self.master, text= lbs_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Lbs"), width=7, height=1),
            Button(self.master, text= ft_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Ft"), width=7, height=1),
            Button(self.master, text= m_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("M"), width=7, height=1),
            Button(self.master, text= mi_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Mi"), width=7, height=1),
            Button(self.master, text= km_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("Km"), width=7, height=1),
            
            Button(self.master, text= cDeg_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("cDeg"), width=7, height=1),
            Button(self.master, text= fDeg_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("fDeg"), width=7, height=1),
            Button(self.master, text= liter_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("liter"), width=7, height=1),
            Button(self.master, text= gal_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("gal"), width=7, height=1),
            Button(self.master, text= cm_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("cm"), width=7, height=1),
            Button(self.master, text= in_button, fg=BTN_TXT_COLOR, bg=BTN_BG_COLOR,
                   command=lambda: self.unitConvert("in"), width=7, height=1),

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
        print("after row-cols full index = ", index)
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

        print("length of button list = ", self.lengthOfbuttonList)
        print("index= ", index)
        self.buttonList[self.lengthOfbuttonList-1].grid(
            row=row, column=0, columnspan=self.numColumns, sticky=(N, S, E, W))

        # listen for enter key
        self.master.bind('<Return>', self.enterKey)

    def setFlag(self, flag):
        self.Flag = flag
        self.press(flag)

    # Function to update expressiom
    # in the text entry box
    def press(self, num:str):
        # point out the global expression variable
        # global expression

        #Refactoring for building operands
        is_operand_data = num.isnumeric() or num == "negative"
        is_operand_data = is_operand_data or num == "."
        is_operand_data = is_operand_data or num == "E"

        if is_operand_data:
            if self.operator is None:
                self.set_operand(0, num)
            else:
                self.set_operand(1, num)

        elif self.Flag is not None or num in "*+-/":
            if self.operator is not None:
                self.equalpress()

            if self.operands[0] is not None:
                self.set_operator(num)
                if self.operator == "log":
                    self.equalpress()

        else:
            self.displayError()

        if self.operands[0] is not None:
            self.expression = self.operands[0]
            if self.operator is not None:
                self.expression += self.operator
                if self.operands[1] is not None:
                    self.expression += self.operands[1]
            self.equation.set(self.expression)
        else:
            self.displayError()


        """
        # concatenation of string
        self.expression += str(num)

        # update the expression by using set method
        self.equation.set(self.expression)
        """

    def set_operand(self, idx, num):

        if num != "." or not self.is_decimal[idx]:
            if self.operands[idx] is None:
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
                self.expression = self.my_math.basic(self.expression_field.get())
                total = self.my_math.log10(self.expression)
                #self.expression = self.expression[startIndex:]
            else:
                # eval takes a string expression and evaluates it
                total = self.my_math.basic(self.expression_field.get())
                floatValue = float(total)
                strVal = format("%8g"% (floatValue))
                total = strVal.strip()

            self.equation.set(total)

            self.previous_answer = total  # save result of operation to previous answer variable
            self.operands[0] = self.previous_answer

            # initialze the expression variable
            # by empty string
            self.expression = ""
            self.Flag = ""
            self.operator = None
            self.operands[1] = None

        # if error is generate then handle
        # by the except block
        except:
            self.displayError()

    # Function to clear the contents
    # of text entry box

    def unitConvert(self, buttonName):

        try:
            if (buttonName == "Kg"):
                self.expression = self.my_math.basic(self.expression_field.get())
                result = self.my_unitConvert.toKg(self.expression)
                self.equation.set(result + " (kg)" )
            elif (buttonName == "Lbs"):
                self.expression = self.my_math.basic(self.expression_field.get())
                result = self.my_unitConvert.toLbs(self.expression)
                self.equation.set(result + " (lbs)")
            elif (buttonName == "Ft"):
                self.expression = self.my_math.basic(self.expression_field.get())
                result = self.my_unitConvert.toFt(self.expression)
                self.equation.set(result + " (ft)")
            elif (buttonName == "M"):
                self.expression = self.my_math.basic(self.expression_field.get())
                result = self.my_unitConvert.toM(self.expression)
                self.equation.set(result  + " (m)" )
            elif (buttonName == "Mi"):
                self.expression = self.my_math.basic(self.expression_field.get())
                result = self.my_unitConvert.toMi(self.expression)
                self.equation.set(result  + " (mi)")
            elif (buttonName == "Km"):
                self.expression = self.my_math.basic(self.expression_field.get())
                result = self.my_unitConvert.toKm(self.expression)
                self.equation.set(result + " (km)")
            
            #self.equation.set(result)

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


# Driver code
if __name__ == "__main__":
    # create a GUI window
    root = Tk()
    root.geometry("300x300")
    my_gui = Calculator(root)
    root.mainloop()


