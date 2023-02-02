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

    result = (sum1**2)/(length*sum2)      # Calculates JFI based on the two sums found
    return result


readylist = []
i = 1
while True:
    try:
        length = int(input("Enter the length of the list :"))
    except ValueError:
        print("Need to input a number")
        continue
    else:
        #Length input is accepteble
        break

while i <= length:
    try:
        uinput = int(input("enter item:"))
        readylist.append(uinput)
    except ValueError:
        print("Need to input a number")
    else:
        i += 1


output = jainsall(readylist)                      # Function called and takes list as args, result saved as output
print('The JFI is ', output)                        # Output printed to screen