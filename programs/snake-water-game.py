import random
print("**********Game**********")
player = 0
computer = 0
total_chances = 10
draw = 0
remaining= 0
list = {1: 'snake',2:'water',3:'gun'}
for i in range(1,11):
    print("Enter your choice:\n")
    try:
        for key,value in list.items():
            print(f"Choose {key} choose {value}")
    except Exception as e:
        print("Wrong Input")

    Input = int(input())
    playerInput = list[Input]
    print("You choose: ", playerInput)
    Choice = random.randint(1,3)
    compChoice = list[Choice]
    print("Computer choose: ", compChoice )

    if(playerInput == compChoice):
        print("Game Draw!Equal Points")
        draw +=1
        print(f"\nPoints\nPlayer = {player}\nComputer = {computer}")

    elif(playerInput == 'snake' and compChoice == 'water'):
        print("\nPlayer wins!")
        player += 1
        print(f"\nPoints\nPlayer = {player}\nComputer = {computer}")

    elif(playerInput == 'snake' and compChoice == 'gun'):
        print("\nComputer wins!")
        computer += 1
        print(f"\nPoints\nPlayer = {player}\nComputer = {computer}")

    elif (playerInput == 'water' and compChoice == 'snake'):
        print("\nComputer wins!")
        computer += 1
        print(f"\nPoints\nPlayer = {player}\nComputer = {computer}")

    elif (playerInput == 'water' and compChoice == 'gun'):
        print("\nPlayer wins!")
        player += 1
        print(f"\nPoints\nPlayer = {player}\nComputer = {computer}")

    elif (playerInput == 'gun' and compChoice == 'snake'):
        print("\nPlayer wins!")
        player += 1
        print(f"\nPoints\nPlayer = {player}\nComputer = {computer}")

    elif (playerInput == 'gun' and compChoice == 'water'):
        print("\nComputer wins!")
        computer += 1
        print(f"\nPoints\nPlayer = {player}\nComputer = {computer}")
    remaining = total_chances - i
    print(f"\n{remaining } chances left out of {total_chances}")

print(f"Draws: {draw}")
if(computer==player):
    print("Game Draw")
elif(computer > player):
    print("Computer Won")
elif(computer < player):
    print("\n******Player won******")