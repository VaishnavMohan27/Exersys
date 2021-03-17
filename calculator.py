from tkinter import *

win = Tk() # This is to create a basic window
win.geometry("240x270")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")


# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enters a number

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# Let us creating a frame for the input field
 
input_frame = Frame(win, borderwidth=5, highlightbackground="black", highlightcolor="black", highlightthickness=1)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=17, bg="#eee", justify=LEFT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=5) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win,bg="grey")
 
btns_frame.pack()
 

 
clear = Button(btns_frame, text = "AC", fg = "black", width = 21, height = 2, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

 
divide = Button(btns_frame, text = "/", fg = "black", width = 6, height = 2, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 3, column = 3, padx = 1, pady = 1)
 

 
seven = Button(btns_frame, text = "7", fg = "black", width = 6, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 6, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 6, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 6, height = 2, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 2, column = 3, padx = 1, pady = 1)
 

 
four = Button(btns_frame, text = "4", fg = "black", width = 6, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 6, height = 2,  bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 6, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 6, height = 2, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 1, column = 3, padx = 1, pady = 1)
 

 
one = Button(btns_frame, text = "1", fg = "black", width = 6, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 6, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 6, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 6, height = 2, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 0, column = 3, padx = 1, pady = 1)
 

 
zero = Button(btns_frame, text = "0", fg = "black", width = 13, height = 2, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 6, height = 2, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 6, height = 2, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop() 
