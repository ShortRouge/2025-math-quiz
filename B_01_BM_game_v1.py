import random

def yes_no(question):
    """check user response to a question is yes / no (y/n), return 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check if user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """print instructions"""

    print("""
pick the number of rounds
then answer the questions
    """)

# check for an integer more than 0 (allows <enter>)
def int_check(question):
    global response
    while True:
        error = "please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check that the number is more than / equal to 13
            if random.randint(1, 100):
                return response
            else:
                print(error)


        except ValueError:
            print(error)

# main routine
print()
print("this is a math quiz")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want to see the instructions")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

rounds_played = 0
rounds_won = 0
rounds_loss = 0
question = 0
game_history = []
mode = "regular"

# ask user for number of rounds / infinite mode
num_rounds = int_check("how many rounds would you like? push <enter> for infinite: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# game loop starts here
while rounds_played < num_rounds:

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    num4 = random.randint(1, 10)
    num5 = random.randint(1, 10)
    num6 = random.randint(1, 10)



    # round headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 round {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)
    print()


    question += 1
    user_choice = int_check(f"what does {num1} x {num2} = ")
    answer2 = num1 * num2
    if user_choice == answer2:
        print("✅✅you got it right✅✅")
        rounds_won =+ 1
    else:
        print("❌❌you got it wrong❌❌")
        rounds_loss += 1

    question += 1
    user_choice = int_check(f"what does {num3} + {num4} = ")
    answer3 = num3 + num4
    if user_choice == answer3:
        print("✅✅you got it right✅✅")
        rounds_won += 1
    else:
        print("❌❌you got it wrong❌❌")
        rounds_loss += 1

    question += 1
    user_choice = int_check(f"what does {num5} - {num6} = ")
    answer4 = num3 - num4
    if user_choice == answer4:
        print("✅✅you got it right✅✅")
        rounds_won += 1
    else:
        print("❌❌you got it wrong❌❌")
        rounds_loss += 1


    print("round history")
    print(f"you got {rounds_won} / {question}")

    rounds_played += 1

game_history = yes_no("Do you want your game history")
if game_history == "yes":
    print("")
    print("game history")
    print(f"rounds Loss: {rounds_loss}")
    print(f"rounds won: {rounds_won}")

