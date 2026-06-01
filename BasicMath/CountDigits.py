# Count the number of digits in a number

# You are given an integer n. You need to return the number of digits in the number.
# The number will have no leading zeroes, except when the number is 0 itself.

# using while loop with somre basic math
n=456

count=0

while n>0:
    n=n//10
    count+=1
print(count)    
    
    
# using len(str(n))
n=456
print(len(str(n)))