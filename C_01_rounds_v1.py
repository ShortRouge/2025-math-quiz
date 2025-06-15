import random

# check for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


mode = "regular"
rounds_played = 0
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

num_rounds = int_check("how many questions would you like? push <enter> for infinite: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # round headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 round {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)
    print()


    print(f"what does {num1} x {num2} = ")
    answer2 = num1 * num2
    user_choice = int(input())
    if user_choice == answer2:
        print("you got it right")
    else:
        print("you got it wrong")

    if user_choice == "xxx":
        break


    rounds_played += 1