# TASK 3
# Reads the throughput values from a file ('text.txt') and then uses jainsall function to calculate a JFI

from task2 import jainsall                          # Imports the jainsall function from task2.py

with open("text.txt") as file:                      # Open text file
    data = file.read()                              # Read contents of file and save to variable 'data'
# Split 'data' string into characters, iterate through them and save numeric values to 'throughputs' list
throughputs = [float(i) for i in data.split() if i.isdigit()]


output = jainsall(throughputs)                      # jainsall function called with list as arg, result saved as output
print('The JFI is ', output)                        # Output printed to screen
