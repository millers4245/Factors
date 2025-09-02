# Generates headings ( ----- Heading ---- )
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Factors
- Instruction 1 
- Instruction 2
- Instruction 3  

    ''')

def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            response = int(response)

            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine

statement_generator("The Ultimate Factor Finder", "-")

want_instructions= input("\nPress <enter> to read the instructions "
                         "or any key to continue")

if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
