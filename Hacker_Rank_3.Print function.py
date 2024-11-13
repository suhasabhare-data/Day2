# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following
# Note that "" represents the consecutive values in between.
# Example
# n = 5
# Print the string .
# Input Format
# The first line contains an integer .
# Constraints
# Output Format
# Print the list of integers from  through  as a string, without spaces.
# Sample Input 3
# output = 123
def print_back_numbers():
    n = int(input("Enter integer"))
    for i in list(range(1,n+1)):
        print(i,end='')

print_back_numbers()
