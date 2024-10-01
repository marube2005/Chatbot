import random

choices = ["rock","paper","scissors"]

while True:

 computer = random.choice(choices)

 my_choice = input("rock, paper, scissors?").lower()

 if my_choice == computer:
   print(computer)
   print("It's a tie!")
   
 elif my_choice == "rock":  
    if computer == "paper":
     print(computer)
     print("You lose!")
    elif computer == "scissors":
      print(computer)
      print("You win")

 elif my_choice == "scissors":
    if computer == "paper":
     print(computer)
     print("You win!")
    elif computer == "rock":
     print(computer)
     print("You loose!")

 elif my_choice == "paper":
    if computer == "scissors":
     print(computer)
     print("You lose!")
    elif computer == "rock":
     print(computer)
     print("You win!")

  play_again = input("Play Again? (y/n): ").lower()

  if play_again != "y":
      break

print("Bye!")