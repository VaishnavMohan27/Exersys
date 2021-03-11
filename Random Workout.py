l =  ['Lunges : It increase muscle mass to build up strength and tones your body. ' ,
           
     'Pushups : Traditional Pushups are beneficial for building upper body strength. They work the triceps, pectoral muscles, and shoulders. ' ,
           
    'Russian Twist : Helps with twisting movements and allows you to quickly change direction.' ,
           
    'Plank : The plank strengthens your spine, your rhomboids and trapezius, and your abdominal muscles, which naturally result in a strong posture.' ,
           
    'Squats : Squating strengthens your core, crushes calories and strengthens the muscles of your lower body.'
    
    'Crunches : Crunches are ideal for strengthening your core, which includes your lower back muscles and obliques.' ,
           
    'High Knees : High knee strengthens all the muscles in your legs, gets your heart rate up and improves momentum, coordination and flexibility.' ,
           
    'Deadlifts : Deadlifting can increase core strength, core stability and improve your posture.' ,
           
    'Mountiain Climbers : Climbers are good for your heart, helps in building upper body strength and increases core strength.' ,
           
    'Overhead Press : It increases strength and size of the shoulder, triceps, trapezius muscles.' ,
           
    'Reverse Crunches : Strengthens your rectus abdominis.Takes strain off your neck and is less stressful on your back than crunches' ,
      
    'Burpees : A whole-body move that provides great bang for your buck for cardiovascular endurance and muscle strength.',

    'Side Plank : Strengthens three muscle groups at once and protects your spine.Strengthens your core without stressing your back.']


import random
from tkinter import *
gui=Tk()
gui.title("Workout Generator")
gui.geometry("200x200")
def printer():
    var=StringVar()
    var.set(random.choice(l))
    w2=Label(gui,textvariable=var, fg='black', bg='white')
    w2.pack()
btn=Button(gui,text="Your Workout", fg='black', bg='white', command=printer)   
btn.pack()




 
