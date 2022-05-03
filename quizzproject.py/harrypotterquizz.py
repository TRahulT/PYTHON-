print("Welcome to my computer Quiz  World !"  )
playing = input("Do you want to play ? ")
if playing.lower()!="yes":
    print("\nNot A Problem ,Take Your Time\n")
    quit()
score = 0
print("O K A Y   L E T ' S   P L A Y ")
print("\nThis  quiz contains total 10 Questions each carry 5 marks\nThere is no negative marking ")
answer=input("1.World War I began in which year? ")
if answer.lower()=="1914":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
answer=input("2.when was india won the first One  day Cricket World Cup? ")
if answer.lower()=="1983":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
answer=input("3.Who killed the  king Ravan? ")
if answer.lower()=="ram":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
answer=input("4.What  is the name of Krishna's  First love? ")
if answer.lower()=="radha":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
answer=input("5.What is the full form of RAM? ")
if answer.lower()=="random access memory":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
answer=input("6.How many seasons in Game of Thorones web series? ")
if answer.lower()=="8":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
answer=input("7.where is Tomi live? ")
if answer.lower()=="florida":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
answer=input("8.who was the King of Hobbits in hobbit web series (killed oaks king)? ")
if answer.lower()=="thorin":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
answer=input("9.Name the world's largest country? ")
if answer.lower()=="russia":
    print(" C O R R E C T !")
    score += 1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
answer=input("10.Name the border between India and Pakistan ? ")
if answer.lower()=="radcliffe line":
    print(" C O R R E C T !")
    score +=1
else:
    print(" I N C O R R E C T !")
    score = score - 0.25
print(" You got "+ str(score)+ " questions correct ")
print(" Your score " + str(score*5) + " marks")
print(" You got  "+ str((score/10)*100) +"% Correct")
