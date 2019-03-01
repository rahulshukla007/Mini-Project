#Snake Water Gun Game

import random
game = ["s","w","g"]

print("For snake Enter: s")
print("For water Enter: w")
print("For gun   Enter: g")


i = 9
user_points = 0
comp_points = 0
while i >= 0:
    user = input("Enter Snake,Water,Gun:\n ")
    comp = random.choice(game)

    if user == comp:
        print(f"Your input {user} and computer input {comp}")
        print("There is a Tie")

    elif user == "s" and comp=="w":
        user_points = user_points + 1
        print(f"Your input {user} and computer input {comp}")
        print("You win by 1 points")

    elif user == "s" and comp=="g":
        print(f"Your input {user} and computer input {comp}")
        comp_points = comp_points + 1
        print("Computer win by 1 points")

    elif user == "w" and comp=="g":
        user_points = user_points + 1
        print(f"Your input {user} and computer input {comp}")
        print("You win by 1 points")

    elif user == "w" and comp=="s":
        print(f"Your input {user} and computer input {comp}")
        comp_points = comp_points + 1
        print("Computer win by 1 points")

    elif user == "g" and comp=="w":
        print(f"Your input {user} and computer input {comp}")
        comp_points = comp_points + 1
        print("Computer win by 1 points")

    elif user == "g" and comp=="s":
        user_points = user_points + 1
        print(f"Your input {user} and computer input {comp}")
        print("You win by 1 points")

    else:
        print("Point remain same becs you enter wrong input")

    print(f"Your points {user_points} and computer points {comp_points} ")
    print(f"no of chances left {i} out of 10\n")
    i = i - 1


print("Game over")

if comp_points > user_points:
    print(f"You lost by {comp_points - user_points} points")
elif comp_points < user_points:
    print(f"You win by {user_points - comp_points} points")
