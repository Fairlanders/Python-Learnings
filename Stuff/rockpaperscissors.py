import random
choices = ["scissors","rock","paper"]

print("Welcome to the rock paper scissors brother.")
print("Please type your choice: ",end="")
player_choice = input("").lower()

while not(player_choice =="scissors" or player_choice =="rock" or player_choice =="paper"):
    print("Please type a valid word.")
    player_choice = input("").lower()

computer_choice = random.choice(choices)

if(computer_choice == "scissors" and player_choice == "paper"):
    print(computer_choice + " was chosen by the computer. You lost LMAO. Imagine losing to a computer 😂")
elif(computer_choice == "scissors" and player_choice == "rock"):
    print(computer_choice + " was chosen by the computer. You won kiddo.")
elif(computer_choice == "scissors" and player_choice == "scissors"):
    print(computer_choice + " was chosen by the computer. A draw, unfortunately.")
elif(computer_choice == "rock" and player_choice == "scissors"):
    print(computer_choice + " was chosen by the computer. You lost LMAO. Imagine losing to a computer 😂")
elif(computer_choice == "rock" and player_choice == "paper"):
    print(computer_choice + " was chosen by the computer. You won kiddo.")
elif(computer_choice == "rock" and player_choice == "rock"):
    print(computer_choice + " was chosen by the computer. A draw, unfortunately.")
elif(computer_choice == "paper" and player_choice == "scissors"):
    print(computer_choice + " was chosen by the computer. You lost LMAO. Imagine losing to a computer 😂")
elif(computer_choice == "paper" and player_choice == "rock"):
    print(computer_choice + " was chosen by the computer. You won kiddo.")
elif(computer_choice == "paper" and player_choice == "paper"):
    print(computer_choice + " was chosen by the computer. A draw, unfortunately.")





