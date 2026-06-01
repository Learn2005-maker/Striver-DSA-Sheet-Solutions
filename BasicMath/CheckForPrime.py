# You are given an integer n. You need to check if the number is prime or not. 
# Return true if it is a prime number, otherwise return false.
# A prime number is a number which has no divisors except 1 and itself.

n=-8
is_prime=True

if n<=1:
    is_prime=False
else:    
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    
print(is_prime)    
# Most Efficient Way
# insted of checking up to n-1 we can check up to sqrt(n)
import math
n=29
is_prime=True
if n<=1:
    is_prime=False  
else:   
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            is_prime=False
            break

print(is_prime)


# Check divisors from 2 → √7 ≈ 2.64 → loop runs only for i = 2.
# 7 % 2 != 0 → no divisor found.
# Loop ends, so is_prime stays True.