n = 8

if (n & 1) == 1:
    print("odd")
else:
    print("even")
# using bitwise AND operator to check if a number is odd or even. 
# If the least significant bit (LSB) is 1, the number is odd; if it's 0, the number is even.