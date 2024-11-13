# Task
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints
# 1 =< n =< 100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Output 0
# Weird
# Explanation 0
# n is odd and odd numbers are weird, so print Weird.
# n = 24
# n > 20 and n is even. so it is not weird.
weird = 'Weird'
notWeird = 'Not Weird'
n = int(input("Enter Number"))

if n % 2 != 0:
    print(weird)
elif n >= 2 and n <=5:
    print(notWeird)
elif n >= 6 and n <=20:
    print(weird)
else:
    print(notWeird)
 

