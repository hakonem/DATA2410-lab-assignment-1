# TASK 4
# Reads the throughput values from a file ('new_text.txt') and then uses jainsall function to calculate a JFI.
# Line 2 is 1200 Kbps, so the numeric value must be divided by 1000 so that all throughputs are given in the same unit (Mbps).

from task2 import jainsall                          # Imports the jainsall function from task2.py

with open("new_text.txt") as file:                  # Open text file
    data = file.read()                              # Read contents of file and save to variable 'data'
# Split 'data' string into characters, iterate through them and save numeric values to 'throughputs' list
throughputs = [float(i) for i in data.split() if i.isdigit()]
kbps = throughputs[1]                               # Saves the second element into a variable
throughputs[1] = kbps/1000                          # Replaces the second element in the list with kbps/1000


output = jainsall(throughputs)                      # jainsall function called with list as arg, result saved as output
print('The JFI is ', output)                        # Output printed to screen
