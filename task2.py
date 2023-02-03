# Task 2
# Function takes a list of throughput values and returns JFI
# JFI = Square of the sum of all throughputs/(N x sum of squares of all throughputs)
def jainsall(list):
    sum1 = 0
    for i in list:
        sum1 = float(sum1) + float(i)                        # For-loop finds sum of all values in list (values type cast to int)

    sum2 = 0
    for i in list:
        sum2 = float(sum2) + float(i)**2                     # For-loop finds sum of squares of all values in list (values type cast to int)

    result = (sum1**2)/(length*sum2)      # Calculates JFI based on the two sums found
    return result


throughputs = []                        # Creating a empty list for user input
i = 1                                   # Variable to keep track of list lenght
while True:                             # While loop for deciding the lenght of the  list
    try:
        length = int(input("Enter the length of the list : ")) # Variable for the max amout of elements in list decided by user input
    except ValueError:                                         # Prints message if ValueError occurs until user input is acceptible
        print("Need to input a whole number")
    else:
        #Length input is accepteble
        break                                                  #breaks the loop

while i <= length:                                  # While loop to decide the elements in the list until the list length is reached
    try:
        uinput = float(input("enter item : "))      # Variable for the elements that will be inserted into the list
        throughputs.append(uinput)                  # Inserts the uinput variable into the list
    except ValueError:                              # Prints out message is ValueError occurs until user input is acceptible
        print("Need to input a number")
    else:                                           # Add +1 to the value of i
        i += 1


output = jainsall(throughputs)                      # Function called and takes list as args, result saved as output
print('The JFI is ', output)                        # Output printed to screen