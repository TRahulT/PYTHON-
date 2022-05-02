import random
guesses=0
input_number= input("Enter a number : ")
if input_number.isdigit():
    input_number= int(input_number)
    if input_number <=0:
        print("Please enter  a larger number next time :")
        quit()
else:
    print(" please enter the digit next time .")
    quit()
random_number=random.randint(0,input_number)
while True:
    guesses +=1
    user_guess=input("make a guess")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("make another guess")
        continue
    if user_guess==random_number:
        print(" You Got it !")
        break
    else:
        if user_guess>random_number:
            print("You are above the number!")
        else:
            print("you are below the number!")
print(" You made " +str(guesses)+ " guesses in Total")
