#imported files
import calendar
import random
from tkinter import *
from datetime import datetime
#------------------------contact---------------------------------
def save_contact(contact):
    name = input("Enter name : ")
    ph_no = input("Enter phone number : ")
    contact[name] = ph_no
    print()
    print("Contact will successfully saved.")

def search_contact(contact):
    print()
    s_name = input("Enter name to search person : ")
    if s_name in contact:
        print("-----------------------------")
        print(f"| {s_name} contact number is : {contact[s_name]} |")
        print("-----------------------------")
        print()
    else:
        print()
        print("The name was Not there..! (or) Incorrect Name")
        print("Please enter correct name")
        print()

def delete_contact(contact):
    print()
    d_name = input("Enter a name to delete : ")
    if d_name in contact:

        print("Conformation!")
        print()
        conf = input("Please select (yes/no) to delete the contact : ")
        if conf == 'yes' or conf == 'YES':
            contact.pop(d_name)
            print("The contact was successfully removed")
            print()
        else:
            print("Thank You..!")
            print()
    else:
        print("The name was not avalible (or) Incorrect Name")
        print()

def display_contact(contact):
    print()
    print("-" * 34) 
    print(" Name \t\tContact Number ")
    for i in contact: 
        print("*{}\t\t{}".format(i,contact.get(i)))
    print("-"*34)
    print()
#-------------------------------------contact--------------------------------
    
#-------------------------------------calendar-------------------------------
def phone_calender():
    x = calendar.calendar(2024)
    print(x)
#-------------------------------------calender-------------------------------
    
#---------------------------------digital calculator-----------------------------
def calculator():

    root = Tk()

    input = Entry(root, width=50)
    input.grid(row=0,column=0,columnspan=3,padx=15,pady=15)
    def click(num):
        current = input.get()
        input.delete(0,END)
        input.insert(0,str(current) + str(num))
    def add():
        current = input.get()
        global fnum
        fnum = int(current)
        input.delete(0,END)
        return
    def clear():
        input.delete(0,END)
    def equal():
        current = input.get()
        snum = int(current)
        input.delete(0,END)
        input.insert(0,fnum + snum)
    button_1 = Button(root, text="1",padx=50,pady=25,command=lambda : click(1))
    button_2 = Button(root, text="2",padx=50,pady=25,command=lambda : click(2))
    button_3 = Button(root, text="3",padx=50,pady=25,command=lambda : click(3))
    button_4 = Button(root, text="4",padx=50,pady=25,command=lambda : click(4))
    button_5 = Button(root, text="5",padx=50,pady=25,command=lambda : click(5))
    button_6 = Button(root, text="6",padx=50,pady=25,command=lambda : click(6))
    button_7 = Button(root, text="7",padx=50,pady=25,command=lambda : click(7))
    button_8 = Button(root, text="8",padx=50,pady=25,command=lambda : click(8))
    button_9 = Button(root, text="9",padx=50,pady=25,command=lambda : click(9))
    button_0 = Button(root, text="0",padx=50,pady=25,command=lambda : click(0))
    button_add = Button(root, text="+",padx=106,pady=25,command=add)
    button_clear = Button(root, text="AC",padx=45,pady=25,command=clear)
    button_equal = Button(root, text="=",padx=106,pady=25,command=equal)

    button_7.grid(row=1,column=0)
    button_8.grid(row=1,column=1)
    button_9.grid(row=1,column=2)

    button_4.grid(row=2,column=0)
    button_5.grid(row=2,column=1)
    button_6.grid(row=2,column=2)

    button_3.grid(row=3,column=0)
    button_2.grid(row=3,column=1)
    button_1.grid(row=3,column=2)
    button_0.grid(row = 4,column=0)

    button_add.grid(row=4,column=1,columnspan=2)
    button_clear.grid(row=5,column=0)
    button_equal.grid(row=5,column=1,columnspan=2)
    root.mainloop()
#-----------------------------digital calculator--------------------------------
    
#-----------------------------Normal calculator---------------------------------
    
def normal_calculator():
    print()
    print("1. Addition        2. Subraction")
    print("3. Multiplication  4. divition")
    print("5.Exit")
    print()
    while True:
        calc_user = input("Select any one of the operation : ")
        if calc_user == '1':   
            a,b = map(int, input("Enter 2 Numbers : ").split())
            print()
            print("Answer : ",(a+b))
            print()
        elif calc_user == '2':
            a,b = map(int, input("Enter 2 Numbers : ").split())
            print()
            print("Answer : ",(a-b))
            print()
        elif calc_user == '3':
            a,b = map(int, input("Enter 2 Numbers : ").split())
            print()
            print("Answer : ",(a*b))
            print()
        elif calc_user == '4':
            a,b = map(int, input("Enter 2 Numbers : ").split())
            print()
            print("Answer : ",(a/b))
            print()
        elif calc_user == '5':
            break
        else:
            print()
            print("Please enter the correct option...!")
            print()
#-----------------------------Normal calculator------------------------
            
#-----------------------------time & date------------------------------
def time_date():
    print()
    print("Date & Time")
    current_time = datetime.now()
    print("Current time is : ",current_time.time())
    print("Date : ",current_time.date())
    print()
    print("Have a nice day!")
#-----------------------------time & date------------------------------

