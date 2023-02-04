# TASK 2
# The jainsall function takes a list of throughput values input by the user and performs the following calculations:
# 1) Sum of all throughputs in the list
# 2) Sum of squares of all throughputs in the list
# 3) JFI = Square of sum 1 / Length of list (i.e. number of throughputs) x sum 2
# and returns the JFI in the result variable.
# Exceptions are handled with try-catch blocks as for task 1.

def jainsall(list):
    sum1 = 0                                        # Initialise sum1 to 0
    for i in list:
        sum1 = sum1+i                               # For-loop finds sum of all values in list

    sum2 = 0                                        # Initialise sum2 to 0
    for i in list:
        sum2 = sum2 + i**2                          # For-loop finds sum of squares of all values in list

    result = (sum1**2)/(len(list)*sum2)             # Calculates JFI based on the two sums found and the length of the list
    return result                                   # Returns JFI


# This if-block evaluates to false when the file is imported to another file i.e. this code will only be executed when
# task2.py is run directly
if '__main__' == __name__:
    throughputs = []                                    # Creating an empty list for user input
    i = 1                                               # Variable to keep track of list length
    while True:                                         # While-loop for deciding the length of the list
        try:
            length = int(input('Enter the length of the list: '))   # Variable for the max amount of elements in list decided by user input
        except ValueError:                                          # Prints message if ValueError occurs until user input is valid
            print('Need to input a whole number')
        else:
            #Length input is valid
            break                                                   # Breaks the loop

    while i <= length:                                  # While-loop to decide the elements in the list until the list length is reached
        try:
            uinput = float(input('Enter throughput value: '))      # Variable for the elements that will be inserted into the list
            throughputs.append(uinput)                  # Appends the uinput variable to the list
        except ValueError:                              # Prints out message is ValueError occurs until user input is valid
            print('Need to input a number')
        else:                                           # Add +1 to the value of i
            i += 1

    output = jainsall(throughputs)                      # jainsall function called with list as arg, result saved as output
    print('The JFI is ', output)                        # Output printed to screen