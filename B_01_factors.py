# Generates headings ( ----- Heading ---- )
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Factors
- Enter a number between 1 and 200 
- Get your number factorized
- Type 'xxx' to stop program

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

# Generate all factors of a number
def factors(var_to_factor):
    factor_list = []
    for i in range(1, var_to_factor + 1):
        if var_to_factor % i == 0:
            factor_list.append(i)
    return factor_list


# Main Routine

statement_generator("The Ultimate Factor Finder", "-")

want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break

    # get factors for integers that are 2 or more
    elif to_factor != 1:
        all_factors = factors(to_factor)

    # set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY, it only has one factor. itself :P"

    # comments for square / primes
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special"

    # output factors and comment
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)
