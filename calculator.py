# Python program to  create a simple GUI  
# calculator using Tkinter 
  
# import everything from tkinter module 
from tkinter import *
import math

# A global constant of sorts. MUST UPDATE THIS VALUE WHEN ADD A BUTTON
NUM_BUTTONS = 18
  
class Mathematics:
    def basic(self, expression):
        return str(eval(expression))

    def log10(self, expression):
        try:
            floatValue = float(expression)
            result = math.log10(floatValue)
        except:
            result = "error"
        return result

class Calculator:
    def __init__(self, master):
        self.master = master
         # set the background colour of GUI window 
        self.master.configure(background="light green") 

        #use object instance to access math functions in the Mathematics class
        self.my_math = Mathematics()

        # set the title of GUI window 
        self.master.title("Calculator") 

        # set the configuration of GUI window 
        # According to Geeks for Geeks the below geomtry declaration is not necessary and imposes predefined
        # size limits which would introduce the need for hard coding
        # https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
        # reference: https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
        #self.master.geometry("265x125") 
        #self.master.geometry("400x300") 

        self.numColumns = 4  #use this to change the number of columns
        self.numButtons = NUM_BUTTONS  #IMPORTANT TO UPDATE THIS AFTER ADD BUTTON
        self.numRows = self.numButtons//self.numColumns + 1  #row number starts from 1 since row 0 is for the display

        #example for adding other functionality
        self.Flag = ""

        #will hold the expression entered by the user
        self.expression = ""

        #for more information on tkinter variables see:
        #https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/

        # StringVar() is the variable class 
        # we create an instance of this class 
        # this holds a variable in a class from ktinker
        self.equation = StringVar() 

        #when/if it is needed below is how to declare a
        #boolean variable
        self.boolean_variable = BooleanVar()
        self.boolean_variable.set = (True)

        #and when/if it is needed below is how to declare an intvariable
        # and a double, both initialized via the constuctor instead of
        #separately as above
        self.int_variable = IntVar(self.master, 0)
        self.double_variable = DoubleVar(self.master, 0.0);
  
        # create the text entry box for 
        # showing the expression . 
        self.expression_field = Entry(self.master, textvariable=self.equation) 
  
        # grid method is used for placing 
        # the widgets at respective positions 
        # in table like structure . 
        self.expression_field.grid(columnspan=self.numColumns, ipadx=70) 
    
        self.equation.set('0') 

        self.buttonList = []

        # create buttons using method createButton
        self.buttonList.append(self.createButton(inputText=' 7 ', commandfunc=lambda: self.press(7)) )
        self.buttonList.append(self.createButton(inputText=' 8 ', commandfunc=lambda: self.press(8)) ) 
        self.buttonList.append(self.createButton(inputText=' 9 ',  commandfunc=lambda: self.press(9)) ) 
        self.buttonList.append(self.createButton(inputText=u"\u232B",commandfunc= self.clear )) 
        self.buttonList.append(self.createButton(inputText=' 4 ',commandfunc=lambda: self.press(4)) ) 
        self.buttonList.append(self.createButton(inputText=' 5 ', commandfunc=lambda: self.press(5)) ) 
        self.buttonList.append(self.createButton(inputText=' 6 ', commandfunc=lambda: self.press(6)) ) 
        self.buttonList.append(self.createButton(inputText=u"\u00F7", commandfunc=lambda: self.press("/"))) 
        self.buttonList.append(self.createButton(inputText=' 1 ', commandfunc=lambda: self.press(1)) )  
        self.buttonList.append(self.createButton(inputText=' 2 ', commandfunc=lambda: self.press(2))) 
        self.buttonList.append(self.createButton(inputText=' 3 ', commandfunc=lambda: self.press(3)) ) 
        self.buttonList.append(self.createButton(inputText=' * ', commandfunc=lambda: self.press("*")) ) 
        self.buttonList.append(self.createButton(inputText=' . ', commandfunc=lambda: self.press(".")) ) 
        self.buttonList.append(self.createButton(inputText=' 0 ', commandfunc=lambda: self.press(0)) ) 
        self.buttonList.append(self.createButton(inputText=' + ', commandfunc=lambda: self.press("+")) ) 
        self.buttonList.append(self.createButton(inputText=' - ', commandfunc=lambda: self.press("-")) ) 
        self.buttonList.append(self.createButton(inputText=' = ', commandfunc=self.equalpress) ) 
        self.buttonList.append(self.createButton(inputText='log', commandfunc=lambda: self.setFlag("log")) ) 
        
       
        index = 0
        for row in range (1, self.numRows):
           for column in range(self.numColumns):
               self.buttonList[index].grid(row = row, column = column)
               #print("row= ",row, " column= ", column)
               index += 1
        
        row += 1
        column = 0
        for i in range (index, len(self.buttonList)):
            self.buttonList[index].grid(row = row, column = column)
            #print("row= ",row, " column= ", column)
            index += 1
            column += 1

    def createButton(self,inputText,commandfunc ,write=True,width=7, height = 1  ):
    # this function creates a button, and takes one compulsory argument, the value that should be on the button

        return Button(self.master, text=inputText, fg= 'black', bg = 'red',
            command = commandfunc , height= height, width=width)

    def setFlag(self, flag):
        self.Flag = flag
        self.press(flag)

    # Function to update expressiom 
    # in the text entry box 
    def press(self, num): 
        # point out the global expression variable 
        #global expression 
    
        # concatenation of string 
        self.expression = self.expression + str(num) 
    
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
    
            #global expression 
    
            # eval function evaluate the expression 
            # and str function convert the result 
            # into string 

            if (self.Flag == "log"):  #example of implementing a function
                startIndex = len("log")
                self.expression = self.expression[startIndex:]
                total = self.my_math.log10(self.expression)
            else:
                total = self.my_math.basic(self.expression) #eval takes a string expression and evaluates it
    
            self.equation.set(total) 
    
            # initialze the expression variable 
            # by empty string 
            self.expression = "" 
            self.Flag = ""
    
        # if error is generate then handle 
        # by the except block 
        except: 
    
            self.equation.set(" error ") 
            self.expression = "" 
    
    
    # Function to clear the contents 
    # of text entry box 
    def clear(self): 
        #global expression 
        self.expression = "" 
        self.Flag = ""
        self.equation.set("") 


# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()
