'''
1 for stone
-1 for paper 
0 for scissor 

'''


# Importing random module for generating random choices
import random  

# Generate a random choice for computer  
computer = random.choice([-1, 0, 1])  

userinput = input("enter your choice [ 's' stone, 'p' paper, or 'sc' scissor. ] : ").strip().lower()  # user se input le liya  

userdictionary = {"s": 1, "p": -1, "sc": 0}  # input stored in a dictionary  

revdict = {1: "Stone", -1: "Paper", 0: "Scissor"}

# Conditions  
if userinput not in userdictionary:  
    print("\nInvalid input! Please enter 's' for stone, 'p' for paper, or 'sc' for scissor.\n")  
else:  
    user = userdictionary[userinput]  # input saved in user  

#both choices 
    print(f"\nComputer chose: {revdict[computer]}\nYou chose: {revdict[user]}\n")  

    # Game result conditions  
    if computer == user:  
        print("It's a draw!!")  
    elif (computer == -1 and user == 0) or (computer == 1 and user == -1) or (computer == 0 and user == 1):  
        print("🎉 You Win!! 🎉")  
    else:  
        print("😞 You Lose... Try again later! 😞\n")  
