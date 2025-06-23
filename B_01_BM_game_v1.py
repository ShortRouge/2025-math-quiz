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
pick the number of rounds, there are three questions per round
then answer the questions it will show if it is right or wrong
    """)

# check for an integer more than 0 (allows <enter>)
def int_check(question):
    global response
    while True:
        error = "please enter an integer that is 1 or more"

        to_check = input(question)

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
questions_right = 0
rounds_loss = 0
question = 0
game_history = []
mode = "regular"

# ask user for number of rounds / infinite mode
num_rounds = int_check("how many rounds would you like?")


# game loop starts here
while rounds_played < num_rounds:

    # this code randomizes the questions so their different every time
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    num4 = random.randint(1, 10)
    num5 = random.randint(1, 10)
    num6 = random.randint(1, 10)



    # the rounds heading showing number of rounds played and rounds left
    rounds_heading = f"\n💿💿💿 round {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)
    print()

    # asks questions for multiplication and says if answer given by user is right or wrong
    question += 1
    user_choice = int_check(f"what does {num1} x {num2} = ")
    answer2 = num1 * num2
    if user_choice == answer2:
        answer2 = "right"
        print("✅✅you got it right✅✅")
        rounds_won += 1
    else:
        answer2 = "wrong"
        print("❌❌you got it wrong❌❌")
        rounds_loss += 1

    # asks questions for addition and says if answer given by user is right or wrong
    question += 1
    user_choice = int_check(f"what does {num3} + {num4} = ")
    answer3 = num3 + num4
    if user_choice == answer3:
        answer3 = "right"
        print("✅✅you got it right✅✅")
        rounds_won += 1
    else:
        answer3 = "wrong"
        print("❌❌you got it wrong❌❌")
        rounds_loss += 1

    # asks questions for subtraction and says if answer given by user is right or wrong
    question += 1
    user_choice = int_check(f"what does {num5} - {num6} = ")
    answer4 = num5 - num6
    if user_choice == answer4:
        answer4 = "right"
        print("✅✅you got it right✅✅")
        rounds_won += 1
    else:
        answer4 = "wrong"
        print("❌❌you got it wrong❌❌")
        rounds_loss += 1

    # shows the user how much they got right
    print("round history")

    feedback = answer2, answer3, answer4
    print(feedback)

    history_item = f"Round {rounds_played + 1}: {feedback}"

    game_history.append(history_item)

    rounds_played += 1

# loop ends here
print()
print("### game history ###")

for item in game_history:
    print(item)
