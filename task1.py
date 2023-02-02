# Task 1
# Function takes two throughput values as args and returns JFI
# JFI = Square of the sum of all throughputs/(N x sum of squares of all throughputs)
def jains(tp1, tp2):
    result = ((tp1+tp2)**2)/(2*(tp1**2+tp2**2))     # Function calculates JFI
    return result


n1 = int(input('Enter throughput value 1: '))       # User inputs first throughput value
n2 = int(input('Enter throughput value 2: '))       # User inputs second throughput value
output = jains(n1, n2)                              # Function called and takes inputs as args, result saved as output
print('The JFI is ', output)                        # Output printed to screen