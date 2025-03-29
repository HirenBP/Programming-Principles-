
print ('Welcome to the Adder REPL')
vars = dict()
command = input('??? '.strip())
def do_input(vars,var):
    if not var.isalpha():
        print('Syntax error')
    else:
        inp = input('Enter a value for ' + var + ': ').strip()
        if inp.isdigit():
            vars[var] = inp
        else:
            print('Syntax error')
def do_print(vars, param):
    if param not in vars:
        print('Syntax error')
    else:
        print('Value of ' + param + ' is ' + str(vars[param]) + '.')

def do_gets(vars, param, param1):
        if param1.isalpha() and param1 not in vars:
            print('Syntax error')
        elif param1.isdigit():
            vars[param] = param1
        elif param1.isalpha():
            vars[param] = vars[param1]
        else:
            print('Syntax error')

def adds_command(vars, var, val):

    if var.isalpha() and val.isdigit():

        if var in vars:

            vars[var] = int(vars[var]) + int(val)
        else:
            vars[var] = int(val)
    elif var.isalpha() and val.isalpha():
        if var in vars and val in vars:
            vars[var] = int(vars[var]) + int(vars[val])

    else:
        # Print an error message
        print(f"Syntax error.")


while command != 'quit':
    cs = command.split()
    if len(cs) == 2 and cs[0] == 'print':
        do_print(vars,cs[1])
    elif len(cs) == 2 and cs[0] == 'input':
        do_input(vars,cs[1])
    elif len(cs) == 3 and cs[1] == 'gets':
        do_gets(vars,cs[0],cs[2])
    elif len(cs) == 3 and cs[1] == 'adds':
        adds_command(vars,cs[0],cs[2])
    else:
        print('Syntax error')
    command = input('??? ')
print('Goodbye')

