# Task 3
# Read the throughput values from a file and then use your jainsall function to calculate a JFI
# JFI = Square of the sum of all throughputs/(N x sum of squares of all throughputs)

with open("text.txt") as file:                      # Open text file
    data = file.read()                              # Read contents of file and save to variable 'data'
# Split 'data' string into characters, iterate through them and save numeric values to 'throughputs' list
throughputs = [int(i) for i in data.split() if i.isdigit()]

def jainsall(list):
    sum1 = 0
    for i in list:
        sum1 = sum1 + int(i)                        # For-loop finds sum of all values in list (values type cast to int)

    sum2 = 0
    for i in list:
        sum2 = sum2 + int(i)**2                     # For-loop finds sum of squares of all values in list (values type cast to int)

    result = (sum1**2)/(len(throughputs)*sum2)      # Calculates JFI based on the two sums found
    return result

output = jainsall(throughputs)
print('The JFI is ', output)
