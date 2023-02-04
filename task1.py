# TASK 1
# The jains function takes two parameters - tp1 and tp2 - which refer to the throughput values input by the user.
# The function performs the following calculation:
# JFI = Square of the sum of all throughputs/(number of throughputs x sum of squares of all throughputs)
# and returns the JFI in the result variable.

def jains(tp1, tp2):
    result = ((tp1+tp2)**2)/(2*(tp1**2+tp2**2))             # Function calculates JFI
    return result                                           # Returns JFI

# EXCEPTION HANDLING
# To ensure that the user inputs two numeric values, the input methods are enclosed within try-except blocks.
# If the inputs cannot be converted to floats, a ValueError exception is thrown and the user is prompted to try again.
# The while True loops means that the user will continue to receive prompts until a valid value is input.
# Successful inputs are assigned to the variables n1 and n2, which will be used as arguments when jains is called.

while True:
    try:
        n1 = float(input('Enter throughput value 1: '))             # User inputs first value
    except ValueError:
        print("Need to input a number")                             # NaN? Print error message to screen and new input prompt
        continue
    else:
        break                                                       # Valid value input
while True:
    try:
        n2 = float(input('Enter throughput value 2: '))             # User inputs second value
    except ValueError:
        print("Need to input a number")                             # NaN? Print error message to screen and new input prompt
        continue
    else:
        break                                                       # Valid value input

output = jains(n1, n2)                              # jains function called with inputs as args, result saved as output
print('The JFI is ', output)                        # Output printed to screen