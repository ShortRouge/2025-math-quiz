import  random

rounds_played = 0
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


num_rounds = int_check("how many rounds ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

num_questions = int_check("how many questions do u want")

if num_questions == "infinite":
    mode = "infinite"


num4 = random.randint(1, 10)
num3 = random.randint(1, 10)
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num6 = random.randint(1, 10)
num5 = random.randint(1, 10)
points = [0]

# game loop starts here
while rounds_played < num_rounds:

    rounds_heading = f"\n💿💿💿 question {rounds_played + 1} of {num_questions}💿💿💿"

    print(rounds_heading)

    print(f"what does {num1} x {num2} = ")
    answer2 = num1 * num2
    user_choice = int(input(""))
    if user_choice == answer2:
        print("you got it correct")
    else:
        print("you got it wrong")

        print(f"what does {num3} + {num4} = ")
        answer2 = num3 + num4
        user_choice = int(input())

        if user_choice == answer2:
            print("✅✅you got it right✅✅")
        else:
            print("❌❌you got it wrong❌❌")

        print(f"what does {num5} - {num6} = ")
        answer2 = num5 - num6
        user_choice = int(input())
        if user_choice == answer2:
            print("✅✅you got it right✅✅")
        else:
            print("❌❌you got it wrong❌❌")

        if num_rounds > rounds_played:
            break




