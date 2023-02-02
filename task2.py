# Task 2
# Function takes a list of throughput values and returns JFI
# JFI = Square of the sum of all throughputs/(N x sum of squares of all throughputs)
def jainsall(list):
    sum1 = 0
    for i in list:
        sum1 = sum1 + int(i)                        # For-loop finds sum of all values in list (values type cast to int)

    sum2 = 0
    for i in list:
        sum2 = sum2 + int(i)**2                     # For-loop finds sum of squares of all values in list (values type cast to int)

    result = (sum1**2)/(len(throughputs)*sum2)      # Calculates JFI based on the two sums found
    return result


input_list = input('Enter list of throughputs separated by a space: ')      # User inputs throughput values
throughputs = input_list.split()                    # Input converted to list (of strings)
output = jainsall(throughputs)                      # Function called and takes list as args, result saved as output
print('The JFI is ', output)                        # Output printed to screen