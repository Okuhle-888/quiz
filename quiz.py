print("WELCOME TO OKUHLE'S QUIZ")

playing = input("Do you want to take part on my quiz? ")

if playing != "yes":
    quit()
print("Okay let's get started!")

score= 0

answer= input("What does CPU stands for? ")


if answer.lower() == "central processing unit":
    print("Correct")
    score+=1

else:
    print("Incorrect")

answer= input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score+=1

else:
    print("Incorrect")

answer= input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct")
    score+=1

else:
    print("Incorrect")

answer= input("What does API stands for? ")
if answer.lower() == "application programming interface":
    print("Correct")
    score+=1

else:
    print("Incorrect")

answer= input("What does ALU stands for? ")
if answer.lower() == "arithmatic logical unit":
    print("Correct")
    score+=1

else:
    print("Incorrect")

answer= input("What does BCD stands for? ")
if answer.lower() == "binary coded decimal":
    print("Correct")
    score+=1

else:
    print("Incorrect")

answer= input("What does BIOS stands for? ")
if answer.lower() == "basic input output sytem":
    print("Correct")
    score+=1

else:
    print("Incorrect")

    answer= input("What does CD stands for? ")
if answer.lower() == "computer disk":
    print("Correct")
    score+=1

else:
    print("Incorrect")

answer= input("What does DAP stands for? ")
if answer.lower() == "direct access protocol":
    print("Correct")
    score+=1

else:
    print("Incorrect")

answer= input("What does ELM stands for? ")
if answer.lower() == "electronic mail":
    print("Correct")
    score+=1

else:
    print("Incorrect")



print("You got" + str(score)+ "questions correct")