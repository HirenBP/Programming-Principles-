# Define a dictionary to store the variables and their values
variables = {}

# Define a function to check if a string is a valid variable name
def is_variable(name):
    # A variable name must contain only letters
    return name.isalpha()

# Define a function to check if a string is a valid natural number
def is_number(num):
    # A natural number must contain only digits and be greater than zero
    return num.isdigit() and int(num) > 0

# Define a function to check if a string is a valid value
def is_value(val):
    # A value can be either a variable name or a natural number
    return is_variable(val) or is_number(val)

# Define a function to get the value of a variable or a number
def get_value(val):
    # If the value is a variable name, return its value from the dictionary
    # If the value is a natural number, return it as an integer
    # If the value is invalid, raise an exception
    if is_variable(val):
        if val in variables:
            return variables[val]
        else:
            raise NameError(f"{val} is undefined.")
    elif is_number(val):
        return int(val)
    else:
        raise ValueError(f"{val} is not a valid value.")

# Define a function to handle the quit command
def quit_command():
    # Print a goodbye message and exit the program
    print("Goodbye.")
    exit()

# Define a function to handle the input command
def input_command(var):
    # Check if the variable name is valid
    if is_variable(var):
        # Prompt for and allow the user to enter a value
        val = input(f"Enter a value for {var}: ")
        # Check if the value is valid
        if is_value(val):
            # Assign the value to the variable in the dictionary
            variables[var] = get_value(val)
        else:
            # Print an error message
            print(f"{val} is not a valid value.")
    else:
        # Print an error message
        print(f"{var} is not a valid variable name.")

# Define a function to handle the print command
def print_command(val):
    # Check if the value is valid
    if is_value(val):
        # Print the value
        print(get_value(val))
    else:
        # Print an error message
        print(f"{val} is not a valid value.")

# Define a function to handle the gets command
def gets_command(var, val):
    # Check if the variable name and the value are valid
    if is_variable(var) and is_value(val):
        # Assign the value to the variable in the dictionary
        variables[var] = get_value(val)
    else:
        # Print an error message
        print(f"Syntax error.")

# Define a function to handle the adds command
def adds_command(var, val):
    # Check if the variable name and the value are valid
    if is_variable(var) and is_value(val):
        # Check if the variable is defined
        if var in variables:
            # Add the value to the variable in the dictionary
            variables[var] += get_value(val)
        else:
            # Print an error message
            print(f"{var} is undefined.")
    else:
        # Print an error message
        print(f"Syntax error.")

# Define a function to handle the unknown command
def unknown_command():
    # Print an error message
    print("Unknown command.")

# Define a dictionary to map the commands to the functions
commands = {
    "quit": quit_command,
    "input": input_command,
    "print": print_command,
    "gets": gets_command,
    "adds": adds_command
}

# Print a welcome message
print("Welcome to the Adder REPL.")

# Start a while loop to read and execute the commands from the user
while True:
    # Prompt for and read a command from the user
    command = input("??? ")
    # Split the command by whitespace
    words = command.split()
    # Check if the command is empty
    if not words:
        # Skip to the next iteration
        continue
    # Get the first word as the keyword
    keyword = words[0]
    # Check if the keyword is in the commands dictionary
    if keyword in commands:
        # Get the function associated with the keyword
        func = commands[keyword]
        # Check the number of arguments required by the function
        num_args = func.__code__.co_argcount
        # Check if the number of words matches the number of arguments
        if len(words) == num_args + 1:
            # Call the function with the remaining words as arguments
            func(*words[1:])
        else:
            # Print an error message
            print("Wrong number of arguments.")
    else:
        # Call the unknown command function
        unknown_command()
