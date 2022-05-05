import random
computer_score=0
user_score=0
clashed=0
options=["rock","paper","scissors"]
while True:
    user_input=input("Rock/Paper/scissors or Q to quit : ").lower()

    if user_input=="q":
        print("NOT A PROBLEM, TAKE YOUR TIME ")
        break

    elif user_input not in options:
        print("enter a valid input :")
        continue
    computer_input=random.randint(0,2)
    computer_picks=options[computer_input]
    print("computer picked ", computer_picks + ".")
    if user_input =="rock" and computer_picks=="scissors":
        print(" you won!")
        user_score =user_score+1
    elif user_input =="paper" and computer_picks=="rock":
        print(" you won!")
        user_score =user_score+1
    elif user_input =="scissors" and computer_picks=="paper":
        print(" you won!")
        user_score =user_score+1
    elif user_input =="rock" and computer_picks=="rock":
        print("clash")
        clashed=clashed+1
    elif user_input =="paper" and computer_picks=="paper":
        print("clash")
        clashed=clashed+1
    elif user_input =="scissors" and computer_picks=="scissors":
        print("clash")  
        clashed=clashed+1      
    else:
        print("you lost!")
        computer_score=computer_score+1
print("you won ",user_score, "Times")
print("CPU won",computer_score, "Times")
print("Game clashed",clashed)
