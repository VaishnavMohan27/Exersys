from tkinter import *
from tkinter import messagebox


def get_height():
    height = float(ENTRY2.get())
    return height


def get_weight():
    weight = float(ENTRY1.get())
    return weight

def calculate_bmi(a=""):   # "a" is there because the bind function gives an argument to the function....
    print(a)
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)


if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("250x120")
    TOP.title("BMI Calculator")
    LABLE = Label(TOP,text="BMI Calculator")
    LABLE.place(x=20, y=0)
    LABLE1 = Label(TOP,text="Enter Weight (in kg):")
    LABLE1.place(x=20, y=30)
    ENTRY1 = Entry(TOP)
    ENTRY1.place(x=150, y=30)
    LABLE2 = Label(TOP,text="Enter Height (in cm):")
    LABLE2.place(x=20, y=60)
    ENTRY2 = Entry(TOP)
    ENTRY2.place(x=150, y=60)
    BUTTON = Button(text="BMI",command=calculate_bmi)
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=130, y=90)
    TOP.mainloop()





