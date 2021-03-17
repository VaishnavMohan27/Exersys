
    #main window
from tkinter import *
import random
from tkinter import messagebox
if __name__ == '__main__':
    #to change the frame
    def change_frame(frame):
        frame.tkraise()
    root=Tk()
    root.title("Exersys")
    root.geometry("500x500")
    sugar_monitor=Frame(root)
    bp_monitor=Frame(root)
    heart_rate=Frame(root)
    health_tip=Frame(root)
    movie_quote=Frame(root)
    bmi=Frame(root)
    main_window=Frame(root)
    tic_tac=Frame(root)
    random_workout=Frame(root)
    timer=Frame(root)
    pedometer=Frame(root)
    phonebook=Frame(root)
    calculator=Frame(root)
    for frame in (main_window,sugar_monitor,bp_monitor,movie_quote,heart_rate,health_tip,bmi,tic_tac,random_workout,timer,pedometer,phonebook,calculator):
        frame.grid(row=2000, column=2000,sticky="news")
    change_frame(main_window)
    button101=Button(main_window,text="Welcome to exersys", command=lambda:change_frame(bmi))
    button101.place(x=45,y=45)
    #bmi calculator
    def get_height():
        height = float(ENTRY12.get())
        return height
    def get_weight():
        weight =float(ENTRY11.get())
        return weight
    def calculate_bmi():
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
    LABLE11 = Label(bmi,text="BMI Calculator")
    LABLE11.place(x=20, y=0)
    LABLE12 = Label(bmi,text="Enter Weight (in kg):")
    LABLE12.place(x=10, y=30)
    ENTRY11 = Entry(bmi)
    ENTRY11.place(x=120, y=30)
    LABLE13 = Label(bmi,text="Enter Height (in cm):")
    LABLE13.place(x=10, y=60)
    ENTRY12 = Entry(bmi)
    ENTRY12.place(x=120, y=60)
    BUTTON11 = Button(bmi,text="BMI",command=calculate_bmi)
    BUTTON11.grid(row=3, column=0, sticky=W)
    BUTTON11.place(x=100, y=80)
    next_btn1 = Button(bmi, text="Next", command=lambda:change_frame(health_tip))
    next_btn1.grid(sticky='e')

    #health tip
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
    def printter():
        var=StringVar()
        var.set(random.choice(l1))
        w2=Label(health_tip,textvariable=var,fg='black',bg='white')
        w2.grid()
        bttn11["state"]=DISABLED
    bttn11=Button(health_tip,text="GET YOUR HEALTH TIP!", fg='black', bg='white',command=printter)
    bttn11.place(x=5,y=50)
    prev_btn2 =Button(health_tip, text="Prev", command=lambda:change_frame(bmi))
    prev_btn2.grid(sticky='w')
    next_btn2=Button(health_tip,text="Next",command=lambda:change_frame(movie_quote))
    next_btn2.grid(sticky='e')
    
    #movie_quotes
    q1="I’m not superstitious, but I am a little stitious"
    q2="If I don’t have some cake soon, I might die"
    q3="The worst thing about prison was the dementors"
    q4="Identity theft is not a joke, Jim! Millions of families suffer every year"
    q5="Guess what, I have flaws. What are they? Oh, I don't know. I sing in the shower. Sometimes I spend too much time volunteering. Occasionally I'll hit somebody with my car. So sue me"
    q6="There’s only one thing I hate more than lying: skim milk. Which is water that is lying about being milk"
    q7="Time is money; Money is power; Power is pizza; Pizza is knowledge"
    q8="Just remember, every time you look up at the moon, I, too, will be looking at a moon. Not the same moon, obviously, That’s impossible"
    q9="I’m allergic to sushi. Every time I eat more than 80 sushis I barf"
    q10="Be the best version fof YOU"
    q11="May the Force be with you"
    q12="I'm gonna make him an offer he can't refuse"
    q13="I love the smell of napalm in the morning"
    q14="A census taker once tried to test me. I ate his liver with some fava beans and a nice chianti"
    q15="There's no place like home"
    q16="My mama always said life was like a box of chocolates. You never know what you are gonna get"
    q17="Elementary, my dear Watson"
    q18="Hasta la vista, baby"
    q19="A martini. Shaken, not stirred"
    q20="I feel the need. The need for speed"
    q21="To infinity and beyond"
    q22="E.T phone home"
    q23="Get busy livin' or get busy dyin'"
    q24="You've got to ask yourself one question: 'Do I feel lucky?' Well, do ya, punk?"
    q25="You can't handle the truth!"
    movie_list=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25]
    def printter():
        var=StringVar()
        var.set(random.choice(movie_list))
        w2=Label(movie_quote,textvariable=var,fg='black',bg='white')
        w2.grid()
        bttn12["state"]=DISABLED
    bttn12=Button(movie_quote,text="Your movie quote of the day!", fg='black', bg='white',command=printter)
    bttn12.grid()
    prev_btn3 =Button(movie_quote, text="Prev", command=lambda:change_frame(health_tip))
    prev_btn3.grid(sticky='w')
    next_btn3=Button(movie_quote,text="Next",command=lambda:change_frame(bp_monitor))
    next_btn3.grid(sticky='e')

    #blood pressure
    def get_sbp():
        sbp = int(ENTRY41.get())
        return sbp
    def get_dbp():
        dbp = int(ENTRY42.get())
        return dbp
    def see_bp(a=""):
        print(a)  
        try:
            sbp = get_sbp()
            dbp = get_dbp()
        except ValueError:
            messagebox.showinfo("Result","Please enter valid data!")
        else:    
            if sbp in range(90,121) and dbp in range(60,81):
                res = "Your blood pressure is normal"
                messagebox.showinfo("Result",res)
            elif sbp in range(121,130):
                res = "Your blood pressure is slightly elevated"
                messagebox.showinfo("result",res)
            elif sbp in range(130,140):
                res = "Stage 1 hypertension. Remember to take care of your body!"
                messagebox.showinfo("result",res)
            elif sbp in range(140,150) and dbp in range(90,120):
                res = "Stage 2 hypertension. Cut back on the sodium and exercise!"
                messagebox.showinfo("result",res)
            elif sbp >= 150 and dbp >= 120:
                res = "Hypertensive crisis.Call 911!"
                messagebox.showinfo("result",res)    
            elif sbp <= 90  and dbp <=60:
                res = "Low blood pressure.Call 911!"
                messagebox.showinfo("result",res)
                BUTTON["state"]=DISABLED
    
    LABLE41= Label(bp_monitor,text="BP visualizer")
    LABLE41.place(x=20, y=0)
    LABLE42 = Label(bp_monitor, text="Systolic:")
    LABLE42.place(x=20, y=30)
    ENTRY41 = Entry(bp_monitor)
    ENTRY41.place(x=90, y=30)
    LABLE43 = Label(bp_monitor,text="Diastolic")
    LABLE43.place(x=20, y=60)
    ENTRY42= Entry(bp_monitor)
    ENTRY42.place(x=90, y=60)
    BUTTON41= Button(bp_monitor,text="BP",command=see_bp)
    BUTTON41.grid(row=3, column=0, sticky=W)
    BUTTON41.place(x=60, y=80)
    next_btn4 = Button(bp_monitor, text="Prev", command=lambda:change_frame(health_tip))
    next_btn4.grid(sticky='e')
    next_btn4= Button(bp_monitor, text="Next", command=lambda:change_frame(tic_tac))
    next_btn4.grid(sticky='w')

    #tic-tac-toe
    from functools import partial 
    from copy import *
    sign=0  
    # Creates an empty board 
    global board 
    board = [[" " for x in range(3)] for y in range(3)] 
      
    # Check l(O/X) won the match or not 
    # according to the rules of the game 
    def winner(b, l): 
        return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
                (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
                (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
                (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
                (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
                (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
                (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
                (b[0][2] == l and b[1][1] == l and b[2][0] == l)) 
       
    # Check if the player can push the button or not 
    def isfree(i, j): 
        return board[i][j] == " "
      
    # Check the board is full or not 
    def isfull(): 
        flag = True
        for i in board: 
            if(i.count(' ') > 0): 
                flag = False
        return flag
    # Decide the next move of system 
    def pc(): 
        possiblemove = [] 
        for i in range(len(board)): 
            for j in range(len(board[i])): 
                if board[i][j] == ' ': 
                    possiblemove.append([i, j])
                    
        move = [] 
        if possiblemove == []: 
            return
        else: 
            for let in ['O', 'X']: 
                for i in possiblemove: 
                    boardcopy = deepcopy(board) 
                    boardcopy[i[0]][i[1]] = let 
                    if winner(boardcopy, let): 
                        return i 
            corner = [] 
            for i in possiblemove: 
                if i in [[0, 0], [0, 2], [2, 0], [2, 2]]: 
                    corner.append(i) 
            if len(corner) > 0: 
                move = random.randint(0, len(corner)-1) 
                return corner[move] 
            edge = [] 
            for i in possiblemove: 
                if i in [[0, 1], [1, 0], [1, 2], [2, 1]]: 
                    edge.append(i) 
            if len(edge) > 0: 
                move = random.randint(0, len(edge)-1) 
                return edge[move] 
      
    # Configure text on button while playing with system 
    def get_text_pc(i, j, gb, l1, l2): 
        global sign 
        if board[i][j] == ' ': 
            if sign % 2 == 0: 
                l1.config(state=DISABLED) 
                l2.config(state=ACTIVE) 
                board[i][j] = "X"
            else: 
                button[i][j].config(state=ACTIVE) 
                l2.config(state=DISABLED) 
                l1.config(state=ACTIVE) 
                board[i][j] = "O"
            sign += 1
            button[i][j].config(text=board[i][j]) 
        x = True
        if winner(board, "X"):
            gd.destroy()
            x = False
            messagebox.showinfo("WELL PLAYED","WELL PLAYED")
            gb.destroy()
            change_frame(tic_tac)
        elif winner(board, "O"):
            gb.destroy()
            x = False
            messagebox.showinfo("GAME OVER!!","GAME OVER!!")
            change_frame(tic_tac)
        elif (isfull()):
            gb.destroy()
            x = False
            messagebox.showinfo("GAME TIED","GAME TIED")
            change_frame(tic_tac)
        if(x): 
            if sign % 2 != 0: 
                move = pc() 
                button[move[0]][move[1]].config(state=DISABLED) 
                get_text_pc(move[0], move[1], gb, l1, l2) 
      
    # Create the GUI of game board for play along with system 
    def gameboard_pc(game_board, l1, l2): 
        global button 
        button = [] 
        for i in range(3): 
            m = 3+i 
            button.append(i) 
            button[i] = [] 
            for j in range(3): 
                n = j 
                button[i].append(j) 
                get_t = partial(get_text_pc, i, j, game_board, l1, l2) 
                button[i][j] = Button( 
                    game_board, bd=5, command=get_t, height=5, width=10)
                button[i][j].grid(row=m, column=n, sticky ="nesw") 
        game_board.mainloop() 
      
    # Initialize the game board to play with system 
    def withpc(game_board): 
        game_board.destroy() 
        game_board = Tk() 
        game_board.title("Tic Tac Toe") 
        l1 = Button(game_board, text="Player : X", width=10) 
        l1.grid(row=1, column=1) 
        l2 = Button(game_board, text = "Computer : O", 
                    width = 10, state = DISABLED) 
          
        l2.grid(row = 2, column = 1) 
        gameboard_pc(game_board, l1, l2) 
        
    # main function 
    def play():
        wpc = partial(withpc, tic_tac)
        head = Button(tic_tac, text = " TIC-TAC-TOE ", width =20)
        B1 = Button(tic_tac, text = "Play", width =15, command = wpc)
        head.grid()
        B1.grid()
    if __name__ == '__main__':
        play()

    next_btn5= Button(tic_tac, text="Prev", command=lambda:change_frame(bp_monitor))
    next_btn5.grid()
    next_btn5 = Button(tic_tac, text="Next", command=lambda:change_frame(random_workout))
    next_btn5.grid()

    #random workout
    q1="15 Lunges and 20 Pushups"
    q2="20 Russian Twists and 1 minute Plank"
    q3="40 Squats and 40 Crunches"
    q4="60 High Knees and 50 Deadlifts"
    q5="50 Mountain Climbers and 30 Overhead Presses"
    q6="40 Reverse Crunches and 30 Burpees"
    q7="30 Side Planks and 20 Supermans"
    q8="20 Jumping Jacks and 1 minute wall sit"
    q9="10 Sprawls and 10 Air Squats"
    q10="20 Leg Raises and 20 Leg Lift Crunches"
    workouts=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

    def printer():
        var1=StringVar()
        var1.set(random.choice(workouts))
        var2=StringVar()
        var2.set(random.choice(workouts))
        w2=Label(random_workout,textvariable=var1, fg='black', bg='white')
        w3=Label(random_workout,textvariable=var2, fg='black', bg='white')
        w2.grid()
        w3.grid()
        btn6["state"]=DISABLED
    btn6=Button(random_workout,text="Your Workout of the day", fg='black', bg='white', command=printer)
    btn6.grid()
    prev_btn6= Button(random_workout, text="Prev", command=lambda:change_frame(tic_tac))
    prev_btn6.grid()
    next_btn6=Button(random_workout,text="Next",command=lambda:change_frame(sugar_monitor))
    next_btn6.grid()

    #blood sugar monitor
    print("food level 1 = when user is fasting")
    print("food level 2 = when user is between meals")
    print("food level 3 = when user has just finished eating")

    def get_bs():
        bloodsugar = int(ENTRY71.get())
        return bloodsugar

    def get_foodlvl():
        foodlevel = int(ENTRY72.get())
        return foodlevel

    def check_bloodsugar(a=""):
        print(a)
        try:
            bloodsugar = get_bs()
            foodlevel = get_foodlvl()

        except ValueError:
            messagebox.showinfo("result", "please enter valid input!!")

        else:
            if foodlevel == 2 and bloodsugar < 3:
                res = "Severely hypoglycemic. Eat more cake"
                messagebox.showinfo("result", res)
            elif foodlevel == 2 and 3 <= bloodsugar < 4:
                res = "Hypoglycemic. Take care of yourself!"
                messagebox.showinfo("result", res)
            elif foodlevel == 2 and 4 <= bloodsugar < 7:
                res = "Normal blood sugar levels. Good job!"
                messagebox.showinfo("result", res)
            elif foodlevel == 2 and 7 <= bloodsugar < 10:
                res = "Hyperglycemic. Maybe you should not eat that cake after all"
                messagebox.showinfo("result", res)
            elif foodlevel == 2 and bloodsugar >= 10:
                res = "Severely Hyperglycemic. Oops."
                messagebox.showinfo("result", res)
            elif foodlevel == 1 and bloodsugar < 4:
                res = "Hypoglycemic.Eat more cake"
                messagebox.showinfo("result", res)
            elif foodlevel == 1 and 4 <= bloodsugar < 5:
                res = "Normal blood sugar levels.Good job!"
                messagebox.showinfo("result", res)
            elif foodlevel == 1 and 5 <= bloodsugar < 7:
                res = "Hyperglycemic. Maybe you should not eat that cake after all"
                messagebox.showinfo("result", res)
            elif foodlevel == 1 and bloodsugar >= 7:
                res = "Severely Hyperglycemic. Oops."
                messagebox.showinfo("result", res)
            elif foodlevel == 3 and 3 <= bloodsugar < 7:
                res = "Hypoglycemic. Take care of yourself"
                messagebox.showinfo("result", res)
            elif foodlevel == 3 and 7 <= bloodsugar < 11:
                res = "Normal blood sugar levels.Good job!"
                messagebox.showinfo("result", res)
            elif foodlevel == 3 and 11 <= bloodsugar < 16:
                res = "Hyperglycemic. Maybe you should not eat that cake after all"
                messagebox.showinfo("result", res)
            elif foodlevel == 3 and bloodsugar >= 16:
                res = "Severely Hyperglycemic. Oops"
                messagebox.showinfo("result", res)



    LABLE71= Label(sugar_monitor, bg="white")
    LABLE71.place(x=20, y=20)
    LABLE72 = Label(sugar_monitor, bg="white", text="Blood sugar:")
    LABLE72.place(x=20, y=40)
    ENTRY71= Entry(sugar_monitor)
    ENTRY71.place(x=90, y=40)
    LABLE73 = Label(sugar_monitor, bg="white", text="food level:")
    LABLE73.place(x=20, y=70)
    ENTRY72= Entry(sugar_monitor)
    ENTRY72.place(x=90, y=70)
    BUTTON71= Button(sugar_monitor,bg="white",text="Blood sugar",command=check_bloodsugar)
    BUTTON71.place(x=55,y=85)
    

    prev_btn7= Button(sugar_monitor, text="Prev", command=lambda: change_frame(random_workout))
    prev_btn7.grid()
    next_btn7= Button(sugar_monitor, text="Next", command=lambda: change_frame(heart_rate))
    next_btn7.grid()

    #heart rate
    print("condition 1 = when user is at rest")
    print("condition 2 = immediately after exercise")

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
            messagebox.showinfo("result", "please enter valid input!!")

        else:
            if condition == 1 and 60 <= heartrate <= 90:
                res = "Heart rate is normal"
                messagebox.showinfo("result", res)
            elif condition == 1 and heartrate > 90:
                res = "Tachycardia.Consult your Doctor"
                messagebox.showinfo("result", res)
            elif condition == 1 and heartrate < 60:
                res = "Bradycardia.Consult your Doctor"
                messagebox.showinfo("result", res)
            elif condition == 2 and 60 <= heartrate <= hr:
                res = "Heart rate is normal."
                messagebox.showinfo("result", res)
            elif condition == 2 and heartrate > hr:
                res = "Tachycardia.Take rest!"
                messagebox.showinfo("result", res)
            elif condition == 2 and 60 > heartrate:
                res = "Bradycardia.Consult your Doctor"
                messagebox.showinfo("result", res)
            else:
                res = "enter valid data"
                messagebox.showinfo("result", res)



    LABLE = Label(heart_rate, bg="white")
    LABLE.place(x=0,y=0)
    LABLE1 = Label(heart_rate, bg="white", text="Heart rate value:")
    LABLE1.place(x=30, y=5)
    ENTRY1 = Entry(heart_rate)
    ENTRY1.place(x=65, y=5)
    LABLE2 = Label(heart_rate, bg="white", text="Age:")
    LABLE2.place(x=30, y=35)
    ENTRY2 = Entry(heart_rate)
    ENTRY2.place(x=65, y=35)
    LABLE3 = Label(heart_rate, bg="white", text="condition:")
    LABLE3.place(x=30, y=65)
    ENTRY3 = Entry(heart_rate)
    ENTRY3.place(x=65, y=65)
    BUTTON = Button(heart_rate,bg="white",text="Heart rate",command=check_heartrate)
    BUTTON.place(x=55,y=85)
    
    prev_btn9 = Button(heart_rate, text="Prev", command=lambda: change_frame(sugar_monitor))

    prev_btn9.grid()
    next_btn9= Button(heart_rate, text="Next", command=lambda: change_frame(pedometer))
    next_btn9.grid()

    #pedometer
    import pandas as ps
    import csv
    label1=Label(pedometer,text="Compare your weight and steps walked to find the calories burnt")
    label1.place(x=90,y=90)
    filesss = ps.read_csv('pedometer.csv')
    print(filesss)
    prev_btn8= Button(pedometer, text="Prev", command=lambda: change_frame(heart_rate))
    prev_btn8.grid()
    next_btn8= Button(pedometer, text="Next", command=lambda: change_frame(phonebook))
    next_btn8.grid()

    #phonebook
    first_names = ["Shivani", "Vaishnav", "Vishal", "Micheal", "Frodo"]
    last_names = ["S", "Mohan", "DB", "Scott", "Baggins"]
    numbers = ["7676715534", "7839345670", "834659385", "8843934983", "9990433853"]
    def obtains():
        a = txt1.get()
        first_names.append(a)
        b = txt3.get()
        last_names.append(b)
        c = txt4.get()
        numbers.append(c)
    def entry():
        wind = Tk()
        wind.title("Add a contact")
        wind.geometry("200x200")
        w1 = Label(wind, text="Enter their first name", fg='black')
        w1.grid()
        txt1 = Entry(wind)
        txt1.grid()
        w3 = Label(wind, text="Enter their last name", fg='black')
        w3.grid()
        txt3 = Entry(wind)
        txt3.grid()
        w4 = Label(wind, text="Enter their number", fg='black')
        w4.grid()
        txt4 = Entry(wind)
        txt4.grid()
        w5 = Button(wind, text="Confirm?", fg='black', command=obtains)
        w5.grid()
    def viewer():
        wind = Tk()
        wind.title("View contacts")
        wind.geometry("200x200")
        for i in range(len(first_names)):
            b = Label(wind, text=first_names[i])
            b.grid(row=i, column=0)
            c = Label(wind, text=last_names[i])
            c.grid(row=i, column=1)
            d = Label(wind, text=numbers[i])
            d.grid(row=i, column=2)
    bttn8= Button(phonebook, text='Add a contact', fg='black', bg='white', command=entry)
    bttn8.grid()
    bttn82 = Button(phonebook, text='View existing contacts', fg='black', bg='white', command=viewer)
    bttn82.grid()
    prev_btn10 = Button(phonebook, text="Prev", command=lambda: change_frame(pedometer))
    prev_btn10.grid()
    next_btn10= Button(phonebook, text="Next", command=lambda: change_frame(timer))
    next_btn10.grid()

    #timer
    import time
    # Declaration of variables
    hour=StringVar()
    minute=StringVar()
    second=StringVar()

    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    # Use of Entry class to take input from the user
    hourEntry= Entry(timer, bg="grey", textvariable=hour)
    hourEntry.place(x=30,y=20)
    minuteEntry= Entry(timer, bg="grey", textvariable=minute)
    minuteEntry.place(x=80,y=20)
    secondEntry= Entry(timer, bg="grey",textvariable=second)
    secondEntry.place(x=130,y=20)


    def submit():
        try:
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            mins,secs = divmod(temp,60)
            hours=0
            if mins >60:
                hours, mins = divmod(mins, 60)
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            timer.update()
            time.sleep(1)
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")

            temp -= 1
    btn11= Button(timer, text='Set Time Countdown',bg="red3", command= submit)
    btn11.place(x = 40,y = 90)
    prev_btn11= Button(timer, text="Prev", command=lambda: change_frame(phonebook))
    prev_btn11.grid()
    next_btn11 = Button(timer, text="Next", command=lambda: change_frame(calculator))
    next_btn11.grid()

    #calculator
    # 'btn_click' function :
    # This Function continuously updates the
    # input field whenever you enters a number

    def btn_click(item):
        global expression
        expression = expression + str(item)
        input_text.set(expression)

    def bt_clear():
        global expression
        expression = ""
        input_text.set("")

    def bt_equal():
        global expression
        result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
        input_text.set(result)
        expression = ""

    expression = ""

    # 'StringVar()' :It is used to get the instance of input field

    input_text = StringVar()


    input_frame = Frame(calculator, highlightbackground="black")

    input_frame.pack(side=TOP)

    # Let us create a input field inside the 'Frame'

    input_field = Entry(input_frame, textvariable=input_text, width=35, bg="#eee",
                        justify=LEFT)

    input_field.grid(row=0, column=0)

    input_field.pack(ipady=5)  # 'ipady' is internal padding to increase the height of input field

    # Let us creating another 'Frame' for the button below the 'input_frame'

    btns_frame = Frame(calculator, bg="grey")

    btns_frame.pack()

    clear = Button(btns_frame, text="AC", fg="black", width=21, height=2, bg="#eee", cursor="hand2",
                   command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

    divide = Button(btns_frame, text="/", fg="black", width=6, height=2, bg="#eee", cursor="hand2",
                    command=lambda: btn_click("/")).grid(row=3, column=3, padx=1, pady=1)

    seven = Button(btns_frame, text="7", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                   command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

    eight = Button(btns_frame, text="8", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                   command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

    nine = Button(btns_frame, text="9", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

    multiply = Button(btns_frame, text="*", fg="black", width=6, height=2, bg="#eee", cursor="hand2",
                      command=lambda: btn_click("*")).grid(row=2, column=3, padx=1, pady=1)

    four = Button(btns_frame, text="4", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

    five = Button(btns_frame, text="5", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

    six = Button(btns_frame, text="6", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

    minus = Button(btns_frame, text="-", fg="black", width=6, height=2, bg="#eee", cursor="hand2",
                   command=lambda: btn_click("-")).grid(row=1, column=3, padx=1, pady=1)

    one = Button(btns_frame, text="1", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

    two = Button(btns_frame, text="2", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

    three = Button(btns_frame, text="3", fg="black", width=6, height=2, bg="#fff", cursor="hand2",
                   command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

    plus = Button(btns_frame, text="+", fg="black", width=6, height=2, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("+")).grid(row=0, column=3, padx=1, pady=1)

    zero = Button(btns_frame, text="0", fg="black", width=13, height=2, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

    point = Button(btns_frame, text=".", fg="black", width=6, height=2, bg="#eee", cursor="hand2",
                   command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

    equals = Button(btns_frame, text="=", fg="black", width=6, height=2, bg="#eee", cursor="hand2",
                    command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)
    prev_btn12= Button(calculator, text="Prev", command=lambda: change_frame(timer))
    prev_btn12.grid()

root.mainloop()







            
