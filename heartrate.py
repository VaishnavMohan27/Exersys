from tkinter import *
from tkinter import messagebox

print("condition 1 = when user is rest")
print("condition 2 = during exercise or post exercise")

def get_hr():
    heartrate = int(ENTRY1.get())
    return heartrate

def get_age():
    age = int(ENTRY2.get())
    return age

def get_condition():
    condition = int(ENTRY3.get())
    return condition
def check_heartrate(a=""):
    print(a)
    try:
        heartrate = get_hr()
        age = get_age()
        condition = get_condition()
        hr = 220 - age
    except ValueError:
        messagebox.showinfo("result","please enter valid input!!")

    else:
        if condition == 1 and 60<=heartrate<=90:
            res = "Heart rate is normal"
            messagebox.showinfo("result",res)
        elif condition == 1 and heartrate > 90:
            res = "Tachycardia.Consult your Doctor"
            messagebox.showinfo("result",res)
        elif condition == 1 and heartrate < 60:
            res = "Bradycardia.Consult your Doctor"
            messagebox.showinfo("result",res)
        elif condition == 2 and 60 <= heartrate <= hr:
            res = "Heart rate is normal."
            messagebox.showinfo("result",res)
        elif condition == 2 and heartrate > hr:
            res = "Tachycardia.Take rest!"
            messagebox.showinfo("result",res)
        elif condition == 2 and 60 > heartrate :
            res = "Bradycardia.Consult your Doctor"
            messagebox.showinfo("result",res)
        else:
            res = "enter valid data"
            messagebox.showinfo("result",res)

if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>",check_heartrate)
    TOP.geometry("450x400")
    TOP.configure(background="yellow")
    TOP.title("Heart Rate checker")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="yellow", text="Welcome to Heart rate checker", font=("Helvetica", 16, "bold"), pady=3)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="yellow", text="Heart rate value:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="yellow", text="Age:", bd=6,
                   font=("Helvetica", 10,"bold"), pady=5)
    LABLE2.place(x=56, y=120)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=120)
    LABLE3 = Label(TOP, bg="yellow", text="condition:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE3.place(x=55, y=180)
    ENTRY3 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY3.place(x=240, y=180)
 
    BUTTON = Button(bg="green", bd=12, text="Heart rate", padx=30, pady=15, command=check_heartrate,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    TOP.mainloop()








            
