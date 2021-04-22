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
q14="Avoid alcohol"
q15="Consume less sodium"
q16="DO NOT SMOKE!"
q17="Prevent mosquito bites"
q18="Your mental health matters too"
q19="Eat nuts"
q20="Get 30 minutes of physical activity"
q21="Do no skip breakfast"
q22="Meditate"
q23="Choose walking over travelling by a vehicle for short distances"
q24="Give your eyes a rest"
q25="Wash your hands!"
q26="Eat vitamin supplements if you don't get them in your diet"
q27="Get your sugar levels tested"
q28="Make sure your haemoglobin levels don't drop"
l1=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28]
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
    bttn1["state"]=DISABLED
bttn1=Button(gui,text="GET YOUR HEALTH TIP OF THE DAY!", fg='black', bg='white',command=printter)           
bttn1.pack()
