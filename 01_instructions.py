# check user enter yes (y) or no (n)
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
    to begin with pick amount of questions to answer.
    then the math questions""")


# main routine
print()
print("this is a math quiz")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want to see the instructions")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("program continues")
