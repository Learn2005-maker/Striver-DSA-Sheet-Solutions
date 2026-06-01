# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. 
# Return the GCD of the two numbers.

# The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

import math

print(math.gcd(12,15))  # Output: 3
print(math.gcd(4,6))

# Brute Force Way
def gcd(a,b):
    gcf=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcf=i
    return gcf

n1=4
n2=6

print(gcd(n1,n2))





# Ecludian Alogrithm to solve gcd of two numbers
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a 
print(gcd(4,6))
# print(gcd(46,88))


# Lcm of two numbers
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

print(lcm(4,6))  # Output: 12










