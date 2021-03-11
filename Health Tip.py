q1='Don’t drink sugar calories!'
q2='Avoid processed junk food (eat real food)'
q3='Get enough sleep!'
q4='Drink some water, especially before meals!'
q5='Avoid bright lights before sleep'
q6='Take vitamin D3 if you don’t get much sun exposure!'
q7='Eat vegetables and fruits'
q8='Make sure to eat enough protein'
q9='Do some cardio!!'
q10='Minimize your sugar intake'
q11='Don’t eat a lot of refined carbs!'
q12='Check your blood pressure regularly'
q13='Take antibiotics only as prescribed!'
l1=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]
import random
from tkinter import *
gui=Tk()
gui.title("Health Tip Generator")
gui.geometry("200x200")
def printter():
    var=StringVar()
    var.set(random.choice(l1))
    w2=Label(gui,textvariable=var,fg='black',bg='white')
    w2.pack()
bttn1=Button(gui,text="GET YOUR HEALTH TIP", fg='black', bg='white',command=printter)           
bttn1.pack()
