# Check if a number is a palindrome or not
# A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome.
"""Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome."""


x=121
if x<0:
    print("false")
else:    
    if int(str(x)[::-1])==x:
        print("true")
    else:
        print("false")
    



