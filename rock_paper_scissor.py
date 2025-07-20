import random
print("Welcome to rock paper and scissor game!!")
choices=["rock","paper","scissor"]
computer_choice=random.choice(choices)
user_choice=input("chose any of these(rock,paper,scissor):-").lower()
print(f"You chose {user_choice} and computer chose {computer_choice}")
user_score=0
computer_score=0
if ((user_choice=="rock" and computer_choice=="scissor") or
    (user_choice=="paper" and computer_choice=="rock") or
    (user_choice=="scissor" and computer_choice=="paper")):
    print("You Won!!")
    user_score+=1
    
elif((user_choice=="rock"and computer_choice=="paper") or 
    (user_choice=="paper"and computer_choice=="scissor") or
    (user_choice=="scissor"and computer_choice=="rock")):
    computer_score+=1
    print(f"You lose!!")
else:
    print("Its a draw!!")
print(f"Scores Your score:{user_score}\n computer_score:{computer_score}")
play_again=input("Do you wnat to play again (yes/no):-").lower()
if play_again!="yes":
    print("Thanks for playing")