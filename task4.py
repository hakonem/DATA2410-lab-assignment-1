with open ("text2.txt") as file:
    data = file.read()
    num = [int(i) for i in data.split() if i.isdigit()]
    test = num[1]/1000
    num[1] = test
    print(num)


def jainsall(list):
    sum1 = 0
    for i in list:
        sum1 = sum1 + float(i)                        # For-loop finds sum of all values in list (values type cast to int)

    sum2 = 0
    for i in list:
        sum2 = sum2 + float(i)**2                     # For-loop finds sum of squares of all values in list (values type cast to int)

    result = (sum1**2)/(len(num)*sum2)      # Calculates JFI based on the two sums found
    return result
              
output = jainsall(num)   
print(output)