#-----------------------------games rock,papper,sis--------------------
def r_p_s():
    while True:
        choices = ["rock","papper","scissors"]

        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input("ROCK,PAPPER,SCISSSORS : ")

        if player == computer:
            print("computer : ",computer)
            print("player : ",player)
            print("Tie!")
        elif player == "rock":
            if computer == "papper":
                print("computer : ",computer)
                print("player : ",player)
                print("You Lose!")
            if computer == "scissors":
                print("computer : ",computer)
                print("player : ",player)
                print("You Win!")

        elif player == "scissors":
            if computer == "rock":
                print("computer : ",computer)
                print("player : ",player)
                print("You Lose!")
            if computer == "papper":
                print("computer : ",computer)
                print("player : ",player)
                print("You Win!")

        elif player == "papper":
            if computer == "scissors":
                print("computer : ",computer)
                print("player : ",player)
                print("You Lose!")
            if computer == "rock":
                print("computer : ",computer)
                print("player : ",player)
                print("You Win!")

        play_again = input("Play again ? (yes/no) : ")
        if play_again != "yes":
            break
    print("bye!")
    print("Have A Nice Day")
#-----------------------------games rock,papper,sis--------------------

#-----------------------------QUIZ game--------------------
def quiz_game():

    def newgame():
        g = []   #guesses
        cg = 0   #correcr_guesses
        qn = 1   #Question_number
        print()
        print("Hello there...! it's a gendral Quiz game to select the correct option and you will get the score")
        print("Good Luck!!!")
        for key in questions:
            print("---------------------------------------------------------------------------------")
            print(key)
            for i in options[qn-1]:
                print(i)
            guess = input("Enter (A, B, C or D): ")
            guess = guess.upper()
            g.append(guess)
            cg += checkanswer(questions.get(key),guess)
            qn += 1
        displayscore(cg, g)
    def checkanswer(answer, guess): 
        if answer == guess:
            print("CORRECT!")
            return 1
        else:
            print("WORNG!")
            return 0
    def displayscore(cg,g):
        print("-------------------")
        print("RESULTS")
        print("-------------------")
        print("ANSWERS: ", end="")
        for i in questions:
            print(questions.get(i), end="")
        print()
        print("GUESSES : ", end="")
        for i in g:
            print(i, end=" ")
        print()
        score = int((cg/len(questions))*100)
        print("your Score is : "+str(score)+"%")
    def play_again():
        pa = input("Play Again (yes/no) : ")
        pa = pa.upper()
        if pa == "YES":
            return True
        else:
            return False
    questions = {
        "How Many Types Of Keys In Python ? :" : "C",
        "Single comment line in  Python ? :" : "A",
        "Python is used to ? :" : "B",
        "Python was relesed publicly in which year ? :" : "D"}
    options = [["A.26","B.52","C.36","D.98"],
            ["A.#comment ","B.'''comment'''","c.<!....comment>","D.*comment"],
            ["A.frame work","B.web & software developement","c.creat app","D.Nothing"],
            ["A.1BC","B.2025","c.1986","D.1991"]]
    newgame()
    while play_again():
        newgame()
    print("Good byee...!")
    print("Have a nice day...!")

#-----------------------------QUIZ game-------------------------------
    
#-----------------------------cricket game----------------------------
def cricket_game():

    while True:

        choices = [1,2,3,4,6]
        computer = random.choice(choices)
        e = 0
        ball = 1
        while True:
            print()
            print(f"ball no : {ball}")
            print()
            player = int(input("Batting : "))
            if player == 5 or player >= 7:
                print("please enter 1 - 4 (or) 6 ")
                e+=0
            else:
                e+=player
            if player != computer:
                    print()
                    print(f"You : {player} -> Bowler : {computer}")
                    ball+=1
            elif player == computer:
                print("------------------")
                print("Bowler : ",computer)
                print("You : ",player)
                print("OUT!")
                print("-----------------")
                print(f"|Your run is : {e}|")
                print("-----------------")
                e = 0
                break
        p_a = input("Do You want play again (y/n) : ")
        if p_a == 'y':
            cricket_game()
        else:
            break
            

#-----------------------------cricket game----------------------------
        

#-----------------------------MAIN FUNCTION----------------------------
def main():
    contact = {}
    print()
    print("-" * 44)
    print("----- Hello There! How Can I Help You? -----")
    print("-" * 44)
    while True:
        print()
        print("---------------------------------------------")
        print("| 1.Phone Book          2.Calendar          |")
        print("|                                           |")
        print("| 3.Digital calculator  4.Normal Calculator |")
        print("|                                           |")
        print("| 5.Time & Date         6.Games             |")
        print("---------------------------------------------")
        print()
        total_application = input("Please Select Your Option : ")
        #phone book application
        if total_application == "1":
            print()
            print("1.save contact \n2.search contact \n3.delete contact \n4.display contact \n5.Exit")
            print()
            user = input("Please select any one : ").strip()
            print()
            if user == '1':
                save_contact(contact)
            elif user == '2':
                search_contact(contact)
            elif user == '3':
                delete_contact(contact)
            elif user == '4':
                display_contact(contact)
            elif user == '5':
                main()
            else:
                print("sorry..! You are entered worng choice")
        #calendar application
        elif total_application == "2":
            print()
            phone_calender()
            print("                          Have a Nice Day...!")
            print()
        #Advance calcunator application
        elif total_application == "3":
            calculator()
        #normal_calculator
        elif total_application == "4":
            normal_calculator()
        #time & data
        elif total_application == "5":
            time_date()
        #games
        elif total_application == "6":
            print()
            print("|-------------------------------------|")
            print("| 1.Rock,Papper,Scissors  2.Quiz game |")
            print("|                                     |")
            print("| 3.Cricket Game          4.Exit      |")
            print("|-------------------------------------|")
            print()
            game_user = input("Choose any one of the game : ")
            if game_user == '1':
                r_p_s()
            elif game_user == '2':
                quiz_game()
            elif game_user == '3':
                cricket_game()

                
main()