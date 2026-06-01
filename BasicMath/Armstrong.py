
# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.


"""
Take input number n.
Count the number of digits in n.
Split the number into digits.
Raise each digit to the power of total digits and sum them up.
If the sum equals the original number, it's an Armstrong number.
"""
    
    
def isArmstrong(n):
    # Convert number to string to easily count digits
    digits=str(n)
    num_digits=len(digits)
    total= sum(int(digit)**num_digits for digit in digits)
    return total==n
print(isArmstrong(153))  # Output: True
print(isArmstrong(123))  # Output: False

