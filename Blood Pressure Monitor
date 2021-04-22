from tkinter import *
from tkinter import messagebox

def get_sbp():
    sbp = int(ENTRY1.get())
    return sbp

def get_dbp():
    dbp = int(ENTRY2.get())
    return dbp
def see_bp(a=""):
    print(a)
    
    try:
        sbp = get_sbp()
        dbp = get_dbp()
    except ValueError:
        messagebox.showinfo("Result","Please enter valid data!")
    else:    

        if 90 < sbp <= 120 or 60 < dbp <= 80:
            res = "Your blood pressure is normal"
            messagebox.showinfo("result",res)
        elif 120 < sbp < 130 or 80 < dbp <= 85:
            res = "Your blood pressure is slightly elevated"
            messagebox.showinfo("result",res)
        elif 130 <= sbp < 140 or 85 < dbp < 90:
            res = "Stage 1 hypertension. Remember to take care of your body!"
            messagebox.showinfo("result",res)
        elif 140 <= sbp < 150 or 90 <= dbp < 120:
            res = "Stage 2 hypertension. Cut back on the sodium and exercise!"
            messagebox.showinfo("result",res)
        elif sbp >= 150 or dbp >= 120:
            res = "Hypertensive crisis.Call 911!"
            messagebox.showinfo("result",res)    
        elif sbp <= 90 or dbp <= 60:
            res = "Low blood pressure.Call 911!"
            messagebox.showinfo("result",res)
        else:
            res = "enter valid data"
            messagebox.showinfo("result",res)

if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>",see_bp)
    TOP.geometry("360x360")
    TOP.configure(background="red3")
    TOP.title("BP visualizer")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="red3", text="Welcome to BP visualizer", font=("Helvetica", 16, "bold"), pady=3)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="red3", text="systolic blood pressure:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="red3", text="diastolic blood pressure:", bd=6,
                   font=("Helvetica", 10,"bold"), pady=5)
    LABLE2.place(x=56, y=120)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=120)
    BUTTON = Button(bg="IndianRed1", bd=12, text="BP", padx=33, pady=15, command=see_bp,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    TOP.mainloop()
    
    
